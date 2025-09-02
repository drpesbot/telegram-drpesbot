import os
from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel

from telegram import Update, Bot
from telegram.ext import Dispatcher, MessageHandler, filters, CommandHandler

TOKEN = os.environ.get("TOKEN")  # التوكن هيتحدد في Vercel

app = FastAPI()

class TelegramWebhook(BaseModel):
    update_id: int
    message: Optional[dict]

def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="تقدر تتابع كل جديد من القناة هنا:\nhttps://t.me/pes224\nهنا هتلاقي كل جديد عن الاستور وتطبيق التطويرات الخاصة بينا."
    )

def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="تقدر تتابع كل جديد من القناة هنا:\nhttps://t.me/pes224\nهنا هتلاقي كل جديد عن الاستور وتطبيق التطويرات الخاصة بينا."
    )

def register_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

@app.post("/webhook")
def webhook(webhook_data: TelegramWebhook):
    bot = Bot(token=TOKEN)
    update = Update.de_json(webhook_data.__dict__, bot)
    dispatcher = Dispatcher(bot, None, workers=4)
    register_handlers(dispatcher)
    dispatcher.process_update(update)
    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello World"}


