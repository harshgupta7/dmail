from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('username', type=str, required=True, help='username is required')
	parser.add_argument('pub_key', type=str, required=True, help='pub_key is required')




	def post(self):
	"""create new user"""

		data = UserRegister.parser.parse_args()

		if UserModel.find_by_username(data['username']):

			return {'message':'username already taken'}

		if UserModel.find_by_pubkey(data['pub_key']):

			return {'message':'user with this pub_key already exists'}


		user = UserModel(data['username'], data['pub_key'])
		user.save_to_db()
		return item.json()


	def get(self):
	"""check if user exists"""

		data = Item.parser.parse_args()

		user = UserModel.find_by_username(data['username'])

		if not user:

			return {'message':'no such user exists'}

		if user.pub_key != data['pub_key']:

			return {'message':'no such user exists'}

		return user.json()


class UserCheck(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('pub_key', type=str, required=True, help='pub_key is required')

	def get(self):

		data = UserCheck.parser.parse_args()

		user = UserModel.find_by_pubkey(data['pub_key'])

		if user:

			return user.json()

		return {'message':'no user exists'}

	








