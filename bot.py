import os
import json
import uuid
import time

from emailGenerate import EmailGenerate
from flask import Flask, request
from TelegramBot8 import Message, TeleBot, Update, ParseMode, InlineKeyboard, InlineKeyboardButton, CallBackQuery

from models import Mail, Datum

app = Flask(__name__)

TELE_API_KEY = os.getenv('telegramApiKey')
RAPID_API_KEY = os.getenv('rapidApiKey')
PORT = int(os.environ.get('PORT', 5000))
HOST = os.environ.get('HOST', "0.0.0.0")

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
    column1 = []
    column2 = []
    for index, mail in enumerate(listOfDomain):
        button = InlineKeyboardButton(text=mail, callback_data="generate_mail" + mail)
        if index % 2 == 0:
            column2.append(button)
        else:
            column1.append(button)

    for index in range(0, max(len(column1), len(column2))):
        row = []
        if index <= len(column1) - 1:
            row.append(column1[index])
        if index <= len(column2) - 1:
            row.append(column2[index])

        keybaords.add(row)

    bot.send_message(message.chat.id, payload, parse_mode=ParseMode.HTML, reply_markup=keybaords)


@bot.callback_handler(regex="^generate_mail@.*$")
def generate_mail(callback: CallBackQuery):
    callback.answer("Generating e-mail")
    email = str(uuid.uuid4().int) + "@" + callback.data.split("@")[1]
    hash_value = emailGenerate.get_hash(email)
    print(hash_value)
    messageLoad = f"<b>Email Address</b>: {email}"
    bot.send_message(callback.message.chat.id, messageLoad, parse_mode=ParseMode.HTML)


@bot.add_command_menu_helper(command="/check_mailbox", description="To check the mailbox of the email."
                                                                   "Add the email behind the command")
def check_mailbox(message: Message):
    try:
        hashValue = emailGenerate.get_hash(message.text.split()[1])
        mail: Mail = emailGenerate.check_email(hashValue)
        if not mail.hasData():
            bot.send_message(message.chat.id, mail.error)
        else:
            messagePayload = ""
            for m in mail.data:
                messagePayload += _generateMailMessage(m)
                messagePayload += "\n"
            bot.send_message(message.chat.id, messagePayload, parse_mode=ParseMode.HTML)
    except:
        bot.send_message(message.chat.id, "Invalid command usage")


def _generateMailMessage(mail: Datum):
    message_load = f"<b>Mail From</b>: {mail.mail_from.replace('<', '[').replace('>', ']')}\n"
    message_load += f'<b>Sent time</b>: {time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(mail.mail_timestamp))}\n'
    message_load += f"<b>Mail Subject</b>: {mail.mail_subject}\n"
    if mail.mail_text.strip() == "":
        message_load += "<b>Mail Message</b>: The mail message is empty\n"
    else:
        message_load += f"<b>Mail Message</b>: {mail.mail_text.replace('<', '[').replace('>', ']')}\n"
    return message_load


@app.route('/', methods=["POST"])
def update():
    bot.start(json.dumps(request.json))
    return 'ok'


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
    bot.set_webhook(f"{HOST}:{PORT}")
    app.run()
