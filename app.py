import os
import flask
from flask import Flask
# from flask_login import LoginManager

SECRET_KEY = os.urandom(32)
app = Flask(__name__)
# login_manager = LoginManager()

from flaskfiles.main import main
from flaskfiles.admin import admin
from flaskfiles.viewcompound import viewcompound
from flaskfiles.inventory import inventory

app.add_url_rule('/', view_func = main, methods=['GET'])
app.add_url_rule('/admin', view_func = admin, methods=['GET'])
app.add_url_rule('/compound/<compName>', view_func = viewcompound, methods = ['GET', 'POST'])
app.add_url_rule('/inventory', view_func = inventory, methods=['GET','POST'])


app.config['SECRET_KEY'] = SECRET_KEY
# login_manager.init_app(app)



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)