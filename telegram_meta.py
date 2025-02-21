from warnings import filters
from telegram.ext import Updater, CommandHandler, MessageHandler

# Replace with your bot token
TOKEN = '7659139732:AAHc7q-k52WeT2p1RNRSnophWptEH_KI5Fc' #'YOUR_BOT_TOKEN'

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! This is a Telegram bot.')

def echo(update, context):
    """Echo the user's message."""
    update.message.reply_text(update.message.text)

def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # On different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # On non command i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(filters.text, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()