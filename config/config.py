# fmt: off

import os
import json

from config.utils import get_env_var, alchemize_url


DEFAULTS = {
    "BOT_TOKEN": "MTExMDExNDMwNjQ0MTM1OTQyMg.GT7zFS.YbIiFyzDmAeYmQoflWXicKGwr8eeI6vjLPzM0M",
    "SPOTIFY_ID": "",
    "SPOTIFY_SECRET": "",

    "BOT_PREFIX": "d!",  # set to empty string to disable
    "ENABLE_SLASH_COMMANDS": False,

    "VC_TIMEOUT": 600,  # seconds
    "VC_TIMOUT_DEFAULT": True,  # default template setting for VC timeout true= yes, timeout false= no timeout

    "MAX_SONG_PRELOAD": 5,  # maximum of 25
    "MAX_HISTORY_LENGTH": 10,
    "MAX_TRACKNAME_HISTORY_LENGTH": 15,

    # if database is not one of sqlite, postgres or MySQL
    # you need to provide the url in SQL Alchemy-supported format.
    # Must be async-compatible
    # CHANGE ONLY IF YOU KNOW WHAT YOU'RE DOING
    "DATABASE_URL": os.getenv("HEROKU_DB") or "sqlite:///settings.db",
}


if os.path.isfile("config.json"):
    with open("config.json") as f:
        DEFAULTS.update(json.load(f))
elif not os.getenv("DANDELION_INSTALLING"):
    with open("config.json", "w") as f:
        json.dump(DEFAULTS, f, indent=2)


for key, default in DEFAULTS.items():
    globals()[key] = get_env_var(key, default)


MENTION_AS_PREFIX = True

ENABLE_BUTTON_PLUGIN = True

EMBED_COLOR = 0x4dd4d0  # replace after'0x' with desired hex code ex. '#ff0188' >> '0xff0188'

SUPPORTED_EXTENSIONS = (".webm", ".mp4", ".mp3", ".avi", ".wav", ".m4v", ".ogg", ".mov")


COOKIE_PATH = "/config/cookies/cookies.txt"

GLOBAL_DISABLE_AUTOJOIN_VC = False

ALLOW_VC_TIMEOUT_EDIT = True  # allow or disallow editing the vc_timeout guild setting


actual_prefix = (  # for internal use
    BOT_PREFIX
    if BOT_PREFIX
    else ("/" if ENABLE_SLASH_COMMANDS else "@bot ")
)

# set db url during install even if it's overriden by env
if os.getenv("DANDELION_INSTALLING") and not DATABASE_URL:
    DATABASE_URL = DEFAULTS["DATABASE_URL"]
DATABASE = alchemize_url(DATABASE_URL)
DATABASE_LIBRARY = DATABASE.partition("+")[2].partition(":")[0]


STARTUP_MESSAGE = "Starting Bot..."
STARTUP_COMPLETE_MESSAGE = "Startup Complete"

NO_GUILD_MESSAGE = "Error: Пожалуйста, присоединитесь к голосовому каналу или введите команду в чате"
USER_NOT_IN_VC_MESSAGE = "Error: Пожалуйста, присоединитесь к активному голосовому каналу, чтобы использовать команды и кнопки"
WRONG_CHANNEL_MESSAGE = "Error: Используй канал, который назначили для бота"
NOT_CONNECTED_MESSAGE = "Error: Бота нет ни в 1 войсе"
ALREADY_CONNECTED_MESSAGE = "Error: Уже используется!"
NOT_A_DJ = "Ты не DJ-eban"
USER_MISSING_PERMISSIONS = "У тебя нет прав на это!"
CHANNEL_NOT_FOUND_MESSAGE = "Error: Не могу найти канал!"
DEFAULT_CHANNEL_JOIN_FAILED = "Error: Could not join the default voice channel"
INVALID_INVITE_MESSAGE = "Error: Неверная ссылка для инвайта"

ADD_MESSAGE = "Этот бот только для The Fufels"  # brackets will be the link text

INFO_HISTORY_TITLE = "Песни играют:"

