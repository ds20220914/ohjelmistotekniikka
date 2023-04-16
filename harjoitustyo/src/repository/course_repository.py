from entities.user import User
from database_connection import get_database_connection
from database_connection import get_course_connection



class CourseRepository:
	def __init__(self, connection1,connection2):

		self._connection1=connection1
		self._connection2=connection2
		
	def create_course(self, role_number,course):
		 
		db=self._connection2.cursor()
		db.execute("INSERT INTO Course (Role_number,Course_name,grade,credit) values (?,?,?,?)",(role_number,course.course_name,course.grade,course.credits))
		self._connection2.commit()
		return User
	def find_all_course(self):
		db=self._connection2.cursor()
		lista=db.execute("SELECT * FROM Course ").fetchall()
		return list(lista)
		
	def find_all_course_by_Student_role_number(self,rolenumber):
		db=self._connection2.cursor()
		lista=db.execute("SELECT * FROM Course WHERE Role_number=?",(rolenumber,)).fetchall()
		return list(lista)
		
course_repository=CourseRepository(get_database_connection(),get_course_connection())
