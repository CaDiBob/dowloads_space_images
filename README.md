# Космический Телеграм

Публикует красивые фото из космоса в телеграм канал.

### Как использовать

Скрипты используют API двух сайтов.

`fetch_spacex.py` Использует публичный [API spacex](https://github.com/r-spacex/SpaceX-API#readme)
Запуск:
```bash
$ python3 fetch_spacex.py
```
`fetch_nasa.py` Использует приватный ключ к [API NASA](https://api.nasa.gov/)
Запуск:
```bash
$ python3 fetch_nasa.py
```
Пример файла `.env`:
```
API_NASA = 'api_nasa'
TG_API = 'tg_token'
TG_CHAT_ID = '@chat_id'
```

Скрипт `send_to_telegram.py` для отправки картинок в телеграм канал.
Для работы скрипта нужно создать телеграм бота через `@BotFather`, [инструкция](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html).
После **[создаем телеграм канал назначаем бота его Администратором](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/) для того чтоб он мог публиковать фото на канале.**
Запуск:
```bash
$ python3 send_to_telegram.py
```
### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).