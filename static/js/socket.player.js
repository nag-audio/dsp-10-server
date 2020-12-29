let ws;

window.onload = function(){
    // Корректное отключение ws подключения при переходе на новую страницу
    ws = new WebSocket("ws://"+window.location.host+"/api/player/ws");

    // Получение сообщения от сервера
    ws.onmessage = function(event){
        let data = JSON.parse(event.data); // Парсинг полученных данных
        console.log(data);
        switch (data.type) {
            case "state":
                // Поставить/убрать паузу
                update_playing_state(data.value);
                break;
            case "volume":
                // Поменять громкость
                update_volume(data.value);
                break;
            case "shuffle":
                // Переключить рандом
                update_shuffle_status(data.value);
                break;
            case "repeat":
                // Переключить повтор
                update_repeat_status(data.value);
                break;
            case "songtime":
                console.log(data);
                break;
        //     case "update_music":
        //         break
            case "start":
                start_player(data.value);
                break;
            default:
                console.error("Unknown command:"+data.type);
        };
    };
}
//  ********* Базовые штуки
// Отправка сообщения
function send_message(data){
    ws.send(data);
}
// ********** Управление плеером
// Переключение на предыдущий трек
function prev_track(){
    let data = JSON.stringify({
        type: "prev",
        value: "1"
    });
    send_message(data);
}
// Переключение на следующий трек
function next_track(){
    let data = JSON.stringify({
        type: "next",
        value: "1"
    });
    send_message(data);
}
// Переключение статуса воспроизведения
function switch_play_state(value){
    let data = JSON.stringify({
        type: "state",
        value: value
    });
    send_message(data);
}
// ********** Настройки воспроизведения
// Отправка сообщения об изменении громкости
function switch_volume(value){
    let data = JSON.stringify({
        type: "volume",
        value: value
    });
    send_message(data);
}
// Переключение повтора
function switch_repeat(value){
    let data = JSON.stringify({
        type: "repeat",
        value: value
    });
    send_message(data);
}
// Переключение рандомного воспроизведения
function switch_shuffle(value){
    let data = JSON.stringify({
        type: "shuffle",
        value: value
    });
    send_message(data);
}

function send_json(){
    var pl_request = new XMLHttpRequest();
    pl_request.onreadystatechange = function(){
        if(pl_request.readyState == 4 && pl_request.status == 200){
            console.log(JSON.parse(pl_request.responseText));
        }
    };
    pl_request.open('GET', "http://"+window.location.host+"/api/playlists/current", true);
    pl_request.send();
}
