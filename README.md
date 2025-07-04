
# Mini Ollama Telegram Bot

Minimal, no‑cost Telegram chatbot powered by a local Ollama tiny model.

## Quick start

```bash
# 1. Install Ollama
curl -fsSL https://ollama.com/install.sh | sh   # macOS/Linux
# Windows: download the MSI from ollama.com

# 2. Pull a tiny model
ollama run tinyllama

# 3. Create Telegram bot with @BotFather and copy the token

# 4. Install deps
pip install -r requirements.txt

# 5. Start
ollama serve                # terminal 1
export TELEGRAM_BOT_TOKEN=123456:ABC...
python mini_bot.py          # terminal 2
```
