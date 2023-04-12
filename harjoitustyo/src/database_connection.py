

import sqlite3
from config import DATABASE_FILE_PATH
from config import DATABASE_FILE_PATH1

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row

connection_course = sqlite3.connect(DATABASE_FILE_PATH1)
connection_course.row_factory = sqlite3.Row


def get_database_connection():
    return connection
    
def get_course_connection():
    return connection_course
