  # By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button



@BotzHub.on(events.NewMessage(incoming=True))
async def start(event):
    await event.reply("🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍♀️🧚‍\n.\
                    \n**• Tuyễn Phi Công Bằng 17cm ???**\
                    \n\n**• 👉 ZALO CHAT [𝗫𝗘𝗠 𝗡𝗚𝗔𝗬](https://zalo.me/g/hamlsi428) **\
                    \n\n**• 👉 APP TỔNG HỢP MB:** QQL849.com ",
                    buttons=[
                        [
                            Button.url("MBBG-SG 🌚",url="https://t.me/joinchat/nfBmvkS4FeFjYjE1"),
                            Button.url("MBBG-HN 🌝",url="https://t.me/joinchat/HarJMbkqSFQ4ODg9")
                        ],
                        [
                            Button.url("ĐỪNG CÓ TÒ MÒ OKE!!!",url="https://t.me/joinchat/HFMeDVI4K_czMjBl")
                        ]
                    ])
    
