# United batchery bot

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
    server_name ваш_домен;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name ваш_домен;

    ssl_certificate /path/to/your/fullchain.pem;
    ssl_certificate_key /path/to/your/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    ssl_ciphers HIGH:!aNULL:!MD5;

    # Root path to the main app directory
    root /home/user/united_batchery_bot/miniapp;

    # General location block for the main root
    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        index index.html;
    }

    # Location block for Просвещения 46
    location /prosvet {
        alias /home/user/united_batchery_bot/miniapp/prosvet;
        index index.html;
    }

    # Location block for Восстания, 26
    location /vosstania {
        alias /home/user/united_batchery_bot/miniapp/vosstania;
        index index.html;
    }

    # Static files
    location /imgs {
        alias /home/user/united_batchery_bot/miniapp/imgs;
    }

    location /prosvet/images {
        alias /home/user/united_batchery_bot/miniapp/prosvet/images;
    }

    location /vosstania/imgs {
        alias /home/user/united_batchery_bot/miniapp/vosstania/imgs;
    }
}

    ```