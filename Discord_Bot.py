import requests

payload  = {
    'content' : 'This is a bot'
}

header = {
    'authorization' : 'Nzc4Mjg5NjgyNTA0ODc2MDUy.YjYl_w.npHlQkcGaTQPopCCKBO314FBB6E'
}

for i in range(10):
    r = requests.post('https://discord.com/api/v9/channels/976934761056567317/messages', data=payload, headers=header)