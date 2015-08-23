#coding: utf8
from flask import Flask
import hashlib, pymongo
app = Flask(__name__)

connection=pymongo.Connection('localhost', 27017)  
db = connection.whisper

@app.route('/')
def install():
	username = u'WYM'
	password = 'pass'
	title = u'Whisper of ' + username
	introduce = u'Welcome to ' + username + '\'s Microblog. There are some interesting things should be share to you.'
	
	password = hashlib.new('md5', password).hexdigest()
	#password.digest()
	#password = password.hexdigest()
	
	DBsettings = db.settings
	if DBsettings.find():
		return '您已经在该数据库中安装了Whisper，无需重复安装。 \r\n You have already installed the Whisper before.'

	settings = [{'type': 'website', 'title': title, 'introduce': introduce}, {'type': 'users', 'username': username, 'password': password}]
	result = DBsettings.insert(settings)
	
	if result:
		return u'安装成功，请终止install并运行Whisper。 \r\n Successfully, Please stop the installer and make the Whisper run.'
	else:
		return u'发生了错误，安装失败。 \r\n Error, Can\'t update database.'

if __name__ == '__main__':
    app.run()
