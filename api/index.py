import os
from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel

from telegram import Update, Bot
from telegram.ext import Dispatcher, MessageHandler, filters, CommandHandler

TOKEN = os.environ.get("TOKEN")

app = FastAPI()

async def start(update: Update, context):
    await update.message.reply_text(
        "تقدر تتابع كل جديد من القناة هنا:\nhttps://t.me/pes224\nهنا هتلاقي كل جديد عن الاستور وتطبيق التطويرات الخاصة بينا."
    )

async def echo(update: Update, context):
    await update.message.reply_text(
        "تقدر تتابع كل جديد من القناة هنا:\nhttps://t.me/pes224\nهنا هتلاقي كل جديد عن الاستور وتطبيق التطويرات الخاصة بينا."
    )

@app.post("/webhook")
async def webhook(request: Request):
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    update = Update.de_json(await request.json(), bot)
    dispatcher.process_update(update)
    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello World"}


