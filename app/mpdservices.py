import mpd
from mpd.asyncio import MPDClient

import json

client = MPDClient()

# Переподключение в случае отвала cоединения 
def reconnect(func):
    async def wrapper(*args):
        try:
            return await func(*args)
        except mpd.ConnectionError:
            await client.connect("localhost", 6600)
            return await func(*args)

    return wrapper

############## Базовое управление плеером
@reconnect
async def get_status():
    return await client.status()

@reconnect
async def get_current_song():
    return await client.currentsong()

@reconnect
async def get_start_status():
    data = {
        'song': await client.currentsong(),
        'status': await client.status()
    }
    return json.dumps(data)

@reconnect
async def change_status(status):
    if status == "pause":
        await client.pause()
    elif status in ['play', 'stop']:
        await client.play()
    
@reconnect
async def prev_song(value):
    await client.previous()

@reconnect
async def next_song(value):
    await client.next()

############### Управление режимами воспроизведения

@reconnect
async def switch_volume(volume):
    await client.setvol(volume)

@reconnect
async def switch_repeat(value):
    if value == 0:
        # Полностью убираем повтор
        await client.repeat(0)
        await client.single(0)
    elif value == 1:
        # Повтор плейлиста
        await client.repeat(1)
        await client.single(0)
    elif value == 2:
        # Повтор текущего трека
        await client.repeat(1)
        await client.single(1)

@reconnect
async def switch_shuffle(value):
    await client.random(value)

############### Управление папками и файлами

############### Управление плейлистами