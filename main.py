"""Base module."""

import time
import os
import datetime
import telebot
from audio_to_speech.converter import convert_to_text

BOT_VERSION = "0.0.1"

current_path = os.getcwd()

# TelegramBotAPI
bot = telebot.TeleBot(
    "BOT_TOKEN", parse_mode=None)

#Welcome
@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Standart command handler. Reaction on start command."""
    chat_id = message.chat.id
    bot.send_message(chat_id, "Hello, I can translate speech to text. For details, enter /info or select the appropriate item from the menu.")

#info
@bot.message_handler(commands=['info'])
def send_info(message):
    """Standart command handler. Reaction on info command."""
    chat_id = message.chat.id
    bot.send_message(chat_id, "Send or forward me a voice message and in response I will send you text message.\nI only accept voice messages.")
    bot.send_message(chat_id, "If you find an error or your speech is not translated into text, please send me(@YOUR_ACCOUNT) a message, thanks.")

@bot.message_handler(content_types=['text'])
def send_warning_message(message):
    """Standart message handler. Reaction on regular message to bot chat."""
    chat_id = message.chat.id
    bot.send_message(chat_id, "I don't process regular text messages")

#Convert voice to text
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    """Voice message handeler."""
    chat_id = message.chat.id
    try:
        result = ""
        user_id = message.from_user.id
        user_name = message.from_user.username
        # Current datetime for audio name
        path = os.path.join(current_path, "save_voice_message", f"{user_name}.{str(user_id)}")
        if not os.path.exists(path):
            os.makedirs(path)
        current_file = path + "/" + datetime.datetime.now().strftime("%d.%m.%Y_%H:%M:%S") + ".ogg"
        # Save file to .ogg format
        file_id = message.voice.file_id
        file_info = bot.get_file(file_id)
        with open(current_file, "wb") as new_file:
            new_file.write(bot.download_file(file_info.file_path))
            while not os.path.isfile(current_file):
                time.sleep(1)
        if os.path.exists(current_file):
            result = convert_to_text(current_file)
        # If not error, return result
        if result:
            bot.send_message(chat_id, result)
        else:
            bot.send_message(chat_id, "Unfortunately, I cannot recognize the message.")
    except Exception as e:
        bot.send_message(chat_id, "Undefined error. Sorry try again. If the error persists, contact me(@YOUR_ACCOUNT)")
        log_file = os.path.join(current_path, "log.txt")
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(datetime.datetime.now().strftime("%d.%m.%Y_%H:%M:%S") + f" User: {user_name}.{user_id} {e}\n")

def main():
    """Main function with bot polling."""
    try:
        print("Bot started")
        bot.polling()
    except Exception as e:
        print("Something went wrong")
        print("Restart bot")
        print(e)
        main()        
if __name__ == "__main__":
    main()
