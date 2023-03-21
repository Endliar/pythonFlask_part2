import random
import json

import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('main.html')


@app.route('/about-us')
def about():
    return flask.render_template('about.html')


@app.route('/about-college')
def college():
    college_info = {
        1: {
            "Колледж": "мегаколледж вки нгу с лучшей общагой на свете",
            "плюсы": "ну он классный, чё, я вот там учился",
            "минусы": "отчислить могут",
            "достоинства": "есть собственный мегаробот уничтожитель в страшном здоровенном ящике aka восстали машины "
                           "из пепла ядерной войны ",
            "Общая оценка": 12.34532,
        },
        2: {
            "Колледж": "Новоколледж",
            "плюсы": "ну вроде просто норм, не особо шарю. Вам же норм",
            "минусы": "Дмитрий душнит на парах",
            "достоинства": "да, я знаю, что плюсы и достоинства это смежные термины,но менять уже не буду, а чё вы "
                           "мне сделаете? ",
            "Общая оценка": 8.12313123454567
        }
    }
    return flask.render_template('college.html', college=college_info)


@app.route('/students')
def students_view():
    student = {
        "Макаров Максим Сергеевич",
        "Ляжков Константин Андреевич",
        "Дёмин Сергей Дмитриевич"
    }
    return flask.render_template('students.html', students=student)


@app.route('/roses')
def roses_roses():
    roses = {
        "Red": ["Freedom", "Forever young", "Explorer"],
        "White": ["Polar Star", "Mondial", "Vendetta"],
        "Other": ["Engagement", "Topaz", "Miss Piggy"],
    }
    return flask.render_template('roses.html', roses=roses)


@app.route('/search')
def search_view():
    return flask.render_template('search.html')


@app.route('/dosearch/')
def do_search_view():
    s = flask.request.args.get('s')
    return f'Это страница поиска. Выполняется поиск по "{s}"'


if __name__ == "__main__":
    app.run(debug=True)
