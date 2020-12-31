from aiohttp import web

from .player import handlers as player_handlers
from .playlistsmanager import handlers as pl_handlers
from .songsmanager import handlers as songs_manager

# Базовый маршрутизатор запросов
routes = [
    # Подключение к плееру
    web.get('/api/player/ws', player_handlers.ws_handler),
    # Урлы работы с файлами
    web.get('/api/files', songs_manager.get_files_info_handler), #Отдать список файлов и папок в директории
    web.get('/api/files/update', songs_manager.update_database_handler), #Обновить БД mpd
    web.post('/api/files/toplaylist', songs_manager.song_to_playlist_handler), #Добавить в плейлист
    web.post('api/files/toplaying', songs_manager.song_to_current_playlist_handler), #Добавить в текущий список воспроизведения
    web.post('api/files/play', songs_manager.play_song_handler), #Воспроизвести выбранный файл 
    # Урлы работы с плейлистами
    # web.get('/api/playlists/current', mm_handlers.get_current_playlist),
    # web.get('/api/playlists/current/play/{id}', mm_handlers.set_playing_track),
    # web.get('/api/playlists/current/remove/{id}', mm_handlers.rm_track)
]