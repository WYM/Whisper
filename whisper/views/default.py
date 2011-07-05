#coding: utf8
from flask import Module, request, session, g, redirect, url_for, abort, render_template, flash, current_app
from mongokit import Connection, Document
from whisper import db

default = Module(__name__)

@default.route('/')
def index():
	db.test.insert({'name':'Mike', 'age': 17})
	return str(db.test.find_one())
