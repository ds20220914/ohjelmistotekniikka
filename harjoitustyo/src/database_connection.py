import sqlite3
from config import DATABASE_FILE_PATH
from config import DATABASE_FILE_PATH1

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row

connection_course = sqlite3.connect(DATABASE_FILE_PATH1)
connection_course.row_factory = sqlite3.Row


def get_database_connection():
    ''' antaa polku käyttäjista vastaava tietokantaan
        Returns:
              polku käyttäjätietokantaan 
    '''
    return connection


def get_course_connection():
    ''' antaa polku kurssisuorituksista vastaava tietokantaan
        Returns:
              polku kurssisuoritus tietokantaan
    '''
    return connection_course
