# Loadmod
'''
.dlmod:: Установщик модулей. \n<b>Использование</b>: \n<code>.dlmod</code> ссылка на raw текст модуля из интернета 
'''
from telethon import events
import asyncio
import requests

def a(client):
	def save_mod(link, event):
		filename = link.split('/')[-1]
		r = requests.get(link, allow_redirects=True)
		if str(link).endswith('.py'):
			open(f'modules/{filename}', 'wb').write(r.content)
		else:
			open(f'modules/{filename}.py', 'wb').write(r.content)

	@client.on(events.NewMessage(pattern=r"\.dlmod", outgoing=True))
	async def _(event):
		if event.fwd_from:
			return
		try:
			txt1 = event.message.message
		except:
			txt1 = event.original_update.message.message
		text = ''.join(txt1.split(' ')[-1])
		try:
			save_mod(text, event)
			await event.edit(f'<b>Успешно установлен модуль!</b>\nНапишите <code>.restart<code> чтобы загрузить установленные модули!', parse_mode='html')
			await asyncio.sleep(4)
			await event.delete()

		except Exception as e:
			print(e)
			await event.edit(f'Ошибка установки! \n<b>Подробности:</b> <code>{e}</code>', parse_mode='html')
			await asyncio.sleep(4)
			await event.delete()




if __name__ == '__main__':
	try:
		a(client)
	except:
		pass
