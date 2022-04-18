# Clocks
'''
.chasy:: Простая анимация часов
'''
from telethon import events
import asyncio

def a(client):
	@client.on(events.NewMessage(pattern=r"\.chasy", outgoing=True))
	async def _(event):
	    if event.fwd_from:
	        return
	    text = '🕐 🕑 🕒 🕓 🕔 🕕 🕖 🕗 🕘 🕙 🕚 🕛 🕜 🕝 🕞 🕟 🕠 🕡 🕢 🕣 🕤 🕥 🕦 🕧'
	    lst1 = text.split(' ')
	    lst = lst1*10
	    for message in lst:
		    await event.edit(message)
		    await asyncio.sleep(0.5)


if __name__ == '__main__':
	try:
		a(client)
	except:
		pass