SONGINFO_UPLOADER = "Загружено: "
SONGINFO_DURATION = "Длительность: "
SONGINFO_SECONDS = "s"
SONGINFO_LIKES = "Likes: "
SONGINFO_DISLIKES = "Dislikes: "
SONGINFO_NOW_PLAYING = "Сейчас играет"
SONGINFO_QUEUE_ADDED = "Добавлено в очередь"
SONGINFO_SONGINFO = "О песне"
SONGINFO_ERROR = "Error: Unsupported site or age restricted content. To enable age restricted content check the documentation/wiki."
SONGINFO_PLAYLIST_QUEUED = "Плейлист :page_with_curl:"
SONGINFO_UNKNOWN_DURATION = "ХЗ"
QUEUE_EMPTY = "Очередь пуста :x:"

HELP_ADDBOT_SHORT = "Добавить бота на другой сервер"
HELP_ADDBOT_LONG = "Gives you the link for adding this bot to another server of yours."
HELP_CONNECT_SHORT = "Подключение бота к войсу"
HELP_CONNECT_LONG = "Подключение бота к войсу в котором ты"
HELP_DISCONNECT_SHORT = "Отключён от войса"
HELP_DISCONNECT_LONG = "Disconnect the bot from the voice channel and stop audio."

HELP_SETTINGS_SHORT = "Посмотреть и настроить бота"
HELP_SETTINGS_LONG = "View and set bot settings in the server. Usage: {}settings setting_name value".format(actual_prefix)

HELP_HISTORY_SHORT = "Посмотреть историю песен"
HELP_HISTORY_LONG = "Shows the " + str(MAX_TRACKNAME_HISTORY_LENGTH) + " last played songs."
HELP_PAUSE_SHORT = "Пауза"
HELP_PAUSE_LONG = "Пауза медиаплеера.Заюзай ещё раз чтобы продолжить."
HELP_VOL_SHORT = "Поменять громкость %"
HELP_VOL_LONG = "Changes the volume of the AudioPlayer. Argument specifies the % to which the volume should be set."
HELP_PREV_SHORT = "Вернуться назад на 1 песню"
HELP_PREV_LONG = "Проиграть предыдущее снова."
HELP_SKIP_SHORT = "Скипнуть песню"
HELP_SKIP_LONG = "Пропускает текущую воспроизводимую песню и переходит к следующему элементу в очереди."
HELP_SONGINFO_SHORT = "О конкретной песне"
HELP_SONGINFO_LONG = "Показывает подробную информацию о воспроизводимой в данный момент песне и размещает ссылку на нее."
HELP_STOP_SHORT = "Остановка музыки"
HELP_STOP_LONG = "Stops the AudioPlayer and clears the songqueue"
HELP_MOVE_LONG = f"{actual_prefix}move [position] [new position]"
HELP_MOVE_SHORT = "Двигает трек в очереди"
HELP_YT_SHORT = "Play a supported link or search on youtube"
HELP_YT_LONG = f"{actual_prefix}p [link/video title/keywords/playlist/soundcloud link/spotify link/bandcamp link/twitter link]"
HELP_PING_SHORT = "Pong"
HELP_PING_LONG = "Тест ответа бота"
HELP_CLEAR_SHORT = "Очистить очередь."
HELP_CLEAR_LONG = "Очистка очереди и скип."
HELP_LOOP_SHORT = "Залупить трек."
HELP_LOOP_LONG = "Лупануть песню или лист значения all/single/off."
HELP_QUEUE_SHORT = "Показ песен в очереди."
HELP_QUEUE_LONG = "Показать номер трека в очереди."
HELP_SHUFFLE_SHORT = "Зашафлить треки"
HELP_SHUFFLE_LONG = "Рандомная сортировка очереди"
HELP_RESET_SHORT = "Переподключение"
HELP_RESET_LONG = "Остановите проигрыватель, отключитесь и снова подключитесь к каналу, на котором вы находитесь"
HELP_REMOVE_SHORT = "Удалить песню"
HELP_REMOVE_LONG = "Позволяет удалить песню из очереди, введя ее позицию (по умолчанию это последняя песня).."


ABSOLUTE_PATH = ""  # do not modify
