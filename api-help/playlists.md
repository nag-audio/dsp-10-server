- Список файлов
Получение списка папок в папке, указанной в конфиге mpd
```
/dirs
```
JSON ответ
```json
{
	{
		directory: "Название папки",
		last-modified: "Дата последнего изменения"
	},
	...........
}
```

------------

- Текущий список воспроизведения
Показывает текущий список треков
```
/playlists/current
```
JSON ответ
```json
{
	{
	file: "Путь к файлу",
	last-modified: "Дата изменения",
	artist: "Создатель",
	title: "Название",
	album: "Альбом",
	date: "Дата создания",
	time: "Время воспроизведения",
	duration: "Чуть более точное время воспроизведения",
	pos: "Позиция в плейлисте",
	id: "ID трека"
	}
	......
}
```

------------

- Проигрывать трек из плейлиста
Указание позиции трека в плейлисте, для последующего его проигрывания
```
/playlists/current/play/{pos}
```

```
Http response 200
```

------------

- Удаление трека из плейлиста по его id
Указание позиции трека в плейлисте, для последующего его удаления
```
/playlists/current/remove/{id}
```

JSON ответ обновленного плейлиста
```json
{
	{
	file: "Путь к файлу",
	last-modified: "Дата изменения",
	artist: "Создатель",
	title: "Название",
	album: "Альбом",
	date: "Дата создания",
	time: "Время воспроизведения",
	duration: "Чуть более точное время воспроизведения",
	pos: "Позиция в плейлисте",
	id: "ID трека"
	}
	......
}
```