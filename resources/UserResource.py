from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('username', type=str, required=True, help='username is required')
	parser.add_argument('pub_key', type=str, required=True, help='pub_key is required')




	def post(self):

		data = UserRegister.parser.parse_args()

		if UserModel.find_by_username(data['username']):

			return {'message':'username already taken'}

		if UserModel.find_by_pubkey(data['pub_key']):

			return {'message':'user with this pub_key already exists'}


		user = UserModel(data['username'], data['pub_key'])
		user.save_to_db()
		return user.json()


class UserCheck(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('pub_key', type=str, required=True, help='pub_key is required')

	def post(self):

		data = UserCheck.parser.parse_args()

		user = UserModel.find_by_pubkey(data['pub_key'])

		if user:

			return user.json()

		return {'message':'no user exists'}


class DeleteUser(Resource):

	def delete(self, name):

		user = UserModel.find_by_username(name)

		if user:

			user.delete()

		return {'message':'user deleted'}





class GetAllUsers(Resource):

	def get(self):

		result = UserModel.query.all()
		return {'users':[x.json() for x in result]}








