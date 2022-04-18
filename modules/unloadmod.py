# Unloadmod
'''
.unloadmod:: Удаление модуля. \n<b>Использование</b>: \n<code>.unloadmod</code> названиемодуля 
'''
from telethon import events
import asyncio
import os
import sys
import subprocess
from pathlib import Path
from importlib import import_module, reload
global files_to_del
files_to_del = []

def a(client):
	def del_mod(link, event):
		for path in sorted((Path("modules")).rglob("*.py")):
			with open(path, encoding='utf-8') as file: 
				lines = file.read().splitlines()[0] 

				a = str(lines).split('#')[-1] 
				b = str(lines).split(' ')[-1]
				if link in b:
					module_path = ".".join(path.parent.parts + (path.stem,))
					files_to_del.append(path)
		for path in files_to_del:		
			print(f'Удален файл: {path}')
			os.remove(f'{path}')


	@client.on(events.NewMessage(pattern=r"\.unloadmod", outgoing=True))
	async def _(event):
		if event.fwd_from:
			return
		try:
			txt1 = event.message.message
		except:
			txt1 = event.original_update.message.message

		text = ''.join(txt1.split(' ')[-1])



		try:
			del_mod(text, event)
			deleted = ','.join(f'\n{str(i)}' for i in files_to_del)
			await event.edit(f'<b>Успешно удален модуль!\n Удалены файлы</b>: <code>{deleted}</code> \n\n<b>Напишите</b> <code>.restart<code> чтобы загрузить установленные модули!', parse_mode='html')
			await asyncio.sleep(6)
			await event.delete()

		except Exception as e:
			print(e)
			await event.edit(f'Ошибка удаления! \n<b>Подробности:</b> <code>{e}</code>', parse_mode='html')
			await asyncio.sleep(6)
			await event.delete()






if __name__ == '__main__':
	try:
		a(client)
	except:
		pass