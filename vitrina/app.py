from flask import Flask, abort, render_template

app = Flask(__name__)

SERVICES = {
    "brake_setup": {
        "name": "Настройка тормоза",
        "price": 350,
        "duration": "20 мин",
        "description": "Регулировка натяжения троса, центровка калипера и проверка износа тормозных колодок.",
    },
    "tube_replacement": {
        "name": "Замена камеры",
        "price": 450,
        "duration": "15 мин",
        "description": "Снятие колеса, демонтаж покрышки, установка новой камеры и накачка до рабочего давления.",
    },
    "derailleur_tuning": {
        "name": "Регулировка переключателя",
        "price": 500,
        "duration": "30 мин",
        "description": "Настройка ограничительных винтов L/H и индексации переключения передач на стенде.",
    },
}


@app.get("/")
def menu():
    return render_template("menu.html", services=SERVICES)


@app.get("/services/<slug>")
def service_detail(slug):
    service = SERVICES.get(slug)
    if service is None:
        abort(404)
    return render_template("drink.html", service=service)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404