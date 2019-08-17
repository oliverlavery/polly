import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to(r'\barr+.*', re.IGNORECASE)
@listen_to(r'\barr+.*', re.IGNORECASE)
def arr(message):
    message.reply('SQUAK!')
    # react with thumb up emoji
    message.react('+1')

@respond_to(r'\bhello', re.IGNORECASE)
def hello(message):
    message.reply('SQUAK! Hello!')

@listen_to(r'\bcracker', re.IGNORECASE)
@respond_to(r'\bcracker', re.IGNORECASE)
def cracker(message):
    message.reply('SQUAK! Polly want a cracker!')
    # react with thumb up emoji
    message.react('+1')
