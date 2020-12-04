#1.created an echo bot as we defined 
#2.creating a simple polling server using flask and telegram which can reply .
import logging
from flask import Flask,request
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters,Dispatcher
from telegram import Bot,Update
#enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)
#Create Updater
TOKEN = "147244:j9kstMdqeT9tfEo6obTxHA6l9Kr-Y7c8"

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

@app.route(f'/{TOKEN}',methods=['GET','POST'])
def webhook():
    #webhook view which recieves updates from telegram
    update = Update.de_json(request.get_json(),bot)
    #process update
    dp.process_update(update)
    return "ok"


def start(bot,update):
    print(update)
    author = update.message.from_user.first_name
    reply = "Hi! {}".format(author)
    bot.send_message(chat_id=update.message.chat_id,text=reply)


def help(bot,update):
    help_text = "hey! this is help text."
    bot.send_message(chat_id=update.message.chat_id,text=help_text)

def echo_text(bot,update):
    reply = update.message.text
    bot.send_message(chat_id=update.message.chat_id,text=reply)

def echo_sticker(bot,update):
    bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)

def error(bot,update):
    logger.error("Update '%s' caused errror '%s'",update,update.error )

#def main():
    #updater = Updater(TOKEN,use_context=False)

    '''updater.start_polling()
    logger.info("Started polling...")
    updater.idle()'''
if __name__ =="__main__":
    bot = Bot(TOKEN)
    bot.set_webhook("https://e51ee54015df.ngrok.io/"+TOKEN)

    #dp = updater.dispatcher
    dp = Dispatcher(bot,use_context=True)

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(MessageHandler(Filters.text,echo_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)
    app.run(port=8443)

