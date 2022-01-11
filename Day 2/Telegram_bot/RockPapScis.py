# @RockPapScis in bot
from telegram import replymarkup
from telegram import update
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import *
from telegram.ext import *
import random

updater = Updater("5059858098:AAHic9l71DGGe3lpYaSICPcmfYScY30CQQY",
				use_context=True)

def start(update: Update, context: CallbackContext):
    
    update.message.reply_text("Enter end command to end game and view your score")
    buttons = [[KeyboardButton("Yayy")]]
    context.bot.send_message(chat_id=update.effective_chat.id,text="Hello ! Ready?",reply_markup=ReplyKeyboardMarkup(buttons))
    
def game(update: Update, context: CallbackContext):
    opt=["Rock","Paper","Scissor"]

def msg_handler(update: Update, context: CallbackContext):
    
    if "Yayy" in update.message.text:
        buttons = [[KeyboardButton("Rock")],[KeyboardButton("Paper")],[KeyboardButton("Scissors")]]
        context.bot.send_message(chat_id=update.effective_chat.id,text="You Go First !",reply_markup=ReplyKeyboardMarkup(buttons))

    opt=["Rock","Paper","Scissors"]
    choice=opt[random.randint(0,2)]
    bot_points=0
    player_points=0
    if ("Rock" in update.message.text or "Paper" in update.message.text or "Scissors" in update.message.text):
        update.message.reply_text( "I'm gonna go with"+ choice)
        if("Rock" in update.message.text):
            if(choice=="Paper"):
                bot_points+=1
                update.message.reply_text("You lost :)")
                
            else:
              if(choice=="Rock"):
                update.message.reply_text("Draw :(")
              else:
                update.message.reply_text("You won ! ")
                player_points+=1
    if("Paper" in update.message.text):
            if(choice=="Scissors"):
                update.message.reply_text("You lost :)")
                bot_points+=1
            else:
              if(choice=="Paper"):
                update.message.reply_text("Draw :(")
              else:
                update.message.reply_text("You won ! ")
                player_points+=1
    if("Scissors" in update.message.text):
            if(choice=="Rock"):
                update.message.reply_text("You lost :)")
                bot_points+=1
            else:
              if(choice=="Scissors"):
                update.message.reply_text("Draw :(")
              else:
                update.message.reply_text("You won ! ")
                player_points+=1
            
def endgame(update: Update, context: CallbackContext):
    update.message.reply_text("Thanks for playing with us")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('end', endgame))
updater.dispatcher.add_handler(MessageHandler(Filters.text, msg_handler))
updater.start_polling()

