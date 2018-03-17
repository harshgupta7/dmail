from db import db

class PendingEmails(db.Model):

	__tablename__ = 'pendingemails'

	id = db.Column(db.Integer, primary_key=True)
	to = db.Column(db.String(500), nullable=False)
	email_hash = db.Column(db.String(500), nullable=False)


	def __init__(self, to, email_hash):

		self.to = to
		self.email_hash = email_hash


	def get_email_hash(self):

		return self.email_hash



	def save_to_db(self):

		db.session.add(self)
		db.session.commit()

	def delete(self):

		db.session.delete(self)
		db.session.commit()

	def json(self):

		return {'to':self.to, 'email_hash':self.email_hash}


	@staticmethod
	def find_by_id(_id):

		return PendingEmails.query.filter_by(id=_id).first()

	@staticmethod
	def find_by_to(to):

		return PendingEmails.query.filter_by(to=to).all()

	@staticmethod
	def find_by_emailhash(email_hash):

		return PendingEmails.query.filter_by(email_hash=email_hash).first()



