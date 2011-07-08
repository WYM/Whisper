#coding: utf8

from flask import Flask
from whisper import config
import pymongo

app = Flask(__name__)

app.config.from_object('whisper.config')
connection=pymongo.Connection(app.config['MONGODB_HOST'], app.config['MONGODB_PORT'])  
db = connection.whisper

from whisper.views.default import default
from whisper.views.admin import admin
from whisper.helper import helper

app.register_module(default)
app.register_module(admin, url_prefix='/admin')
app.register_module(helper, url_prefix='/helper')
