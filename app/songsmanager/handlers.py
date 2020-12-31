from aiohttp import web
import json

from app import mpdservices

# Обработка запроса информации о файлах
async def get_files_info_handler(request):
    directory = request.rel_url.query.get('directory', None)
    data = await mpdservices.get_directory_files(directory)
    return web.json_response(data)

# Запрос на обновление базы данных
async def update_database_handler(request):
    data = await mpdservices.update_mpd_database()
    return web.json_response(data)

# Запрос на добавление песни в один из сохраненных плейлистов
async def song_to_playlist_handler(request):
    data = await request.json()
    await mpdservices.song_to_playlist(data['file'], data['playlist'])
    return web.Response(status=200)

# Запрос на добавление песни в список воспроизведения
async def song_to_current_playlist_handler(request):
    data = await request.json()
    await mpdservices.to_current_playlist(data['file'])
    return web.Response(status=200)

# Запрос на проигрывание выбранной песни
async def play_song_handler(request):
    pass
