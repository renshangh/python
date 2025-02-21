import requests

def send_telegram_message(api_token, chat_id, message):
    """
    Send a message to a Telegram chat using the Bot API.

    Args:
        api_token (str): The API token obtained from BotFather.
        chat_id (int): The ID of the chat where the message will be sent.
        message (str): The message to be sent.
    """
    url = f"https://api.telegram.org/bot{api_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    return response.json()
# https://api.telegram.org/bot7659139732:AAHc7q-k52WeT2p1RNRSnophWptEH_KI5Fc/getUpdates
# Example usage
api_token = "7659139732:AAHc7q-k52WeT2p1RNRSnophWptEH_KI5Fc"  #"YOUR_API_TOKEN_HERE"
chat_id = "-1002319021247"  #"YOUR_CHAT_ID_HERE"
# chat_id = "5507785599"  #"telebot"
# add date and time to the message
import datetime 
now = datetime.datetime.now()
message = "Hello from Linkgear! "+str(now)  # "Hello from Linkgear!"

response = send_telegram_message(api_token, chat_id, message)
print(response)