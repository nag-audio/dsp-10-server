import logging
import json

from aiohttp import WSMsgType
from aiohttp import web

from app.mpdservice import services

# Список обработчиков команд
ws_command_handlers = {
     'state': services.switch_state,
     'next': services.next_track,
     'prev': services.prev_track,
     'volume': services.switch_volume,
     'shuffle': services.switch_shuffle,
     'repeat': services.switch_repeat
}

# Отправка нового состояния всем пользователям
async def broadcast_data(app, data):
    for client in app['websockets']:
        try:
            await client.send_str(data)
        except ConnectionResetError:
            app['websockets'].remove(client)
            logging.error("Подключение оборвалось")

# Создание и обработка подключений
async def ws_handler(request):
    current_ws = web.WebSocketResponse()
    await current_ws.prepare(request)
    request.app['websockets'].append(current_ws)
    logging.debug("new socket connection.")
    data = services.get_start_status(1)
    await current_ws.send_str(data)
    # Прослушка сообщений текущего подключения
    async for msg in current_ws:
        # Если пришло текстовое сообщение
        if msg.type == WSMsgType.TEXT:
            # Закрытие соединения
            # if msg.data == "close":
            #     request.app['websockets'].remove(current_ws)
            #     await current_ws.close()
                # Получение и преобразование в словарь
            data = json.loads(msg.data)
            print(data)
            # Выполнение команды
            if ws_command_handlers[data['type']](data['value']): 
                await broadcast_data(request.app, msg.data)
        # Если ошибка с подключением
        elif msg.type == WSMsgType.ERROR:
            logging.error(f"ws connection closed with exception: {current_ws.exception()}")
        
    logging.debug("socket connection closed")

    return current_ws
         