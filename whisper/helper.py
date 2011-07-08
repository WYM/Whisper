#coding: utf8
from flask import Module, request, session, g, redirect, url_for, abort, render_template, flash
import hashlib, urllib
from whisper import db

helper = Module(__name__)

@helper.route('/')
def index():
	return 'Access denied'

def valid_login(username, password, users):
	for user in users:
		if user.username == username and user.password == password:
			return True
	return False

def get_avatar(email, size = 42, default = ''):
	if not default:
		default = url_for('static', filename = 'default.jpg')
	gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
	gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
