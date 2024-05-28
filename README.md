# United batchery bot

## Минимальные систеные требования
1. 20 gb ssd/hdd.
2. 512mb ram
3. 1 cpu

## Зависимости
1. Docker compose

## Запуск
1. скопировать пример .env.example в .env

    ```sh
    cp .env.example .env
    ```
и заполнить этот файл `.env`


2. Поднтять бота
    ```sh
    docker compose up -d
    ```

3. Перейти в папку miniapp и запустить nginx с сертификатом для доступа к мини приложению из вне
Пример `nginx.conf`

    ```conf
    server {
        listen 80;
        root /home/user/united_batchery_bot/miniapp;

        server_name ваш_домен;

        location / {
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location / {
            index index.html
        }
    }

    ```
