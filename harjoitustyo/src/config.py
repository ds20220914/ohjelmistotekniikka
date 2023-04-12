import os


dirname = os.path.dirname(__file__)



DATABASE_FILENAME = os.getenv("Smonitoring_database") or "Smonitoringdatabase.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

course_list_FILENAME= os.getenv("Course_database") or "Course_database.sqlite"
DATABASE_FILE_PATH1 = os.path.join(dirname, "..", "data", course_list_FILENAME)
