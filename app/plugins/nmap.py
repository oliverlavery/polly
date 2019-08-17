import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import nmap

def string_results(nm):
    text = ""
    for host in nm.all_hosts():
        text += "Host: {} | ".format(nm[host]['addresses']['ipv4'])
        for proto in nm[host].all_protocols():
            text += "{} ".format(proto)
            lport = sorted(nm[host][proto].keys())
            open_ports = []

            for port in lport:
                if nm[host][proto][port]['state'] == 'open':
                    open_ports.append(port)

            if len(open_ports) == 0:
                text += "No open ports. | "
            else:
                text += "{} | ".format(str(open_ports))
        if 'osmatch' in nm[host]:
            text += "OS best guess ({}% confidence): {} | ".format(
                nm[host]['osmatch'][0]['accuracy'],
                nm[host]['osmatch'][0]['name'])
    return text

@respond_to(r'^scan\s(.*)', re.IGNORECASE)
def nmap_scan(message, addr):
    message.reply('SQUAK! Scanning host '+addr+'...')
    nm = nmap.PortScanner()
    try:
        nm.scan(addr, arguments='-PS80 -F -O')
    except nmap.nmap.PortScannerError as e:
        print("NMAP Error: {0}".format(e))
        message.reply("Scree!\n{0}".format(e))
        return

    message.reply("```\n"+string_results(nm)+"\n```")
