from flask import Flask, render_template
from flask import url_for

#app obj
app = Flask(__name__)

name='Xdh'
movies=[
    {'title': 'Inception', 'year': '2010'},
    {'title': 'Interstellar', 'year': '2014'},
    {'title': 'Dunkirk', 'year': '2017'},
    {'title': 'Bat Man I', 'year': '2005'},
    {'title': 'Bat Man II', 'year': '2008'},
    {'title': 'Bat Man III', 'year': '2012'},
    {'title': 'TENET', 'year': '2020'},
    {'title': 'The Prestige', 'year': '2006'}
]


@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)

# @app.route('/main')
# def main():
#     return '<h1>Hello World!</h1>'
#
# @app.route('/user/<name>')
# def user_page(name):
#     return 'User: %s' % name

# @app.route('/test')
# def test_url_for():
#     #url_for通过函数生成url规则
#     print(url_for('hello'))
#     print(url_for('main'))
#     print(url_for('user_page',name='peter'))





if __name__ == '__main__':
    app.run()
