import telegram

# Replace YOUR_BOT_TOKEN with your actual bot token
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

# Replace YOUR_CHAT_ID with the actual chat ID where you want to send the message
chat_id = 'YOUR_CHAT_ID'

# Replace YOUR_MESSAGE with the message you want to send
message = 'YOUR_MESSAGE'

# Send the message
bot.send_message(chat_id=chat_id, text=message)
