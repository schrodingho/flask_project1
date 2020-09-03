from flask import Flask, render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql
pymysql.install_as_MySQLdb()






#app obj
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@127.0.0.1:3306/flask_sql_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

##commander: initdb 数据库初始化
import click
@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:  # 判断是否输入了选项
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息


@app.cli.command()
def forge():
    db.drop_all()
    """Generate fake data."""
    db.create_all()

    # 全局的两个变量移动到这个函数内
    name = 'Grey Li'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字

class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份





# name='Xdh'
# movies=[
#     {'title': 'Inception', 'year': '2010'},
#     {'title': 'Interstellar', 'year': '2014'},
#     {'title': 'Dunkirk', 'year': '2017'},
#     {'title': 'Bat Man I', 'year': '2005'},
#     {'title': 'Bat Man II', 'year': '2008'},
#     {'title': 'Bat Man III', 'year': '2012'},
#     {'title': 'TENET', 'year': '2020'},
#     {'title': 'The Prestige', 'year': '2006'},
#     {'title': 'None', 'year': 'None '}
# ]


@app.route('/')
def index():
    user = User.query.first()  # 读取用户记录
    movies = Movie.query.all()  # 读取所有电影记录
    return render_template('index.html',user=user,movies=movies)



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
#     print(url_for('hello'))#传入端点值（视图函数的名称）和参数，它会返回对应的 URL。
#     print(url_for('main'))
#     print(url_for('user_page',name='peter'))





if __name__ == '__main__':
    app.run()
