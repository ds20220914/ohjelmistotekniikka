from database_connection import get_database_connection
import sqlite3


def remove_tables(get):
	db=get.cursor()
	db.execute("DROP TABLE if exists User ")
	get.commit()

def create_tables(get):
	db=get.cursor()
	db.execute("CREATE TABLE User (id INTEGER PRIMARY KEY, User_name TEXT, password TEXT,role_number TEXT ) ")
	get.commit()
def initialize_database():
	get=get_database_connection()
	remove_tables(get)
	create_tables(get)
	return 9

