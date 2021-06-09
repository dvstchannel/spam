  # By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button



@BotzHub.on(events.NewMessage(incoming=True))
async def start(event):
    await event.reply("🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍\n.\
                    \n**• LINK MỚI ANH EM ƠI!!! CHỊ ÁO ĐỎ, CÓ HÌNH CON THỎ**\
                    \n\n**• 👉 Nhóm Live ZALO FREE [𝗫𝗘𝗠 𝗡𝗚𝗔𝗬](https://zalo.me/g/mjpxri305) **\
                    \n\n**• 👉 APP XEM IDOL LIVE:** http://00ff.live ",
                    buttons=[
                        [
                            Button.url("LINK🌚",url="https://t.me/joinchat/lUJ5klLg_s04NWJl"),
                            Button.url("FULL🌝",url="https://t.me/joinchat/BTUop80zaKA5MjA1")
                        ],
                        [
                            Button.url("APP LIVE FREE LUÔN",url="https://t.me/joinchat/HFMeDVI4K_czMjBl")
                        ]
                    ])
    
