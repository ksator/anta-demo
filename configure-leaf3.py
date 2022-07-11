"""
This scripts configure the leaf3 device
"""

import ssl
from jsonrpclib import Server

ssl._create_default_https_context = ssl._create_unverified_context
USERNAME = "arista"
# use the password of your ATD instance
PASSWORD = "aristad4dc"
IP = "192.168.0.14"

print ('Configuring leaf3')
URL = "https://" + USERNAME + ":" + PASSWORD + "@" + IP + "/command-api"
switch = Server(URL)

with open('leaf3.conf','r', encoding='utf8') as f:
    conf_list = f.read().splitlines()

conf = switch.runCmds(version=1,cmds=conf_list, autoComplete=True)
print ('Done')
