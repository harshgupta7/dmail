from flask_restful import Resource, reqparse
from models.item import UserModel


class User(Resource):

	parser = reqparse.RequestParser()