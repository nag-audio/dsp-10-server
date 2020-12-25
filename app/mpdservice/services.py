import json

from app.mpdservice import client, on_connect_error

############### WebSocket #######################

# True - уведомить подключенных пользователях об изменениях
# False - не уведомлять
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
    return True

# Предыдущий трек
@on_connect_error
def prev_track(value):
    client.previous()
    return False

# Следующий трек
@on_connect_error
def next_track(value):
    client.next()
    return False

# Изменить громкость
@on_connect_error
def switch_volume(value):
    client.setvol(value)
    return True

# Включение повтора
@on_connect_error
def switch_repeat(value):
    client.repeat(value)
    return True

# Включение рандомного воспроизведения
@on_connect_error
def switch_shuffle(value):
    client.random(value)
    return True

############### AJAX ###################

# Текущий плейлист
@on_connect_error
def current_playlist(value):
    return client.playlistinfo()

@on_connect_error
def play_track_by_number(value):
    client.play(value)

@on_connect_error
def remove_track_by_number(value):
    client.deleteid(value)
