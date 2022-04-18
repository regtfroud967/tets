# Eval
'''
.eval:: Выполнение python кода. \n\n<b>Использование:</b> \n<code>.eval</code> вашкод
'''

from telethon import events
import asyncio
from io import StringIO
import sys

def a(client):
	@client.on(events.NewMessage(pattern=r"\.eval (.*)", outgoing=True))
	async def _(event):
		if event.fwd_from:
			return
		try:
			txt1 = event.message.message
		except:
			txt1 = event.original_update.message.message
		code = ' '.join(txt1.split(' ')[1:])
		result = sys.stdout = StringIO()
		try:
			exec(code)

			await event.edit(f'<b>Code:</b>\n<code>{code}</code>\n\n<b>Result</b>:\n<code>{result.getvalue()}</code>', parse_mode='html')
		except:
			await event.edit(f'<b>Code:</b>\n<code>{code}</code>\n\n<b>Result</b>:\n<code>{sys.exc_info()[0].__name__}: {sys.exc_info()[1]}</code>', parse_mode='html')


if __name__ == '__main__':
	try:
		a(client)
	except:
		pass