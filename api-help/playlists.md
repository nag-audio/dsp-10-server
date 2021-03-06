- Список плейлистов
Получение списка сохраненных плейлистов. 
```
GET /playlists
```
JSON ответ (статус 200)
```json
{
	{
		playlist: "Название плейлиста (пр. "Синдзи, полезай в Еву")",
		last-modified: "Дата последнего изменения (пр. "2021-01-07T18:54:02Z")"
	},
	...........
}
```
При внутренней ошибке возвращает 500 с описанием ошибки в JSON
```json
{
	error: "Текст ошибки"
}
```

------------

- Список песен в плейлисте
Показывает список треков в указанном плейлиста
```
GET /playlists/?playlistname=(Название плейлиста или current для текущего списка воспроизведения )
```
JSON ответ
```json
{
	{
	file: "Путь к файлу (пр. "dir/file.mp3")",
	last-modified: "Дата изменения (пр. "2021-01-07T18:54:02Z")",
	artist: "Str",
	title: "Str",
	album: "Str",
	date: "Дата создания (пр. "2021")",
	time: "Время воспроизведения (пр. "347")",
	duration: "Чуть более точное время воспроизведения (пр. "346.78")",
	pos: "Позиция в плейлисте (пр. "3")",
	id: "ID трека (пр. "6")"
	}
	......
}
```
Ошибки: 400 при некорректном запросе, 404 если плейлист не найден, 500 при иных ошибках 
```json
{
	error: "Текст ошибки"
}
```

------------

- Переключить на трек в текущем плейлисте или сменить плейлист
Указание позиции трека в плейлисте, для последующего его проигрывания
```
GET /playlists/play?songpos=(int, позиция трека в списке воспроизведения) or ?playlistname=(str, Название плейлиста)
```
В случае успеха возвращает код 204 с пустым телом, в случае некорректного запроса 400, 404 если трек не найден и 500 при иных ошибках
```json
{
	error: "Текст ошибки"
}
```
------------

- Удаление плейлиста или трека из выбранного плейлиста
Указание позиции трека в плейлисте, для последующего его удаления
```
DELETE /playlists?playlistname=(str, Название плейлиста)&songpos=(int, позиция трека в списке воспроизведения)
```
В случае успеха возвращает пустой ответ с кодом 204, в случае некорректного запроса 400, 404 если трек не найден и 500 при иных ошибках

------------

- Сохранить текущий список воспроизведения

```
POST /playlists/save
```
Запрос
```json
{
	playlistname: "str, Название плейлиста"
}
```
В случае успеха пустой ответ с кодом 204, при ошибках вовзращает 500 с описанием ошибки в JSON
```json
{
	error: "Текст ошибки"
}
```

------------

- Переименовать плейлист
```
POST /playlists/rename
```
Запрос
```json
{
	currentname: (str, Текущее название плейлиста),
	newname: (str, Новое название плейлиста)
}
```
В случае успеха пустой ответ с кодом 204, при ошибках вовзращает 500 с описанием ошибки в JSON
```json
{
	error: "Текст ошибки"
}
```

------------

- Переместить трек на другую позицию в плейлисте
```
POST /playlists/swap
```
Запрос
```json
{
	playlistname: (str, Название плейлиста),
	currentpos: (str, Текущая позиция трека),
	newpos: (str, Новая позиция трека)
}
```
В случае успеха пустой ответ с кодом 204, при ошибках вовзращает 500 с описанием ошибки в JSON
```json
{
	error: "Текст ошибки"
}
```
