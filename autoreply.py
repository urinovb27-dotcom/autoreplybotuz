from telethon import TelegramClient, events
import asyncio

api_id = 30147500
api_hash = "f0e4032301c5eb6988dd67ddf47f9ade"

client = TelegramClient("session", api_id, api_hash)

count = 0

# 👥 GROUP TEXT
group_text = """#телеграм43275 #йок43275 #боп43275 #кетгунча43275 #оналарин43275 #скб43275 #чртаман43275 #транс43275 #боллари43275 #бахке43275 😂"""

# 💬 LICHKA TEXT
private_text = """#ОНЕНи #Хали #УзоК #сКаМаН #СаБрЛи #БоЛ #СоКоВЧа 😻 😂"""

@client.on(events.NewMessage)
async def handler(event):
    global count

    try:
        # 👥 GROUP
        if event.is_group:
            count += 1
            await asyncio.sleep(60)
            await client.send_message(event.chat_id, group_text)

        # 💬 LICHKA
        else:
            await asyncio.sleep(180)
            await event.respond(private_text)

    except Exception as e:
        print("Xato:", e)

client.start()
print("Bot ishlayapti...")
client.run_until_disconnected()