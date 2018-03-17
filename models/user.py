from db import db

class UserModel(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False)
	pub_key = db.Column(db.Text, nullable=False)

	def __init__(self, username, pub_key):

		self.username = username
		self.pub_key = pub_key

	def save_to_db(self):

		db.session.add(self)
		db.session.commit()

	def json(self):

		return {'username':self.username, 'pub_key':self.pub_key}

	def delete(self):

		db.session.delete(self)
		db.session.commit()

	@staticmethod
	def find_by_username(username):

		return UserModel.query.filter_by(username=username).first()

	@staticmethod
	def find_by_pubkey(pub_key):

		return UserModel.query.filter_by(pub_key=pub_key).first()

	@staticmethod
	def find_by_id(_id):

		return UserModel.query.filter_by(id=_id).first()





