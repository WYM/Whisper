#coding: utf8
from flask import Module, request, session, g, redirect, url_for, abort, render_template, flash
import hashlib, urllib, datetime
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
		default = url_for('.static', filename = 'default.jpg')
	if email:
		gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
	else:
		gravatar_url = default;
	gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
	return gravatar_url
	
def time_span(ts):
   delta = datetime.datetime.utcnow() - ts
   if delta.days >= 365:
       return u'%d年前' % (delta.days / 365)
   elif delta.days >= 30:
       return u'%d个月前' % (delta.days / 30)
   elif delta.days > 0:
       return u'%d天前' % delta.days
   elif delta.seconds < 60:
       return u"%d秒前" % delta.seconds
   elif delta.seconds < 60 * 60:
       return u"%d分钟前" % (delta.seconds / 60)
   else:
       return u"%d小时前" % (delta.seconds / 60 / 60)
