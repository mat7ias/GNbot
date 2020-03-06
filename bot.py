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
import json

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
if os.path.isfile("./config.yaml"):
    with open("./config.yaml") as config_file:
        config = yaml.load(config_file)
else:
    exit("No configuration file 'config.yaml' found")
    sys.exit()
##### Open fortune cookies
if os.path.isfile("./fortunes.json"):
    with open("./fortunes.json") as fortunes_file:
        fortunes = json.load(fortunes_file)
else:
    print("No fortune cookies file 'fortunes.json' found")

##### load config
bot_token = config['bot_token']
bot = telegram.Bot(token=bot_token)

TEAM           = config['TEAM']
GNT            = config['GNT_ID']
GNT_PLAYGROUND = config['GNT_PLAYGROUND_ID']

PRIOR_CMD_MSG_ID = {
	GNT   : 0,
	GNT_PLAYGROUND   : 0
}

PRIOR_CMD_ID = {
	GNT   : 0,
	GNT_PLAYGROUND   : 0
}


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

def delete(chat_id):
    try:
        bot.delete_message(chat_id=chat_id,message_id=PRIOR_CMD_ID[chat_id])
    except:
        pass
    try:
        bot.delete_message(chat_id=chat_id, message_id=PRIOR_CMD_MSG_ID[chat_id])
    except:
        pass


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
    message_id = update.message.message_id
    msg = config['commands']
    if (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        if PRIOR_CMD_MSG_ID[chat_id] > 0:
            delete(chat_id)
        message = bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)
        PRIOR_CMD_MSG_ID[chat_id] = int(message.message_id)
        PRIOR_CMD_ID[chat_id] = int(message_id)
    else:
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def extras(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    msg = config['extras']
    if (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        if PRIOR_CMD_MSG_ID[chat_id] > 0:
            delete(chat_id)
        message = bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)
        PRIOR_CMD_MSG_ID[chat_id] = int(message.message_id)
        PRIOR_CMD_ID[chat_id] = int(message_id)
    else:
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def resources(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    msg = config['resources']
    message_id = update.message.message_id
    if (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        if PRIOR_CMD_MSG_ID[chat_id] > 0:
            delete(chat_id)
        message = bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)
        PRIOR_CMD_MSG_ID[chat_id] = int(message.message_id)
        PRIOR_CMD_ID[chat_id] = int(message_id)
    else:
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def videos(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    msg = config['videos']
    if (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        if PRIOR_CMD_MSG_ID[chat_id] > 0:
            delete(chat_id)
        message = bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)
        PRIOR_CMD_MSG_ID[chat_id] = int(message.message_id)
        PRIOR_CMD_ID[chat_id] = int(message_id)
    else:
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def rules(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    msg = config['rules']
    if (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        if PRIOR_CMD_MSG_ID[chat_id] > 0:
            delete(chat_id)
        message = bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)
        PRIOR_CMD_MSG_ID[chat_id] = int(message.message_id)
        PRIOR_CMD_ID[chat_id] = int(message_id)
    else:
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def adminlist(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    msg = config['adminlist']
    if (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        if PRIOR_CMD_MSG_ID[chat_id] > 0:
            delete(chat_id)
        message = bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)
        PRIOR_CMD_MSG_ID[chat_id] = int(message.message_id)
        PRIOR_CMD_ID[chat_id] = int(message_id)
    else:
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def releases(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    message_id = update.message.message_id
    msg = config['releases']
    if (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        if PRIOR_CMD_MSG_ID[chat_id] > 0:
            delete(chat_id)
        message = bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)
        PRIOR_CMD_MSG_ID[chat_id] = int(message.message_id)
        PRIOR_CMD_ID[chat_id] = int(message_id)
    else:
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)

def carlos(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
    message_id = update.message.message_id
    if (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        if PRIOR_CMD_MSG_ID[chat_id] > 0:
            delete(chat_id)
        message = bot.sendPhoto(chat_id=chat_id, photo=open("carlos.png",'rb'), caption="WHADAMAGANADO")
        PRIOR_CMD_MSG_ID[chat_id] = int(message.message_id)
        PRIOR_CMD_ID[chat_id] = int(message_id)
    else:
        bot.sendPhoto(chat_id=chat_id, photo=open("carlos.png",'rb'), caption="WHADAMAGANADO")

def rabbit(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
    message_id = update.message.message_id
    bunnylist=["/home/ubuntu/rabbitpic.jpg", "/home/ubuntu/rabbit1.jpg", "/home/ubuntu/rabbit2.jpg", "/home/ubuntu/rabbit3.jpg", "/home/ubuntu/rabbit4.jpg", "/home/ubuntu/rabbit5.jpg", "/home/ubuntu/rabbit6.jpg", "/home/ubuntu/rabbit7.jpg", "/home/ubuntu/rabbit8.jpg", "/home/ubuntu/rabbit9.jpg", "/home/ubuntu/rabbit10.jpg", "/home/ubuntu/rabbit11.jpg", "/home/ubuntu/rabbit12.jpg", "/home/ubuntu/rabbit13.jpg", "/home/ubuntu/rabbit14.jpg", "/home/ubuntu/rabbit15.jpg", "/home/ubuntu/rabbit16.jpg", "/home/ubuntu/rabbit17.jpg", "/home/ubuntu/rabbit18.jpg", "/home/ubuntu/rabbit19.jpg"]
    if (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        if PRIOR_CMD_MSG_ID[chat_id] > 0:
            delete(chat_id)
        message = bot.sendPhoto(chat_id=chat_id, photo=open(random.choice(bunnylist), "rb"))
        PRIOR_CMD_MSG_ID[chat_id] = int(message.message_id)
        PRIOR_CMD_ID[chat_id] = int(message_id)
    else:
        bot.sendPhoto(chat_id=chat_id, photo=open(random.choice(bunnylist), "rb"))


def fortune(bot, update):
    pprint(update.message.chat.__dict__, indent=4)
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
    previous_fortune_id = config['previous']['fortune']
    if (previous_fortune_id == user_id + 1) and (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        message_id = update.message.message_id
        bot.delete_message(chat_id=chat_id, message_id=message_id)
    elif (user_id == previous_fortune_id) and (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        msg = ("One who asks for many fortunes in a row, is one who should rethink their life.")
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)
        config['previous']['fortune'] = user_id + 1
    elif (user_id != previous_fortune_id) and (chat_id == GNT or chat_id == GNT_PLAYGROUND):
        msg = random.choice(fortunes)
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)
        config['previous']['fortune'] = user_id
    else:
        msg = random.choice(fortunes)
        bot.sendMessage(chat_id=chat_id,text=msg,parse_mode="Markdown",disable_web_page_preview=1)


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
    dp.add_handler(CommandHandler("fortune", fortune))

##### MessageHandlers


##### Log all errors
    dp.add_error_handler(error)

# Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
