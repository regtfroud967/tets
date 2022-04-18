# Spam
'''
.spam:: Спам в чате. \n\n<b>Использование:</b> \n<code>.spam</code> кол-во спам текст
'''


import asyncio
from telethon import events


def a(client):
	@client.on(events.NewMessage(pattern=r"\.spam", outgoing=True))
	async def _(event):
		try:
			try:
				txt1 = event.message.message
			except:
				txt1 = event.original_update.message.message

			counter = int(txt1.split(' ')[1])
			spam_message = ' '.join(txt1.split(' ')[2:])
			await event.delete()
			await asyncio.wait([event.respond(spam_message) for i in range(counter)])
		except Exception as e:
			print(e)


	

if __name__ == '__main__':
    try:
        a(client)
    except:
        pass