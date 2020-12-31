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
    elif status == 'play':
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
    if value == '0':
        # Полностью убираем повтор
        await client.repeat(0)
        await client.single(0)
    elif value == '1':
        # Повтор плейлиста
        await client.repeat(1)
        await client.single(0)
    elif value == '2':
        # Повтор текущего трека
        await client.repeat(1)
        await client.single(1)

@reconnect
async def switch_shuffle(value):
    await client.random(value)

############### Управление папками и файлами

@reconnect
async def get_directory_files(directory=None):
    if directory:
        dir_info = await client.lsinfo(directory)
    else:
        dir_info = await client.lsinfo()

    return dir_info

@reconnect
async def update_mpd_database():
    await client.update()
    return await client.lsinfo()

@reconnect
async def song_to_playlist(songuri, playlist_name):
    await client.playlistadd(playlist_name, songuri)

@reconnect
async def to_current_playlist(songuri):
    await client.add(songuri)

@reconnect
async def play_song(songid):
    pass

############### Управление плейлистами

# Текуший плейлист
@reconnect
async def get_current_playlist_info():
    return await client.playlistinfo()

@reconnect
async def play_song_in_current_playlist(songid):
    await client.playid(songid)

@reconnect
async def swap_songs_from_current_playlist(song1id, song2id):
    await client.swapid(song1id, song2id)
    return await client.playlistinfo()

@reconnect
async def remove_song_from_current_playlist(songid):
    await client.deleteid(songid)
    return await client.playlistinfo()   

@reconnect
async def save_playlist(name):
    await client.save(name) 

# Сохраненные плейлисты
@reconnect
async def list_playlists():
    return await client.listplaylists()

@reconnect
async def playlist_info(name):
    return await client.playlistinfo(name)

@reconnect
async def remove_song_from_playlist(playlist, songpos):
    await client.playlistdelete(playlist, songpos)
    return await client.playlistinfo(playlist)

@reconnect
async def swap_songs_from_playlist(playlistname, pos1, pos2):
    await client.playlistmove(playlistname, pos1, pos2)
    return await client.playlistinfo(playlist)

@reconnect
async def rename_playlist(origin_name, new_name):
    await client.rename(origin_name, new_name)

@reconnect
async def play_playlist(playlist_name):
    await client.clear()
    await client.load(playlist_name)
    await client.play()

@reconnect
async def remove_playlist(name):
    await client.rm(name)
    return await client.listplaylists()