import telebot
import conf
from collections import Counter
import flask
import re

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Здравствуйте! Это бот, который напишет Вам самые частотные буквы в сообщении.')

@bot.message_handler(func=lambda m: True)
def send_sym(message):
    clean_message = re.sub('[^А-Яа-яA-Za-z]', '', message.text)
    reply0 = Counter(str(clean_message)).most_common(3)
    reply = str(reply0)
    bot.send_message(message.chat.id, reply)

@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'

@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

