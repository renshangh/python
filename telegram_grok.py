import telegram
from telegram.ext import Updater, CommandHandler
import logging

# Enable logging to see what's happening
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                   level=logging.INFO)

# Replace 'YOUR_BOT_TOKEN' with the token you get from BotFather
TOKEN = '7659139732:AAHc7q-k52WeT2p1RNRSnophWptEH_KI5Fc'  #'YOUR_BOT_TOKEN' 7659139732:AAHc7q-k52WeT2p1RNRSnophWptEH_KI5Fc

# Replace 'YOUR_CHAT_ID' with the chat ID you want to send messages to
CHAT_ID = '336d1586-72ea-4b2c-a916-3daaba4d8502' #'YOUR_CHAT_ID'

# Initialize the bot
bot = telegram.Bot(token=TOKEN)

def start(update, context):
    """Send a welcome message when the command /start is issued."""
    update.message.reply_text('Hello! I can send messages to this chat.')

def send_message(context):
    """Function to send a message to the specified chat."""
    context.bot.send_message(chat_id=CHAT_ID, 
                           text='This is a test message from your bot!')

def main():
    """Main function to run the bot."""
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add command handler for /start
    dp.add_handler(CommandHandler("start", start))

    # Schedule a message to be sent (e.g., immediately for testing)
    updater.job_queue.run_once(send_message, 0)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()