import logging
import json

from aiohttp import WSMsgType
from aiohttp import web

from app import mpdservices

# Список обработчиков команд
ws_command_handlers = {
    'state': mpdservices.change_status,
    'next': mpdservices.next_song,
    'prev': mpdservices.prev_song,
    'volume': mpdservices.switch_volume,
    'shuffle': mpdservices.switch_shuffle,
    'repeat': mpdservices.switch_repeat
}

# Создание и обработка подключений
async def ws_handler(request):
    # Инициализация нового подключения
    current_ws = web.WebSocketResponse()
    await current_ws.prepare(request)
    request.app['websockets'].append(current_ws)
    logging.debug("new socket connection.")

    # Отправка новому подключению текущий статус 
    data = await mpdservices.get_start_status()
    await current_ws.send_str(data)
    
    # Прослушка сообщений текущего подключения
    async for msg in current_ws:
        # Если пришло текстовое сообщение
        if msg.type == WSMsgType.TEXT:
            data = json.loads(msg.data)

            if data['type'] == 'close':
                # Закрытие соединения
                request.app['websockets'].remove(current_ws)
                await current_ws.close()
            # Выполнение команды
            await ws_command_handlers.get(data['type'])(data['value'])

        # Если ошибка с подключением
        elif msg.type == WSMsgType.ERROR:
            logging.error(f"ws connection closed with exception: {current_ws.exception()}")
        
    logging.debug("socket connection closed")

    return current_ws
         