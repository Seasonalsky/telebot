from telegram.ext import Updater, CommandHandler
import requests
import re

contents = requests.get('https://random.dog/woof.json').json()
image_url = contents['url']

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url