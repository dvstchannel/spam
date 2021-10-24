  # By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button



@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("**• 👉 Xem thêm nhiều group ở phía 👇**\n\n**• 👉 Nếu không vào được nhóm, vui lòng chọn cách mở chặn Pron cho điện thoại hệ điều hành iphone.👍**",
                    buttons=[
                        [
                            Button.url("✅Tổng hợp link nhóm✅",url="https://t.me/tuoidaythi")
                        ],
                        [
                            Button.url("⛔️Nội quy Bộ Tộc⛔️",url="https://t.me/noiquybotoc18")
                        ],
                        [
                            Button.url("🔞Mở Chặn Pron IOS🔞",url="https://t.me/unlock18")
                        ],
                        [
                            Button.url("🇻🇳Cài Tiếng Việt🇻🇳",url="http://t.me/setlanguage/abcxyz")
                        ]
                    ])
    
