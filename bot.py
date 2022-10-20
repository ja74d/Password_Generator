from telegram.ext import *
from telegram import *
import telegram
import logging
import random

# every password has 16 characters

English = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capital = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
others = ["@", "$", "%", "^", "&", "*", "(", ")", "_", "/", "?"]

total = [English, capital, numbers, others]



updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi\ni'm a simple bot\nmy job is generating 16 character passwords\nto get new password type: /genpass")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def genpass(update: Update, context: CallbackContext):
    global passwd
    passwd = ""
    password = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 16):
        if password[i] == 0:
            password[i] = random.choice(random.choice(total))
    for j in password:
        passwd += j

    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Your Password:\n\n `{passwd}`", parse_mode=telegram.ParseMode.MARKDOWN_V2)


start_handler = CommandHandler('genpass', genpass)
dispatcher.add_handler(start_handler)

updater.start_polling()