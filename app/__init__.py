# Code by Ebuiiiek-Bopobuiiiek umaruch@starpony.com
from aiohttp import web
import logging

from .loghandler import FileHandler
from .routes import routes

# Отключение текущих пользователей
async def close_connections(app):
    for ws in app['websockets']:
        await ws.close(code=1001, message="Server shutdown")

# Инициализация приложения
def _init_app():
    # Инициализация логгера
    logging.basicConfig(
        format="%(asctime)s %(levelname)s - %(message)s",
        handlers=[
            FileHandler("server.log", maxBytes=1024*1024)
        ],
        level=logging.DEBUG
    )

    app = web.Application(logger=logging.getLogger())
    app.add_routes(routes)
    app['websockets'] = []
    app.on_shutdown.append(close_connections)

    logging.debug("App init success.")

    return app
