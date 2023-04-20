import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv(
     "DATABASE_FILENAME") or "Smonitoringdatabase.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

COURSE_LIST_FILENAME = os.getenv("COURSE_LIST_FILENAME") or "Course_database.sqlite"
DATABASE_FILE_PATH1 = os.path.join(dirname, "..", "data", COURSE_LIST_FILENAME)
