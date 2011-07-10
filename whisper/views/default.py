#coding: utf8
from flask import Module, request, session, g, redirect, url_for, abort, render_template, flash, current_app, get_flashed_messages
from whisper import db
from whisper.helper import *
import datetime

default = Module(__name__)

@default.route('/')
def index():
	data = db.posts.find()
	if get_flashed_messages():
		message = get_flashed_messages()[0]
	else:
		message = 'Making splendid shots of our life!'
	return render_template('index.html', data = data, message = message, get_avatar = get_avatar, time_span = time_span)

@default.route('/post/', methods=['POST', 'GET'])
def post():
	if request.method == 'POST' and request.form['name'] and request.form['email'] and request.form['content']:
		db.posts.insert({
			'id': db.ids.find_and_modify({"name":"posts"}, {'$inc':{'id':1}}, True),
			'name': request.form['name'],
			'email': request.form['email'],
			'content': request.form['content'],
			'dateline': datetime.datetime.utcnow(),
			'comments': [],
		})
		
		flash(request.form['name'] + u'，您的帖子已经发表成功~')
	else:
		flash(request.form['name'] + u'，请填写所有需要的项目后再发表~')
	return(redirect(url_for('index')))

@default.route('/star/<int:pid>/')
def star(pid):
	#db.posts.update({'id': pid}, {'$set': {'star' : 1}}, True)
	flash(u'成功给帖子加上星标')
	return(redirect(url_for('index')))

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
