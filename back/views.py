"""__author__ = pengshengbing"""
from flask import render_template, request, \
    session, Blueprint, redirect, url_for

from back.models import db, Blog, Article, ArticleType
from utils.functions import is_login

from werkzeug.security import generate_password_hash, check_password_hash
blue = Blueprint('first', __name__)


@blue.route('/')
@is_login
def index():
    return render_template('back/index.html')


@blue.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('back/register.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        if password and password2 and username:
            user = Blog.query.filter(Blog.username == username).first()
            if user:
                error = '该账号已注册,请更换账号'
                return render_template('back/register.html', error=error)
            else:
                if password2 == password:
                    user = Blog()
                    user.username = username
                    user.password = generate_password_hash(password)
                    db.session.add(user)
                    db.session.commit()
                    return redirect(url_for('first.login'))
                else:
                    error = '两次密码不一致'
                    return render_template('back/register.html', error=error)
        else:
            error = '请填写完整的信息'
            return render_template('back/register.html', error=error)


@blue.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('back/login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            user = Blog.query.filter(Blog.username == username).first()
            if not user:
                error = '该账号不存在,请先注册'
                return render_template('back/login.html', error=error)
            if not check_password_hash(user.password, password):
                error = '密码错误,请重新输入'
                return render_template('back/login.html', error=error)
            session['user_id'] = user.id
            return redirect(url_for('first.index'))
        else:
            error = '请填写完整的登录信息'
            return render_template('back/login.html', error=error)


@blue.route('/logout/', methods=['GET'])
def logout():
    del session['user_id']
    return redirect(url_for('first.login'))


# 文章分类管理
@blue.route('/a_type/', methods=['GET', 'POST'])
def a_type():
    if request.method == 'GET':
        types = ArticleType.query.all()

        return render_template('back/boke_list.html', types=types)


@blue.route('/add_type/', methods=['GET', 'POST'])
def add_type():
    if request.method == 'GET':
        return render_template('back/boke_add.html')
    if request.method == 'POST':
        atype = request.form.get('atype')
        if not atype:
            error = '请填写分类信息'
            return render_template('back/boke_add.html', error=error)
        art_type = ArticleType()
        art_type.t_name = atype
        db.session.add(art_type)
        db.session.commit()
        return redirect(url_for('first.a_type'))

#  删除文章分类


@blue.route('/del_type/<int:id>/', methods=['GET'])
def del_type(id):
    d_type = ArticleType.query.get(id)
    db.session.delete(d_type)
    db.session.commit()
    return redirect(url_for('first.a_type'))


@blue.route('/a_list/', methods=['GET'])
def a_list():
    articles = Article.query.all()
    return render_template('back/boke_lists.html', articles=articles)


@blue.route('/article_add/', methods=['GET', 'POST'])
def article_add():
    if request.method == 'GET':
        arts = ArticleType.query.all()
        return render_template('back/article_detail.html', arts=arts)
    if request.method == 'POST':
        title = request.form.get('name')
        desc = request.form.get('desc')
        category = request.form.get('category')
        content = request.form.get('content')
        if title and desc and category and content:
            art = Article()
            art.title = title
            art.desc = desc
            art.content = content
            art.type = category
            db.session.add(art)
            db.session.commit()
            return redirect(url_for('first.a_list'))
        else:
            error = '请填充完整的信息'
            return render_template('back/article_detail.html', error=error)

# 用户列表


@blue.route('/user/')
def user():
    return render_template('back/user_list.html')

# 文章删除

@blue.route('/del_art/<int:id>/')
def del_art(id):
    art = Article.query.get(id)
    print(art)
    db.session.delete(art)

    db.session.commit()
    return redirect(url_for('first.a_list'))



