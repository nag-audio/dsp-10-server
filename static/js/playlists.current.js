window.onload = function(){
    load_playlist_info();
}

// Запрос данных о текущем плейлисте
function render_playlist_data(data){
    console.log(data);
    let pl_list = document.querySelector(".playlist__list");
    data.forEach(function(track){
    let song_data = `<div class="playlist__item"><div class="playlist__image" onclick="play_track_from_playlist(${track.pos})" style="background-image: url('/static/img/noimage_thumb.png')"><svg width="15" height="17" viewBox="0 0 15 17" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g fill="white">
            <path d="M14.0874 8.21503L14.0907 8.20939L1.18366 0.595776L1.18035 0.601419C1.09396 0.545985 0.994548 0.515378 0.892569 0.512817C0.737379 0.512967 0.588597 0.576057 0.478913 0.688227C0.369229 0.800396 0.307617 0.952467 0.307617 1.11102C0.307617 1.13529 0.318113 1.15561 0.320875 1.17875H0.307617V16.4054H0.320875C0.355121 16.7023 0.593189 16.9359 0.892569 16.9359C0.999727 16.9359 1.09418 16.8986 1.18035 16.8473L1.18919 16.8625L14.0962 9.24948L14.0874 9.23424C14.2619 9.13097 14.3845 8.94586 14.3845 8.72464C14.3845 8.50341 14.2619 8.31887 14.0874 8.21503Z"/>
            </g>
            </svg>
            </div>
            <div class="playlist__info">
              <div class="playlist__info_item"><span class="playlist__song">${track.title}</span><span class="playlist__artist">${track.artist}</span></div>
              <div class="playlist__info_item"><span class="playlist__album">${track.album}</span><span class="playlist__time">5:45</span></div>
            </div>
            <div class="playlist__icon" onclick="remove_track_from_playlist(${track.id})"><svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg"><g fill="currentColor"><path d="M9 0C4.02991 0 0 4.02991 0 9C0 13.9701 4.02991 18 9 18C13.9701 18 18 13.9701 18 9C18 4.02991 13.9701 0 9 0ZM12.8571 9.48214C12.8571 9.57054 12.7848 9.64286 12.6964 9.64286H5.30357C5.21518 9.64286 5.14286 9.57054 5.14286 9.48214V8.51786C5.14286 8.42946 5.21518 8.35714 5.30357 8.35714H12.6964C12.7848 8.35714 12.8571 8.42946 12.8571 8.51786V9.48214Z"/></g></svg></div>
          </div>`;
    pl_list.innerHTML += song_data;
    });
}

// Шаблон AJAX запроса для обновления плейлиста
var pl_request = new XMLHttpRequest();
pl_request.onreadystatechange = function(){
    if(pl_request.readyState == 4 && pl_request.status == 200){
        render_playlist_data(JSON.parse(pl_request.responseText));
    }
}

// Шаблон AJAX запроса для проигрывания трека из плейлиста
var play_request = new XMLHttpRequest();
play_request.onreadystatechange = function(){
    if(play_request.readyState == 4 && play_request.status == 200){
        return 0;
    }
}

// Шаблон AJAX запроса для удаления трека из плейлиста 
var rm_request = new XMLHttpRequest();
rm_request.onreadystatechange = function(){
    console.log(rm_request);
    if(rm_request.readyState == 4 && rm_request.status == 200){
        location.reload();
    }
}

// Обновление данных о текущем плейлисте
function load_playlist_info(){
    pl_request.open('GET', "http://"+window.location.host+"/api/playlists/current", true);
    pl_request.send();
}

// Проигрывание трека из текущего плейлиста
function play_track_from_playlist(track_id){
    play_request.open('GET', "http://"+window.location.host+"/api/playlists/current/play/"+track_id, true);
    play_request.send();     
}

// Удаление трека из текушего плейлиста
function remove_track_from_playlist(track_id){
    rm_request.open('GET', "http://"+window.location.host+"/api/playlists/current/remove/"+track_id, true);
    rm_request.send();  
}