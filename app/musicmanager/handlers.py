from aiohttp import web

from app.mpdservice import services

# Текущий список воспроизведения
def get_current_playlist(request):
    return web.json_response(services.current_playlist(1))

def set_playing_track(request):
    track_id = int(request.match_info['id'])
    services.play_track_by_number(track_id)
    return web.Response(status=200)

def rm_track(request):
    track_id = int(request.match_info['id'])
    print(f"Юзер потребовал удалить песню с id {track_id}")
    services.remove_track_by_number(track_id)
    return web.json_response(services.current_playlist(1))