from aiohttp.web import run_app

import app

run_app(app._init_app())