import os
import json
from emailGenerate import EmailGenerate
from flask import Flask, request
from TelegramBot8 import Message, TeleBot, Update, ParseMode

app = Flask(__name__)

TELE_API_KEY = os.getenv('telegramApiKey')
RAPID_API_KEY = os.getenv('rapidApiKey')
bot = TeleBot(TELE_API_KEY)

emailGenerate = EmailGenerate(RAPID_API_KEY)


@bot.add_command_helper(command="/hi")
def hi(message: Message):
    bot.send_message(message.chat.id, "Hello")


@bot.add_command_menu_helper(command="/domain_list", description="Command to get the list of domain")
def domain_list(message: Message):
    listOfDomain = emailGenerate.get_domains()
    payload = "<b>List of domains:</b>\n"
    for index, mail in enumerate(listOfDomain):
        payload += f"<b>{index+1}.</b> {mail} \n"
    bot.send_message(message.chat.id, payload, parse_mode=ParseMode.HTML)


@app.route('/', methods=["POST"])
def hello_world():
    bot.start(json.dumps(request.json))
    return 'ok'


if __name__ == "__main__":
    bot._set_commands()
    app.run()
