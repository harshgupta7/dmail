import os
from flask import Flask 
from flask_restful import Api
from resources.EmailResource import EmailServer, CheckEmail
from resources.UserResource import UserRegister, UserCheck

app = Flask(__name__)
api = Api(app)
app.secretkey = 'trenton alphanso miriam trotsky'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')


api.add_resource(EmailServer, '/send')
api.add_resource(CheckEmail,'/checkemail')
api.add_resource(UserRegister,'/register')
api.add_resource(UserCheck,'/finduser')





if __name__ == '__main__':


	from db import db 
	db.init_app(app)


	if app.config['DEBUG']:
		

	@app.before_first_request
	def create_table():
		db.create_all()


	app.run(debug=True)
