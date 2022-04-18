# Restart
'''
.restart:: Перезапуск юзербота.
'''
from telethon import events
import asyncio
import os
import sys
import subprocess

def a(client):
	@client.on(events.NewMessage(pattern=r"\.restart", outgoing=True))
	async def _(event):
		if event.fwd_from:
			return
		await event.edit('Перезапуск...')
		await asyncio.sleep(2 / 10)
		await event.edit('Перейдите в терминал!')
		await asyncio.sleep(2 / 10)
		await event.delete()
		os.execvp(
			sys.executable,
			[
				sys.executable,
				"Telemagic.py",
			],
		)
if __name__ == '__main__':
	try:
		a(client)
	except:
		pass