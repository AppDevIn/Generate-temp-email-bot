import os
import json
from emailGenerate import EmailGenerate
from flask import Flask, request
from TelegramBot8 import Message, TeleBot, Update

app = Flask(__name__)

TELE_API_KEY = os.getenv('telegramApiKey')
RAPID_API_KEY = os.getenv('rapidApiKey')
bot = TeleBot(TELE_API_KEY)

emailGenerate = EmailGenerate(RAPID_API_KEY)


@bot.add_command_helper(command="/hi")
def hi(message: Message):
    bot.send_message(message.chat.id, "Hello")


@bot.add_command_helper(command="/domain_list")
def domain_list(message: Message):
    listOfDomain = emailGenerate.get_domains()
    bot.send_message(message.chat.id, listOfDomain)


@app.route('/', methods=["POST"])
def hello_world():
    bot._set_commands()
    bot.start(json.dumps(request.json))
    return 'ok'


if __name__ == "__main__":
    app.run()
