#coding: utf8
from flask import Module, request, session, g, redirect, url_for, abort, render_template, flash, current_app
from whisper import db
from whisper.helper import *

default = Module(__name__)

@default.route('/')
def index():
	db.test.insert({'name':'Mike', 'age': 17})
	return str(db.test.find_one())

@default.route('/login/', methods=['GET', 'POST'])
def login():
	if 'user' in session:
		return redirect(url_for('admin.index'))
	else:
		if request.method == 'POST':
			users = db.setttings.find({'type': 'users'})
			if user_valid(request.form['username'], request.form['password'], users):
				session.user = request.form['username']
				return redirect(url_for('admin.index'))
			else: 
				flash('用户名或密码可能存在错误，请重新登陆。')
				return redirect(url_for('login'))
		else:
			render_template('login.html')
