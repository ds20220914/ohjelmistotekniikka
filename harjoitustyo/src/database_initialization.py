from database_connection import get_database_connection
from database_connection import get_course_connection
import sqlite3


def remove_tables(get):
	db=get.cursor()
	db.execute("DROP TABLE if exists User ")
	get.commit()

def create_tables(get):
	db=get.cursor()
	db.execute("CREATE TABLE User (id INTEGER PRIMARY KEY, User_name TEXT, password TEXT,role_number TEXT ) ")
	get.commit()

def remove_tables1(get1):
	db=get.cursor()
	db.execute("DROP TABLE if exists Course ")
	get.commit()

def create_tables1(get1):
	db=get.cursor()
	db.execute("CREATE TABLE Course (id INTEGER PRIMARY KEY, Role_number INTEGER,Course_name TEXT, grade INTEGER, credit INTEGER ) ")
	get.commit()



def initialize_database():
	get=get_database_connection()
	get1=get_course_connection()
	remove_tables1(get1)
	create_tables1(get1)
	remove_tables(get)
	create_tables(get)
	

