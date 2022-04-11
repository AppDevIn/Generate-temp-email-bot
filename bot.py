import os
import json
from flask import Flask, request
from TelegramBot8 import Message, TeleBot, Update

app = Flask(__name__)

API_KEY = os.getenv('telegramApiKey')
bot = TeleBot(API_KEY)


@bot.add_command_helper(command="/hi")
def hi(message: Message):
    bot.send_message(message.chat.id, "Hello")


@app.route('/', methods=["POST"])
def hello_world():
    bot._set_commands()
    bot.start(json.dumps(request.json))
    return 'ok'


if __name__ == "__main__":
    app.run()
