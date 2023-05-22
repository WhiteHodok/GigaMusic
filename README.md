![botlogo](https://github.com/WhiteHodok/GigaMusic/assets/39564937/43877767-8f35-4c8b-bc3d-753ebc6bdd6f)





# GigaMusic
Музыкальный бот для Discord, написанный на Python с поддержкой Youtube, SoundCloud, Spotify, Bandcamp, Twitter и пользовательских файлов.

### Имейте в виду:
* В Вики может быть ответ, который вы ищете https://github.com/Krutyi-4el/DandelionMusic/wiki.
* Известные проблемы перечислены в Issues. Если вы заинтересованы в этом проекте, не стесняйтесь подать заявку.


#### API-ключи
* Discord - https://discord.com/developers
* Spotify (опционально) - https://developer.spotify.com/dashboard/
  - Идентификатор клиента
  - Секрет клиента
  - Примечание: Ограничение на 50 элементов плейлиста без API

Полученные ключи должны быть введены в ```config.json``` (or set as environment variables)

#### Requirements (skip this if you've decided to use pre-built exe)

* Installation of Python 3.8+

Install dependencies:
```
pip install -r requirements.txt
```

##### Windows
Скачайте `ffmpeg` и поместите его в папку в PATH.

Если ffmpeg не найден, скрипт попытается загрузить его автоматически.
##### Другие платформы
Установите пакеты `ffmpeg` и `libopus`.

### Установка - Самостоятельный хостинг

1. Загрузите релиз, если он доступен, в качестве альтернативы загрузите zip-архив репозитория.
2. Выполните предварительные условия
3. Запустите ``run.py`` в корне проекта (или exe)
4. Посмотреть параметры конфигурации в config.json (больше информации на https://github.com/Krutyi-4el/DandelionMusic/wiki/Configuration).

Плагин для воспроизведения кнопок:
* Установите эмодзи с помощью команды настройки, чтобы включить эту функцию.
* Эмодзи должны быть доступны для бота
* Требуются разрешения на управление сообщениями

Пользовательские Cookies:
* Извлеките файл cookies.txt из браузера, используя предпочтительный метод.
* Перепишите существующий файл cookies.txt в /config/cookies/
* (Необязательно) Установите пользовательское местоположение cookies.txt, изменив COOKIE_PATH в config.py


## Команды:

### Музыка

После того, как бот присоединился к вашему серверу, используйте ``d!help`` для отображения справки и информации о командах.


```
d!p [link/video title/key words/playlist-link/soundcloud link/spotify link/bandcamp link/twitter link]
```

* Воспроизводит аудио поддерживаемого веб-сайта
    - Ссылка на видео (https://ww...)
    - Название видео, например (Gennifer Flowers - Fever Dolls).
    - Ссылка на плейлист YouTube.
* Если песня играет, она будет добавлена в очередь.

#### Команды плейлиста

```
d!skip / d!s
```

* Пропускает текущую песню и воспроизводит следующую в очереди.

```
d!q
```

* Показать список песен в очереди

```
d!shuffle / d!sh
```

* Перемешать очередь

```
d!l / d!loop [all/single/off]
```

* По умолчанию зацикливает всю очередь. ``d!loop single`` зацикливает текущий трек.

```
d!mv / d!move
```

* Перемещение позиции композиции в очереди.

#### Аудиокоманды

```
d!pause
```

* Приостанавливает текущую песню.

```
d!resume
```

* Возобновляет приостановленную песню.

```
d!prev
```

* Возврат на одну песню назад и повторное воспроизведение последней песни.

```
d!np
```

* Показывает более подробную информацию о текущей песне.

```
d!volume / d!vol
```

* Регулировка громкости 1-100%.
* Передать без аргументов для текущей громкости

```
d!remove / d!rm
```

* Удаляет песню из очереди (по умолчанию последняя песня)

```
d!stop / d!st
```
* Останавливает текущую песню и очищает очередь воспроизведения.


### General

```
d!settings / d!setting / d!set
```
* Без аргументов: Перечисляет настройки сервера
* Аргументы: (настройка) (значение)
* Опустите значение, чтобы сбросить настройку.
* Пример: d!setting start_voice_channel ChannelName
* Только для администраторов и диджеев

```
d!c
```

* Подключает бота к голосовому каналу пользователя.

```
d!dc
```

* Отключает бота от текущего голосового канала

```
d!history
```
* Показывает названия X последних проигранных песен. Настраивается в config.json


### Утилита

```
d!reset / d!rs
```

* Отключение и повторное подключение к голосовому каналу

```
d!ping
```

* Проверить связь с ботом

```
d!addbot
```

* Отображает информацию о том, как добавить бота на другой ваш сервер.




## Благодарности

1.https://github.com/adriansteffan/DiscordJockey


2.https://github.com/Krutyi-4el/DandelionMusic
