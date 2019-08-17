import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import os
import time
import shodan
import socket

shodan_client = shodan.Shodan(os.environ.get('SHODAN_TOKEN', ''))

@respond_to(r'^host\s(.*)', re.IGNORECASE)
def host(message, addr):
    message.reply('SQUAK! Searching for '+addr+'...')
    try:
        host = shodan_client.host(addr)
    except shodan.exception.APIError as e:
        print("API Error: {0}".format(e))
        message.reply("Scree! Invalid query.\n{0}".format(e))
        return

    # Print general info
    response = "IP: %s\nOrganization: %s\nOperating System: %s\n\n" % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))

    # Print all banners
    for item in host['data']:
        response += "---\nPort: %s\nBanner: %s\n" % (item['port'], item['data'])
    message.reply("```\n"+response+"\n```")

# @respond_to(r'^resolve\s(.*)', re.IGNORECASE)
# def resolve(message, item):
#     message.reply('SQUAK! Resolving '+item+'...')
#     message.reply(str(socket.gethostbyname(item)))

@respond_to(r'^search\s(.*)', re.IGNORECASE)
def search(message, item):
    message.reply('SQUAK! Searching for '+item+'...')
    try:
        results = shodan_client.search(item)
    except shodan.exception.APIError as e:
        print("API Error: {0}".format(e))
        message.reply("Scree! Invalid query.\n{0}".format(e))
        return

    count = 0
    detail = 'Results found: %s \n' % results['total']
    message.reply(detail)
    detail = ""
    for result in results['matches']:
        detail += 'IP Addr: %s\n' % result['ip_str']
        for host in result['hostnames']:
            detail += 'Host: %s\n' % host
        detail += 'OS: %s\n' % result['os']
        # detail += 'Data: %s\n' % result['data']
        message.reply("```\n"+detail+"\n```")
        detail = ""
        count = count + 1
        if count == 100:
            message.reply('Screech! I stopped after 100 results.')
            break
