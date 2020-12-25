from aiohttp import web

from .player import handlers as player_handlers
from .musicmanager import handlers as mm_handlers

# Базовый маршрутизатор запросов
routes = [
    web.get('/api/player/ws', player_handlers.ws_handler),
    web.get('/api/playlists/current', mm_handlers.get_current_playlist),
    web.get('/api/playlists/current/play/{id}', mm_handlers.set_playing_track),
    web.get('/api/playlists/current/remove/{id}', mm_handlers.rm_track)
]