import requests
import time

message  = {
    'content' : 'Hi'
}

header = {
    'authorization' : 'Nzc4Mjg5NjgyNTA0ODc2MDUy.GDR-GS.Q7NBhOiW-cqwCRfnQ2ObRlFd1yXJoQKZmJfo3w'
}

#Prints 'Hi' every second 25 times in discord
for i in range(25):
    r = requests.post('https://discord.com/api/v9/channels/981272777367625788/messages', data=message, headers=header)
    time.sleep(1)
