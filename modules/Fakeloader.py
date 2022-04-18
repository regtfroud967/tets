# Fakeloader
'''
.fl:: Фейковая строка загрузки. \n\n<b>Использование</b>: \n<code>.fl</code>
'''
import asyncio
from telethon import events


def a(client):
	@client.on(events.NewMessage(pattern=r"\.fl", outgoing=True))
	async def _(event):
		try:
			txt1 = event.message.message
		except:
			txt1 = event.original_update.message.message
		inp = ' '.join(txt1.split(' ')[1:])
		load = [" ","▏","▎","▍","▌","▋","▊","▉"]
		bar = ""
		count = 0
		await event.edit("`[Инициализация]`")
		await asyncio.sleep(3)
		for i in range(13):
			for division in load:
				space = " " * (12 - i)
				await event.edit(f"`{bar}{division}{space}[{count}%]`")
				count += 1
				await asyncio.sleep(3 / 100)
				if count == 101:
					break
			bar += "█"
		await asyncio.sleep(2)
		done = "Загрузка завершена!"
		if inp:
			done = inp
		await event.edit(f"`{done}`")

if __name__ == '__main__':
	try:
		a(client)
	except:
		pass