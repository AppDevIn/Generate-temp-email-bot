import os
import json
import uuid

from emailGenerate import EmailGenerate
from flask import Flask, request
from TelegramBot8 import Message, TeleBot, Update, ParseMode, InlineKeyboard, InlineKeyboardButton, CallBackQuery

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
    payload = "<b>List of domains:</b>"
    keybaords = InlineKeyboard()

    for index, mail in enumerate(listOfDomain):
        button = InlineKeyboardButton(text=mail, callback_data="generate_mail")
        keybaords.add(button)
    bot.send_message(message.chat.id, payload, parse_mode=ParseMode.HTML, reply_markup=keybaords)


@bot.callback_handler("generate_mail")
def generate_mail(callback: CallBackQuery):
    callback.answer("Generating e-mail")
    email = str(uuid.uuid4().int) + "@mailkept.com"
    hash_value = emailGenerate.generate_email(email)
    print(hash_value)
    bot.send_message(callback.message.chat.id, email)


@app.route('/', methods=["POST"])
def update():
    bot.start(json.dumps(request.json))
    return 'ok'


if __name__ == "__main__":
    bot._set_commands()
    bot.set_webhook("https://vids-battery-stood-usda.trycloudflare.com")
    app.run()
