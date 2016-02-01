from flask import url_for
from main import app


def t_url_for():
    with app.test_request_context():
        print(url_for('index'))
        print(url_for('add', x=1, y=3))
        print(url_for('static', filename='style.css'))


if __name__ == '__main__':
    t_url_for()
