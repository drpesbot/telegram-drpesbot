import os
from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel

from telegram import Update, Bot

TOKEN = os.environ.get("TOKEN")

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    bot = Bot(token=TOKEN)
    update = Update.de_json(await request.json(), bot)

    if update.message:
        chat_id = update.message.chat_id
        text = update.message.text

        if text == "/start":
            await bot.send_message(
                chat_id=chat_id,
                text="تقدر تتابع كل جديد من القناة هنا:\nhttps://t.me/pes224\nهنا هتلاقي كل جديد عن الاستور وتطبيق التطويرات الخاصة بينا."
            )
        else:
            await bot.send_message(
                chat_id=chat_id,
                text="تقدر تتابع كل جديد من القناة هنا:\nhttps://t.me/pes224\nهنا هتلاقي كل جديد عن الاستور وتطبيق التطويرات الخاصة بينا."
            )
    return {"message": "ok"}

@app.get("/")
def index():
    return {"message": "Hello World"}


