import logging
import mpd

from app import config

client = mpd.MPDClient()
client.timeout = 30
try:
    client.connect(
        host=config.MPD_HOST,
        port=config.MDP_PORT
    )
    logging.info("MPD Server connect success.")
except mpd.ConnectionError:
    logging.error("MPD Server connection error.")

# Востанавливает соединение с mpd
def on_connect_error(command):
    def wrapper(value):
        try:
            return command(value)
        except mpd.ConnectionError:
            client.connect(
                host=config.MPD_HOST,
                port=config.MDP_PORT
            )
            return command(value)
        except mpd.base.CommandError:
            pass
    return wrapper   