#coding: utf8
from flask import Module, request, session, g, redirect, url_for, abort, render_template, flash

admin = Module(__name__)

@admin.route('/')
def index():
	return 'admin that is.'
