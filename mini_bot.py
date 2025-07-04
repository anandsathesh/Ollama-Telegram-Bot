
import os, requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

OLLAMA_URL = "http://localhost:11434"
MODEL = "tinyllama"

async def respond(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = update.message.text
    try:
        r = requests.post(f"{OLLAMA_URL}/api/generate",
                          json={"model": MODEL, "prompt": prompt, "stream": False},
                          timeout=120)
        answer = r.json().get("response", "⚠️ No response from Ollama")
    except Exception as e:
        answer = f"⚠️ Error: {e}"
    await update.message.reply_text(answer)

if __name__ == "__main__":
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("Set TELEGRAM_BOT_TOKEN env var")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond))
    print("Bot running… Press Ctrl+C to stop.")
    app.run_polling()
