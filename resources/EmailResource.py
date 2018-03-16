from flask_restful import Resource, reqparse
from models.email import PendingEmails
from models.user import UserModel

class EmailServer(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument('pub_key', type=str, required=True, help='pub_key is required')
	parser.add_argument('email_hash', type=str, required=True, help='email_hash is required')


	def post(self):

		"""post new email"""

		data = EmailServer.parser.parse_args()

		if not UserModel.find_by_pubkey(data['pub_key']):

			return {'message':'No user with that pub_key exists'}


		email = PendingEmails(to=data['pub_key'], email_hash=data['email_hash'])

		email.save_to_db()

		return email.json()


	def get(self):

		"""check if an email is still not downloaded by a particular user"""

		data = EmailServer.parser.parse_args()

		if PendingEmails.find_by_pubkey(data['email_hash']):

			if PendingEmails.find_by_to(data['pub_key']):

				return {'message':'email not yet downloaded'}

		return {'message':'email not in server'}




class CheckEmail(Resource):

	parser = reqparse.RequestParser()

	parser.add_argument('pub_key')

	def get(self):

		data = EmailServer.parser.parse_args()

		emails = PendingEmails.find_by_to(data['pub_key'])

		if not emails:

			return {'message':'no new emails'}


		hashes = []
		for x in emails:

			hashes.append(x.get_email_hash())

		return {'emails':hashes}

		




