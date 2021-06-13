  # By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button



@BotzHub.on(events.NewMessage(incoming=True))
async def start(event):
    await event.reply("🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍\n.\
                    \n**• LINK Mọi người có biết tin của chị bên đội malay chưa ???**\
                    \n\n**• 👉 ZALO CHAT [𝗫𝗘𝗠 𝗡𝗚𝗔𝗬](https://zalo.me/g/mjpxri305) **\
                    \n\n**• 👉 APP XEM IDOL LIVE:** http://00ff.live ",
                    buttons=[
                        [
                            Button.url("HÓNG NÈ 🌚",url="https://t.me/joinchat/nfBmvkS4FeFjYjE1"),
                            Button.url("TWITTER 🌝",url="https://twitter.com/botocsex")
                        ],
                        [
                            Button.url("Hóng Hớt TV",url="https://t.me/joinchat/HFMeDVI4K_czMjBl")
                        ]
                    ])
    
