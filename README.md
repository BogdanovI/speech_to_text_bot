# Telegram bot to convert voice messages to text.

Forward/record voice message to bot chat -> bot sends transcription as a text message.

## Installation

### Manually
Install all necessary modules:
```bash
sudo apt-get update &&
sudo apt-get install -y \
    ffmpeg \
    python3 \
    python3-pip \
    git
```
Install python dependencies:
```bash
sudo python3 -m pip install \
    pydub \
    pyTelegramBotAPI \
    git+https://github.com/openai/whisper.git
```
Clone repository:
```bash
git clone git@github.com:BogdanovI/speech_to_text_bot.git
```
Replace BOT_TOKEN in main.py:
```python
# TelegramBotAPI
bot = telebot.TeleBot("BOT_TOKEN", parse_mode=None)
```
Replace YOUR_ACCOUNT in main.py:
```python
bot.send_message(chat_id, "Undefined error. Sorry try again. If the error persists, contact me(@YOUR_ACCOUNT)")
```
## Usage
```bash
python3 main.py
```

## Docker
In the repository provide Docker file with all dependencies

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
