from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello World! (%s)<br><a href="/add/2/3/">2+3</a>' % request.method


@app.route('/add/<int:x>/<int:y>/')
def add(x, y):
    return '%d+%d=%d' % (x, y, x+y)


if __name__ == '__main__':
    app.debug=True
    app.run()
    # app.run(host='0.0.0.0')
