import flask
from flask import Flask

app = Flask(__name__)
from flaskfiles.main import main
from flaskfiles.admin import admin

app.add_url_rule('/', view_func = main, methods=['GET'])
app.add_url_rule('/admin', view_func = admin, methods=['GET'])

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)