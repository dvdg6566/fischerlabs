import os
import flask
from flask import Flask,session,request,flash,redirect
from werkzeug.security import generate_password_hash, check_password_hash
import awstools
from forms import LoginForm
from flask import render_template

# from flask_login import LoginManager

SECRET_KEY = "21 IS A VERY GOOD NUMBER"
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config["SESSION_PERMANENT"] = True
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_NAME'] = 'login-session'

from flaskfiles.main import main
from flaskfiles.viewcompound import viewcompound,addItem
from flaskfiles.inventory import inventory
from flaskfiles.login import login
from flaskfiles.signup import signup
from flaskfiles.order import order,changeOrder
from flaskfiles.profile import profile

app.add_url_rule('/', view_func = main, methods=['GET'])
app.add_url_rule('/login', view_func = login, methods=['GET','POST'])
app.add_url_rule('/addItem',view_func=addItem,methods = ['POST'])
app.add_url_rule('/changeOrder',view_func=changeOrder,methods=['POST'])
app.add_url_rule('/compound/<compound>', view_func = viewcompound, methods = ['GET', 'POST'])
app.add_url_rule('/inventory', view_func = inventory, methods=['GET','POST'])
app.add_url_rule('/signup', view_func = signup, methods=['GET','POST'])
app.add_url_rule('/profile', view_func = profile, methods=['GET','POST'])
app.add_url_rule('/order/<orderID>',view_func=order,methods=['GET','POST'])

@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    flash('Logout successful', 'info')
    return redirect('/')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)