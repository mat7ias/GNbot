from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from time import time
import time
import os
from pprint import pprint
import sys
import yaml
import telegram
import random

#### Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - '
                    '%(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure Logging

FORMAT = '%(asctime)s -- %(levelname)s -- %(module)s %(lineno)d -- %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger('root')
logger.info("Running "+sys.argv[0])

##### Open config_file
config = None
if os.path.isfile("bot/GolemBot/config.yaml"):
    with open("bot/GolemBot/config.yaml") as config_file:
        config = yaml.load(config_file)
else:
    exit("No configuration file 'config.yaml' found")
    sys.exit()

##### load config
bot_token = config['bot_token']
bot = telegram.Bot(token=bot_token)

TEAM = config['TEAM']

def get_name(user):
        try:
            name = user.first_name
        except (NameError, AttributeError):
            try:
                name = user.username
            except (NameError, AttributeError):
                logger.info("No username or first name")
                return	""
        return name

################################ Anti-spam #####################################

def spamfilter(bot, update):
    user_id = update.message.from_user.id
    count = config['previouscommand_count']
    chat_id = update.message.chat.id
    pprint(update.message.chat.type)
    if (chat_id == -1001097743663):
        config['previouscommand_count'] = count + 1

################################ Commands ######################################

def start(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    message_id = update.message.message_id
    chat_id = update.message.chat.id
    if (update.message.chat.type == 'group') or (update.message.chat.type == 'supergroup'):
        msg = config['pmme']
        bot.sendMessage(chat_id=chat_id,text=msg,reply_to_message_id=message_id, parse_mode="Markdown",disable_web_page_preview=1)
    else:
        msg = config['start']
        update.message.reply_text("Hey "+str(update.message.chat.first_name)+"! Get a list of my commands with /commands")

def commands(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    msg = config['commands']
    bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def extras(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    msg = config['extras']
    bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def resources(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    msg = config['resources']
    count = config['previouscommand_count']
    message_id = update.message.message_id
    if (count >= 6) and (chat_id == -1001097743663):
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)
        config['previouscommand_count'] = 0
    if (count < 6) and (chat_id == -1001097743663):
        bot.delete_message(chat_id=chat_id,message_id=message_id)
    elif (chat_id != -1001097743663):
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def videos(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    msg = config['videos']
    bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def rules(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    msg = config['rules']
    bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def adminlist(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    msg = config['adminlist']
    bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def releases(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    msg = config['releases']
    bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def carlos(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
    if user_id == 440263207:
    	msg = bot.sendPhoto(chat_id=chat_id, photo=open("carlos.png",'rb'), caption="WHADAMAGANADO")
    if user_id == 474621061:
        msg = bot.sendPhoto(chat_id=chat_id, photo=open("carlos.png",'rb'), caption="THAT'S A SCAM")

def rabbit(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
    bunnylist=["/home/ubuntu/rabbitpic.jpg", "/home/ubuntu/rabbit1.jpg", "/home/ubuntu/rabbit2.jpg", "/home/ubuntu/rabbit3.jpg", "/home/ubuntu/rabbit4.jpg", "/home/ubuntu/rabbit5.jpg", "/home/ubuntu/rabbit6.jpg", "/home/ubuntu/rabbit7.jpg", "/home/ubuntu/rabbit8.jpg", "/home/ubuntu/rabbit9.jpg", "/home/ubuntu/rabbit10.jpg", "/home/ubuntu/rabbit11.jpg", "/home/ubuntu/rabbit12.jpg", "/home/ubuntu/rabbit13.jpg", "/home/ubuntu/rabbit14.jpg", "/home/ubuntu/rabbit15.jpg", "/home/ubuntu/rabbit16.jpg", "/home/ubuntu/rabbit17.jpg", "/home/ubuntu/rabbit18.jpg", "/home/ubuntu/rabbit19.jpg"]
    msg = bot.sendPhoto(chat_id=chat_id, photo=open(random.choice(bunnylist), "rb"))

###############################################################################

###### Error logging
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)

###### Running the bot
def main():
    # Create the EventHandler and pass it your bot's token.
    print("Bot started")
    updater = Updater(bot_token)

##### Get the dispatcher to register handlers
    dp = updater.dispatcher

##### CommandHandlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("commands", commands))
    dp.add_handler(CommandHandler("extras", extras))
    dp.add_handler(CommandHandler("resources", resources))
    dp.add_handler(CommandHandler("videos", videos))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("adminlist", adminlist))
    dp.add_handler(CommandHandler("releases", releases))
    dp.add_handler(CommandHandler("carlos", carlos))
    dp.add_handler(CommandHandler("rabbit", rabbit))

##### MessageHandlers
    dp.add_handler(MessageHandler(Filters.all, spamfilter))

##### Log all errors
    dp.add_error_handler(error)

# Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
