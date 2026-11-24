from pathlib import Path
from typing import Literal

from fastapi import Query
from fastapi.responses import FileResponse
from fastapi_offline import FastAPIOffline

app = FastAPIOffline(title="Веломастерская «Крути педали»", redoc_url=None)
prices = {
    "brake_setup": 350,
    "tube_replacement": 450,
    "derailleur_tuning": 500,
}
names = {
    "brake_setup": "Настройка тормоза",
    "tube_replacement": "Замена камеры",
    "derailleur_tuning": "Регулировка переключателя",
}


@app.get("/", include_in_schema=False)
def home():
    return FileResponse(Path(__file__).with_name("index.html"))


@app.get("/api/price", summary="Рассчитать стоимость ремонта")
def calculate_price(
    item: Literal["brake_setup", "tube_replacement", "derailleur_tuning"],
    quantity: int = Query(1, ge=1, le=20),
):
    unit_price = prices[item]
    return {
        "item": item,
        "name": names[item],
        "quantity": quantity,
        "unit_price": unit_price,
        "total": unit_price * quantity,
    }