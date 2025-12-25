## Переменные окружения

Приложение использует `.env` или ConfigMap для настройки.
Переменные окружения, которые использовал я:
```
TYPE=IPAPI
# TYPE=JSONIP
PORT=8000
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5441
```


## Запуск через Docker Compose


Создайте `.env` с необходимыми переменными на основе.

Чтобы запустить приложение:
```bash
docker-compose up -d
```

Чтобы остановить приложение:
```bash
docker-compose down
```

---

## Запуск в Kubernetes

Установить или обновить Helm-чарт:
```bash
helm install my-release . -n myapp

# После выполнения этой команды с помощью Notes в терминале пишется, какие команды вводить или по какому http открыть
```


Удалить Helm-чарт:
```bash
helm uninstall my-release -n myapp
```

---

## API

- **GET /ip** — возвращает ваш текущий IP.  
- Все успешные запросы сохраняются в базу данных PostgreSQL.  

Пример ответа:
```json
{
  "myIP": "145.10.34.3",
  "type": "IPAPI"
}
```

## Скриншот успешной работы
<img width="1790" height="1022" alt="image" src="https://github.com/user-attachments/assets/17f8b5c4-7df6-4d13-8771-eba1d99296cf" />
