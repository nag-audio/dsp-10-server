from aiohttp import web

from .player import handlers as player_handlers

# Базовый маршрутизатор запросов
routes = [
    web.get('/api/player/ws', player_handlers.ws_handler)
]