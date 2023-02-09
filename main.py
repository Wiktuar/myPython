from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token= "5948400891:AAEUagQYYa7sLh8vj09J7O7TaCRhVv0ZVWQ")
updater = Updater(token= "5948400891:AAEUagQYYa7sLh8vj09J7O7TaCRhVv0ZVWQ")
dispatcher = updater.dispatcher

def correct(update, context):
    text = update.message.text
    list = text.split()

    for l in list:
        if("абв" in l): list.remove(l)

    resultStr = ""
    for l in list:
        resultStr += l + " "

    context.bot.send_message(update.effective_chat.id, resultStr)

message_handler = MessageHandler(Filters.command, correct)

dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()


