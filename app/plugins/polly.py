import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to

def help_msg():
    return """
            .------.
           /  ~ ~   \,------.      ______
         ,'  ~ ~ ~  /  (@)   \   ,'      \\
       ,'          /`.    ~ ~ \ /         \\
     ,'           | ,'\  ~ ~ ~ X     \  \  \\
   ,'  ,'          V--<       (       \  \  \\
 ,'  ,'               (vv      \/\  \  \  |  |
(__,'  ,'   /         (vv   ""    \  \  | |  |
  (__,'    /   /       vv   "'"    \ |  / / /
      \__,'   /  |     vv          / / / / /
          \__/   / |  | \         / /,',','
             \__/\_^  |  \       /,'',','\\
                    `-^.__>.____/  ' ,'   \\
                            // //---'      |
          ===============(((((((=================
                                     | \ \  \\
                                     / |  |  \\
                                    / /  / \  \\
                                    `.     |   \\
                                      `--------'
======================================================
                ___       _  _
                | . \ ___ | || | _ _
                |  _// . \| || || | |
                |_|  \___/|_||_|`_. |
                                <___'

Polly scans the horizon for vessels to plunder:
    help    -- This message
    search  -- Search the horizon for a phrase
    host    -- Examine a host address
    scan    -- Scan a host address
"""

@respond_to(r'^help', re.IGNORECASE)
def help_response(message):
    message.reply("```\n"+help_msg()+"\n```")


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

@listen_to(r'\bsing\b|\bsong\b', re.IGNORECASE)
@respond_to(r'\bsing\b|\bsong\b', re.IGNORECASE)
def song(message):
    message.reply("""
        :musical_note: _And it's all for me grog, me jolly, jolly grog_
        _All for me beer and tobacc-y_
        _Well I spent all me tin on the lassies 'n gin_
        _Across the western ocean I must journey-y!_ :musical_note:
        SQUAK!
    """)

@listen_to(r'\bjoke|\blaugh', re.IGNORECASE)
@respond_to(r'\bjoke|\blaugh', re.IGNORECASE)
def joke(message):
    message.reply("I'm pining for the fjords. SQUAK!")
