from database_connection import get_database_connection
from database_connection import get_course_connection


def remove_tables(get):
    db_connection = get.cursor()
    db_connection.execute("DROP TABLE if exists User ")
    get.commit()


def create_tables(get):
    db_connection = get.cursor()
    db_connection.execute('''CREATE TABLE User (
			id INTEGER PRIMARY KEY,
			User_name TEXT,
			password TEXT,
			role_number TEXT
		) ''')
    get.commit()


def remove_tables1(get1):
    db1_connection = get1.cursor()
    db1_connection.execute("DROP TABLE if exists Course ")
    get1.commit()


def create_tables1(get1):
    db1_connection = get1.cursor()
    db1_connection.execute('''CREATE TABLE Course (
			id INTEGER PRIMARY KEY,
			Role_number INTEGER,
			Course_name TEXT,
			grade INTEGER,
			credit INTEGER
		) ''')
    get1.commit()


def initialize_database():
    get = get_database_connection()
    get1 = get_course_connection()
    remove_tables1(get1)
    create_tables1(get1)
    remove_tables(get)
    create_tables(get)
