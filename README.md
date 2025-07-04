# 🛰️ mini-ollama-telegram-bot
A **zero-cost, fully-local** Telegram chatbot that pipes user messages straight into an on-device LLM running through [Ollama](https://ollama.com).  
The default model is **TinyLLaMA (420 MB)**, so it fits on low-RAM laptops and the free tiers of most hobby cloud hosts.

---

## 🌟 Why you might like this

* **Free & offline-friendly** – no OpenAI / API keys needed.  
* **Privacy-first** – chats never leave the box that runs Ollama.  
* **Dead-simple** – ~70 lines of Python, one Dockerfile if you want cloud.  
* **Portable** – works on Windows 11, macOS, Linux, WSL, or any x86-64 server.

---

## 🖼️ Architecture (local mode)

```
Telegram App  ──► Telegram Bot API  ──►  mini_bot.py  ──►  Ollama Serve  ──►  TinyLLaMA
      ▲                                                                        │
      └───────────────────────  Reply sent back  ◄─────────────────────────────┘
```

---

## 📂 Project layout

| File / folder       | Purpose                                         |
|---------------------|-------------------------------------------------|
| `mini_bot.py`       | Telegram ↔️ Ollama bridge (async, long-polling) |
| `requirements.txt`  | Python deps (`python-telegram-bot`, `requests`) |
| `Dockerfile`*       | Optional: bake Ollama + model for cloud deploy  |
| `.gitignore`        | Keeps pycache and secrets out of Git            |
| `README.md`         | *You’re reading it!*                            |

\* *The Dockerfile is only needed if you plan to deploy to Koyeb, Fly.io, etc.*

---

## 🛠️ Prerequisites

| Component            | Version / Notes                              |
|----------------------|----------------------------------------------|
| Python               | 3.10 or newer                                |
| Ollama               | Latest release (install script / MSI)        |
| Telegram bot token   | From **[@BotFather](https://t.me/botfather)**|
| Model weights        | `tinyllama` (420 MB) or any model you prefer |

---

## 🚀 Quick start (Local Laptop)

1. **Clone repo**

   ```bash
   git clone https://github.com/YOUR_USERNAME/mini-ollama-telegram-bot.git
   cd mini-ollama-telegram-bot
   ```

2. **Create a virtual-env & install deps**

   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Pull a lightweight model and launch Ollama**

   ```bash
   ollama run tinyllama          # downloads & tests the model
   # After the first run, keep Ollama serving in another terminal:
   ollama serve
   ```

4. **Set your Telegram token and run the bot**

   *Linux / macOS*

   ```bash
   export TELEGRAM_BOT_TOKEN=123456:ABCdef...
   python mini_bot.py
   ```

   *Windows PowerShell*

   ```powershell
   $env:TELEGRAM_BOT_TOKEN="123456:ABCdef..."
   python mini_bot.py
   ```

5. **Talk to your bot**

   Open Telegram → search for your bot’s username → press **Start** → say “Hello” – it replies via TinyLLaMA.

---

## ⚙️ Environment variables

| Variable              | Default              | Description                             |
|-----------------------|----------------------|-----------------------------------------|
| `TELEGRAM_BOT_TOKEN`  | **required**         | Bot token from @BotFather               |
| `OLLAMA_URL`          | `http://localhost:11434` | Change if Ollama runs elsewhere      |
| `OLLAMA_MODEL`        | `tinyllama`          | Any model you’ve pulled with Ollama     |

*Hard-coding secrets is discouraged; use environment variables or a `.env` loader like [python-dotenv](https://pypi.org/project/python-dotenv/).*

---

## ☁️ One-command cloud deploy (Koyeb free tier)

```bash
# inside repo root
koyeb service create mini-ollama-bot \
  --git github.com/YOUR_USERNAME/mini-ollama-telegram-bot \
  --dockerfile ./Dockerfile \
  --instance-type free \
  --env TELEGRAM_BOT_TOKEN=123456:ABCdef...
```

Koyeb’s free tier (512 MB RAM / 2 GB SSD) is enough for `tinyllama`.  
The Dockerfile copies the model cache so rebuilds are fast.

---

## 🧠 Extending ideas

| Idea                     | Hint |
|--------------------------|------|
| **Conversation memory**  | Store `update.message.chat_id` → list[prompt, response] in a dict and send whole history to Ollama. |
| Slash commands (`/help`) | Add `CommandHandler` via `python-telegram-bot`. |
| Switch models on the fly | Accept `/model tinyllama` to set `context.user_data["model"]`. |
| Webhooks                 | Host behind HTTPS and replace polling with `Application.run_webhook`. |

---

## 🛡️ Security & Privacy

* **Never publish your Telegram token in Git.**  
* The bot does not log user messages by default; add logging only if you need it.  
* If you deploy to cloud, note that *all* inference stays on that server — messages still never leave your control.

---

## 📝 License

MIT — do whatever you want, but no warranty.  
If you build something neat, a star on GitHub would be appreciated!

---

> Made with ❤️ and caffeinated by TinyLLaMA + Ollama.
