# Press F
'''
.f:: Press f to respect \n\n<b>Использование</b>: \n<code>.f</code>
'''
import asyncio
from telethon import events


def a(client):
	@client.on(events.NewMessage(pattern=r"\.f", outgoing=True))
	async def payf(event):
		try:
			txt1 = event.message.message
		except:
			txt1 = event.original_update.message.message
		paytext=''.join(txt1.split(' ')[1:])
		if not paytext:
			paytext='0'
		pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(paytext*8, paytext*8, paytext*2, paytext*2, paytext*2, paytext*6, paytext*6, paytext*2, paytext*2, paytext*2, paytext*2, paytext*2)
		await event.edit(pay)


if __name__ == '__main__':
	try:
		a(client)
	except:
		pass