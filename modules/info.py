# Chat Info
'''
.chinfo:: Получение информации о чате. \n\n<b>Использование:</b> \n<code>.chinfo</code> в целевом чате
'''

from telethon import events
import asyncio

def a(client):
    @client.on(events.NewMessage(pattern=r"\.chinfo", outgoing=True))
    async def _(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        info = f'''\n<b>Информация о чате:\n\nНазвание: <code>{chat.title}</code>\nID: <code>{chat.id}</code>\nКол-во участников: <code>{chat.participants_count}</code></b>


        '''
        await event.edit(info, parse_mode='html')


if __name__ == '__main__':
    try:
        a(client)
    except:
        pass