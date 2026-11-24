# Веломастерская «Крути педали» (`bike_service`)

Веб-приложение из двух сервисов: витрина услуг на **Flask** и калькулятор стоимости на **FastAPI**.

## Тема и правило расчёта
- **Тема:** Веломастерская (услуги по ремонту и настройке велосипедов).
- **Правило расчёта:** `итоговая_сумма = цена_услуги * количество` (количество — целое число от 1).
- **Пример расчёта:** Замена камеры стоит 450 ₽ за колесо. Для 2 колёс стоимость составит **900 ₽**.

## Локальный запуск (без Docker)

### 1. Витрина на Flask
```bash
cd vitrina
python -m venv .venv
source .venv/bin/activate  # для Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app app run --port 5000
```

### 2. Калькулятор на FastAPI
```bash
cd kalkulyator
python -m venv .venv
source .venv/bin/activate  # для Windows: .venv\Scripts\activate
pip install -r requirements.txt
fastapi dev main.py --port 8000
```

## Запуск на сервере через Docker Compose
- **Каталог проекта:** `~/voinov-bike-service`
- **Команда запуска:**
  ```bash
  docker compose up -d --build
  ```
- **Адреса на сервере (заполнить после деплоя):**
  - Витрина: `http://<IP-сервера>:<порт-1>/`
  - Форма калькулятора: `http://<IP-сервера>:<порт-2>/`
  - Документация API (`/docs`): `http://<IP-сервера>:<порт-2>/docs`