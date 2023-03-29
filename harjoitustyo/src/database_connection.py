import sqlite
from config import Smonitor_File_path1

connection1=sqlite3.connect(Smonitor_File_path1


def get_database_connection():
	return connection1
