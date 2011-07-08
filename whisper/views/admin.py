#coding: utf8
from flask import Module, request, session, g, redirect, url_for, abort, render_template, flash
from whisper import db
from whisper.helper import *

admin = Module(__name__)

@admin.before_request
def berore_request():
	if 'user' not in session:
		return str(url_for('default.login'))

@admin.route('/')
def index():
	return ''

@admin.route('/login')
def login():
	return 'admin that is.'
