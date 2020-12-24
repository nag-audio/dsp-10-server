import json

from app.mpdservice import client, on_connect_error

@on_connect_error
def get_start_status(value):
    data = {
        'type': 'start',
        'value':{
            'music': client.currentsong(),
            'status': client.status()
        }
    }
    return json.dumps(data)

# Переключение паузы
@on_connect_error
def switch_state(value):
    if value=="pause":
        print("переключено на паузу")
        client.pause()
    elif value=="play":
        print("переключено на старт")
        client.play()

# Предыдущий трек
@on_connect_error
def prev_track(value):
    client.previous()

# Следующий трек
@on_connect_error
def next_track(value):
    client.next()

# Изменить громкость
@on_connect_error
def switch_volume(value):
    client.setvol(value)

# Включение повтора
@on_connect_error
def switch_repeat(value):
    client.repeat(value)

# Включение рандомного воспроизведения
@on_connect_error
def switch_shuffle(value):
    client.random(value)