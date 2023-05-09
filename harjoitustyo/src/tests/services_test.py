from service.studymonitoring_services import Services
import unittest
from repository.user_repository import user_repository
from repository.course_repository import course_repository
from entities.user import User
from entities.course import Course

class TestService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_first = User("moi", "1234", "A2222")
        self.user_sec=User("A_ope","1111","1111")
        self.user_thir=User("B_opi","2222","2222")
        self.course=Course("ma","5","5")

    def test_new_user(self):
        new = Services()
        right=new.new_user(self.user_first.username, self.user_first.password, self.user_first.role_number)
        list = user_repository.find_all()
        number=len(list)
        print(number)
        self.assertEqual(number, 0)
        self.assertEqual(right,False)
        
    def test_new_user1(self):
        new = Services()
        right=new.new_user(self.user_sec.username, self.user_sec.password, self.user_sec.role_number)
        list = user_repository.find_all()
        user=list[0]
        name=user["User_name"]
        self.assertEqual(name, "A_ope")
        self.assertEqual(right,True)
        
    def test_new_user2(self):
        new = Services()
        right=new.new_user(self.user_thir.username, self.user_thir.password, self.user_thir.role_number)
        list = user_repository.find_all()
        user=list[0]
        name=user["User_name"]
        self.assertEqual(name, "B_opi")
        self.assertEqual(right,True)
    def test_new_user3(self):
        new = Services()
        user=User("","2222","2222")
        right=new.new_user(user.username, user.password, user.role_number)
        list = user_repository.find_all()
        self.assertEqual(right,False)
    def test_new_user4(self):
        new = Services()
        user=User("A_ope","","2222")
        right=new.new_user(user.username, user.password, user.role_number)
        list = user_repository.find_all()
        self.assertEqual(right,False)
    def test_new_user5(self):
        new = Services()
        user=User("A_ope","2222","")
        right=new.new_user(user.username, user.password, user.role_number)
        list = user_repository.find_all()
        self.assertEqual(right,False)
    def test_new_user6(self):
        new = Services()
        user=User("B_opi","2222","2222")
        right=new.new_user(self.user_thir.username, self.user_thir.password, self.user_thir.role_number)
        right1=new.new_user(user.username, user.password, user.role_number)
        list = user_repository.find_all()
        self.assertEqual(right1,False)
    def test_new_user7(self):
        new = Services()
        right=new.new_user(self.user_thir.username, self.user_thir.password, self.user_thir.role_number)
        right1=new.new_user(self.user_sec.username, self.user_sec.password, self.user_sec.role_number)
        list = user_repository.find_all()
        self.assertEqual(right1,True)
        self.assertEqual(right,True)
    
    def test_add_new_course1(self):
        new = Services()
        new.new_user(self.user_thir.username, self.user_thir.password, self.user_thir.role_number)
        right=new.add_new_course(self.user_thir.role_number,self.course)
        list=new.find_course_by_username(self.user_thir.username)
        name=list[0]
        print(name["Course_name"])
        print(name["Role_number"])
        self.assertEqual(right,True)
        self.assertEqual(name["Course_name"],"ma")
    def test_add_new_course2(self):
        new = Services()
        right=new.add_new_course(self.user_thir.role_number,self.course)
        list=new.find_course_by_username(self.user_thir.username)
        number=len(list)
        self.assertEqual(right,False)
        self.assertEqual(number,0)
    def test_add_new_course3(self):
        course1=Course("ma","","5")
        new = Services()
        new.new_user(self.user_thir.username, self.user_thir.password, self.user_thir.role_number)
        right=new.add_new_course(self.user_thir.role_number,course1)
        list=new.find_course_by_username(self.user_thir.username)
        number=len(list)
        self.assertEqual(right,False)
    def test_add_new_course4(self):
        course1=Course("","5","5")
        new = Services()
        new.new_user(self.user_thir.username, self.user_thir.password, self.user_thir.role_number)
        right=new.add_new_course(self.user_thir.role_number,course1)
        list=new.find_course_by_username(self.user_thir.username)
        number=len(list)
        self.assertEqual(right,False)
    def test_add_new_course5(self):
        course1=Course("ma","5","")
        new = Services()
        new.new_user(self.user_thir.username, self.user_thir.password, self.user_thir.role_number)
        right=new.add_new_course(self.user_thir.role_number,course1)
        list=new.find_course_by_username(self.user_thir.username)
        number=len(list)
        self.assertEqual(right,False)
        
    def test_find_by_rolenumber(self):
        new = Services()
        right=new.new_user(self.user_sec.username, self.user_sec.password, self.user_sec.role_number)
        right1=new.add_new_course(self.user_sec.role_number,self.course)
        list=new.find_by_rolenumber(self.user_sec.role_number)
        user=list[0]
        name=user["Course_name"]
        self.assertEqual(name, "ma")
        self.assertEqual(right,True)
        
    def test_find_by_coursename_rolenumber(self):
        new = Services()
        right=new.find_by_coursename_rolenumber(self.user_sec.role_number,"ma")
        self.assertEqual(right,False)
    def test_find_by_coursename_rolenumber1(self):
        new = Services()
        right1=new.new_user(self.user_sec.username, self.user_sec.password, self.user_sec.role_number)
        right=new.find_by_coursename_rolenumber(self.user_sec.role_number,"")
        self.assertEqual(right,False)
    def test_find_by_coursename_rolenumber2(self):
        new = Services()
        right1=new.new_user(self.user_sec.username, self.user_sec.password, self.user_sec.role_number)
        right=new.find_by_coursename_rolenumber("","ma")
        self.assertEqual(right,False)
    def test_find_by_coursename_rolenumber3(self):
        new = Services()
        right1=new.new_user(self.user_sec.username, self.user_sec.password, self.user_sec.role_number)
        right=new.find_by_coursename_rolenumber(self.user_sec.role_number,"ma")
        self.assertEqual(right1,True)
        self.assertEqual(right,True)
        new.add_new_course(self.user_sec.role_number,self.course)
        right2=new.find_by_coursename_rolenumber(self.user_sec.role_number,"ma")
        self.assertEqual(right2,False)
    def test_find_by_coursename_rolenumber4(self):
        new = Services()
        new.new_user(self.user_sec.username, self.user_sec.password, self.user_sec.role_number)
        new.add_new_course(self.user_sec.role_number,self.course)
        right2=new.find_by_coursename_rolenumber(self.user_sec.role_number,"ne")
        self.assertEqual(right2,True)
        right3=new.find_by_coursename_rolenumber(self.user_sec.role_number,"ma")
        self.assertEqual(right3,False)
