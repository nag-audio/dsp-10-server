import pathlib
# Настройка для разработки
DEBUG = True

# Настройки файлов
BASE_DIR = pathlib.Path(__file__).parent
STATIC_DIR = BASE_DIR.parent.joinpath("static")
TEMPLATES_DIR = BASE_DIR.joinpath("templates")

# Настройки redis
REDIS_HOST, REDIS_PORT = "localhost", 5000

# Настройки mpd
MPD_HOST, MDP_PORT = "localhost", 6600
