# Privet
'''
.pr:: Анимация слова "Привет". \n Использование: .pr
'''
from telethon import events
import asyncio


def a(client):
	@client.on(events.NewMessage(pattern=r"\.pr", outgoing=True))
	async def _(event):
		if event.fwd_from:
			return
		await event.edit("\n🌑🌑🌑🌑🌑🌑🌑🌑 \n🌑🌕🌕🌕🌕🌕🌕🌑 \n🌑🌕🌕🌕🌕🌕🌕🌑 \n🌑🌕🌕🌑🌑🌕🌕🌑 \n🌑🌕🌕🌑🌑🌕🌕🌑 \n🌑🌕🌕🌑🌑🌕🌕🌑 \n🌑🌕🌕🌑🌑🌕🌕🌑 \n🌑🌑🌑🌑🌑🌑🌑🌑")
		await asyncio.sleep(0.5)
		await event.edit("\n🌑🌑🌑🌑🌑🌑🌑🌑 \n🌑🌕🌕🌕🌕🌑🌑🌑 \n🌑🌕🌕🌑🌕🌕🌑🌑 \n🌑🌕🌕🌑🌕🌕🌑🌑 \n🌑🌕🌕🌕🌕🌑🌑🌑 \n🌑🌕🌕🌑🌑🌑🌑🌑 \n🌑🌕🌕🌑🌑🌑🌑🌑 \n🌑🌑🌑🌑🌑🌑🌑🌑")
		await asyncio.sleep(0.5)
		await event.edit("\n🌑🌑🌑🌑🌑🌑🌑🌑 \n🌑🌕🌕🌑🌑🌕🌕🌑 \n🌑🌕🌕🌑🌑🌕🌕🌑 \n🌑🌕🌕🌑🌕🌕🌕🌑 \n🌑🌕🌕🌕🌕🌕🌕🌑 \n🌑🌕🌕🌕🌑🌕🌕🌑 \n🌑🌕🌕🌑🌑🌕🌕🌑 \n🌑🌑🌑🌑🌑🌑🌑🌑")
		await asyncio.sleep(0.5)
		await event.edit("\n🌑🌑🌑🌑🌑🌑🌑🌑 \n🌑🌕🌕🌕🌕🌑🌑🌑 \n🌑🌕🌕🌑🌕🌕🌑🌑 \n🌑🌕🌕🌕🌕🌑🌑🌑 \n🌑🌕🌕🌑🌕🌕🌑🌑 \n🌑🌕🌕🌑🌕🌕🌑🌑 \n🌑🌕🌕🌕🌕🌑🌑🌑 \n🌑🌑🌑🌑🌑🌑🌑🌑")
		await asyncio.sleep(0.5)
		await event.edit("\n🌑🌑🌑🌑🌑🌑🌑🌑 \n🌑🌕🌕🌕🌕🌑🌑🌑 \n🌑🌕🌕🌑🌑🌑🌑🌑 \n🌑🌕🌕🌕🌕🌑🌑🌑 \n🌑🌕🌕🌕🌕🌑🌑🌑 \n🌑🌕🌕🌑🌑🌑🌑🌑 \n🌑🌕🌕🌕🌕🌑🌑🌑 \n🌑🌑🌑🌑🌑🌑🌑🌑")
		await asyncio.sleep(0.5)
		await event.edit("\n🌑🌑🌑🌑🌑🌑🌑🌑 \n🌑🌕🌕🌕🌕🌕🌕🌑 \n🌑🌕🌕🌕🌕🌕🌕🌑 \n🌑🌑🌑🌕🌕🌑🌑🌑 \n🌑🌑🌑🌕🌕🌑🌑🌑 \n🌑🌑🌑🌕🌕🌑🌑🌑 \n🌑🌑🌑🌕🌕🌑🌑🌑 \n🌑🌑🌑🌑🌑🌑🌑🌑")

if __name__ == '__main__':
	try:
		a(client)
	except:
		pass