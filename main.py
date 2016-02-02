import pprint
from flask import Flask, request, render_template, Markup
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', name='World', ext_var=request.method)


@app.route('/add/<int:x>/<int:y>/')
def add(x, y):
    return '%d+%d=%d' % (x, y, x+y)


@app.template_filter('pp')
def filter_pp(x):
    s = pprint.pformat(x, indent=4, width=80)
    s = Markup.escape(s)
    return Markup('<pre>%s</pre>' % s)


@app.context_processor
def inject_dict():
    d = dict((x, x**2) for x in range(10))
    return dict(d=d)

@app.context_processor
def inject_fn():
    def f(n):
        return 'xyx '*n
    return dict(dub_str=f)


if __name__ == '__main__':
    app.debug=True
    app.run()
    # app.run(host='0.0.0.0')
