import time
from pypresence.presence import Presence

app_id = '1249130863665479832'
time_elapsed = True

RPC = Presence(app_id)
RPC.connect()

start = None
if time_elapsed:
    start = time.time()

RPC.update(
    details='Solo',
    state='Rap FR',
    large_image='car',
    large_text='Porsche',
    small_image='nxd',
    small_text='🖖🏻',
    buttons=[
         {
            "label": 'KYOTO',
            "url": 'https://discord.gg/NwF5EkHsZQ'
        },
        {
            "label": 'SHIBUYA',
            "url": 'https://discord.gg/Shibuya'
        }
    ],
    start=start
)

print('Discord Rich Presence launched!')

while True: time.sleep(15)