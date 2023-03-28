import os
import sqlite3

class Initialization:

	def create_database():
		db=sqlite3.connect("user.db")
		db.execute("CREATE TABLE User (id INTEGER PRIMARY KEY, User_name TEXT, password TEXT,role_number INTEGER ) ")

	def connect_to_database():
		db=sqlite3.connect("user.db")
