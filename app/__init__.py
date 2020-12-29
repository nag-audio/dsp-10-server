# Code by Ebuiiiek-Bopobuiiiek umaruch@starpony.com
from aiohttp import web
import logging
import asyncio
import json

from .loghandler import FileHandler
from .routes import routes
from app import mpdservices

# Отключение текущих пользователей в случае выключения сервера
async def close_connections(app):
    for ws in app['websockets']:
        await ws.close(code=1001, message="Server shutdown")

# Передача статуса проигрывателя текущим пользователям
async def listen_mpd_progress_song(app):
    try:
        song_id = 0
        while True:
            status = await mpdservices.get_status()
            song = None
            if song_id != status.get('songid', None):
                song = await mpdservices.get_current_song()
                song_id = status.get('songid', None)
            data = json.dumps({
                'status': status,
                'song': song
            })
            for ws in app['websockets']:
                await ws.send_str(data)
            await asyncio.sleep(5)
 
    except asyncio.CancelledError:
        pass

async def start_background_tasks(app):
    app['mpd_listener'] = asyncio.create_task(listen_mpd_progress_song(app))

async def cleanup_background_tasks(app):
    app['mpd_listener'].cancel()
    await app['mpd_listener']

# Инициализация приложения
def _init_app():
    # Инициализация логгера
    logging.basicConfig(
        format="%(asctime)s %(levelname)s - %(message)s",
        handlers=[
            FileHandler("server.log", maxBytes=1024*8000)
        ],
        level=logging.DEBUG
    )

    app = web.Application(logger=logging.getLogger())
    app.add_routes(routes)
    app['websockets'] = []

    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)
    app.on_shutdown.append(close_connections)

    logging.debug("App init success.")

    return app
