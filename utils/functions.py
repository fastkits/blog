"""__author__ = pengshengbing"""
# 登录过后能够访问index.html
# 没有登录不给访问,跳转到session_login.html页面
# 条件

# 1.外层函数嵌套内层函数
# 2.外层函数返回内层函数
# 3.内层函数调用外层函数的参数
from functools import wraps

from flask import session, redirect, url_for, render_template


def is_login(func):
    @wraps(func)
    def check():
        user_id = session.get('user_id')
        if user_id:
            return func()
        else:
            return redirect(url_for('first.login'))
    return check

