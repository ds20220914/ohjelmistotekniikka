from database_connection import get_database_connection

class Initialization:

	def remove_tables(get):
		db=sqlite3.connect(get)
		db.execute("DROP TABLE User")

	def create_tables(get):
		db=sqlite3.connect(get)
		db.execute("CREATE TABLE User (id INTEGER PRIMARY KEY, User_name TEXT, password TEXT,role_number INTEGER ) ")

	def initialize__database():
		get=get_database_connection()
		remove_tables(get)
		create_tables(get)

