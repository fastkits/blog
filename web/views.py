"""__author__ = pengshengbing"""
from flask import render_template, Blueprint, redirect, url_for

from back.models import ArticleType, Article

web_blue = Blueprint('web', __name__)


@web_blue.route('/index/')
def index():
    arts = Article.query.all()
    art_type = ArticleType.query.all()
    return render_template('web/index.html/', arts=arts, art_type=art_type)


@web_blue.route('/info/<int:id>/')
def info(id):
    art_info = Article.query.get(id)
    art_type = ArticleType.query.all()
    return render_template('web/info.html', art_info=art_info, art_type=art_type)


@web_blue.route('/type_info/<int:id>/')
def type_info(id):
    arts = Article.query.filter(Article.type == id).all()
    art_type = ArticleType.query.all()
    return render_template('web/type.html', arts=arts, art_type=art_type)


@web_blue.route('/type_info_arts/<int:id>/')
def type_info_arts(id):
    art_info = Article.query.get(id)
    art_type = ArticleType.query.all()
    return render_template('web/info.html', art_info=art_info, art_type=art_type)


@web_blue.route('/about/')
def about():
    art_type = ArticleType.query.all()
    return render_template('web/about.html', art_type=art_type)

@web_blue.route('/list/')
def list():
    art_type = ArticleType.query.all()
    return render_template('web/list.html', art_type=art_type)


@web_blue.route('/girl/')
def grils():

    return '<h1>哈哈哈哈,我是迪丽热青</h1>'


@web_blue.route('/liuyanban/')
def liuyan():

    return render_template('web/liuyan.html')

