from aiohttp import web

from .player import handlers as player_handlers
from .playlistsmanager import handlers as mm_handlers

# Базовый маршрутизатор запросов
routes = [
    # Подключение к плееру
    web.get('/api/player/ws', player_handlers.ws_handler),
    # Урлы работы с файлами
    #web.get('/api/files/') Отдать список файлов и папок в директории
    #web.get('api/files/update') Обновить БД mpd
    #web.get('api/files/toplaylist') Добавить в плейлист
    #web.get('api/files/toplaying') Добавить в текущий список воспроизведения
    #web.get('api/files/play') Воспроизвести выбранный файл 
    # Урлы работы с плейлистами
    web.get('/api/playlists/current', mm_handlers.get_current_playlist),
    web.get('/api/playlists/current/play/{id}', mm_handlers.set_playing_track),
    web.get('/api/playlists/current/remove/{id}', mm_handlers.rm_track)
]