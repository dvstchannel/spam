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
                            Button.url("FACEBOOK 🌚",url="https://www.facebook.com/groups/2754080448238156/?multi_permalinks=2789031428076391&notif_id=1623451636366372&notif_t=feedback_reaction_generic&ref=notif"),
                            Button.url("TWITTER 🌝",url="https://twitter.com/botocsex")
                        ],
                        [
                            Button.url("APP LIVE FREE LUÔN",url="https://t.me/joinchat/HFMeDVI4K_czMjBl")
                        ]
                    ])
    
