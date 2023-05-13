import matplotlib.pyplot as plt
from repository.user_repository import user_repository
from repository.course_repository import course_repository
from entities.user import User



class Services:
    ''' sovelluslogiikasta vastaava luokka'''

    def new_user(self, name, password,role_number):
        ''' lisää uuden käyttäjän tietokantaan 
            Args:
               name:uuden käyttäjän nimi
               password:uuden käyttäjän salasana
               role_number:uuden käyttäjän roolinumero(opiskelijanumero tai opettajanumero)
            Returns:
               user-olio
        '''
        if len(name) == 0 or len(password) == 0 or len(role_number) == 0:
            return False
        lista = user_repository.find_all()
        for i in lista:
            if name in i:
                return False
        if name[0]!="A" and name[0]!="B":
            return False
        user_repository.create(User(name, password, role_number))
        return True

    def find_course_by_username(self, username):
        ''' etsi kurssien suoritustiedot käyttäjänimen avulla
            Args:
               username: käyttäjänimi
            Returns:
               palauttaa käyttäjän jokaisen kurssin suoritustiedot tupleina listassa
        '''
        rolenumber = user_repository.find_by_username(
            username)
        number = None
        for i in rolenumber:
            number = i["role_number"]
        list1 = course_repository.find_all_course_by_student_role_number(
            number)
        return list1

    def find_by_rolenumber(self, rolenumber):
        ''' etsi kurssien suoritustiedot roolinumero(opiskelijanumero) avulla
            Args:
                rolenumber: roolinumero
            Returns:
               palauttaa käyttäjän jokaisen kurssin suoritustiedot tupleina listassa
        '''
        list1 = course_repository.find_all_course_by_student_role_number(
            rolenumber)

        return list1

    def find_by_coursename_rolenumber(self, rolenumber, course_name):
        ''' etsi onko tietty opiskelijan tietyn kurssin suoritustieto jo olemassa tietokannassa
            Args:
                rolenumber: roolinumero
                course_name: kurssin nimi
            Returns:
                palauttaa True jos kurssitieto jo olemassa, False jos ei ole olemassa
        '''
        all_user=user_repository.find_all()
        exist=False
        for i in all_user:
            if rolenumber in i:
                exist=True
        if exist is False:
            return False
        if len(rolenumber)==0 or len(course_name)==0:
            return False
        lista = course_repository.find_all_course_by_student_role_number(
            rolenumber)
        for i in lista:
            if course_name==i["Course_name"]:
                return False
        return True

    def login(self, username, password):
        ''' kirjaa käyttäjän sisään
            Args:
                username:käyttäjänimi
                password:salasana
            Returns:
                jos käyttäjänimi alkaa A, eli on opettaja,
                     ja käyttäjänimi ja salasana oikein, palauttaa 1
                jos käyttäjänimi alkaa B, eli on opiskelija,
                     ja käyttäjänimi ja salasana oikein, palauttaa 2
                jos käyttäjänimi ei alka A tai B tai jos salasana tai käyttäjänimi
                     on väärin, palauttaa 3
        '''
        if len(username) != 0 and len(password) != 0:
            lista = user_repository.find_all()
            for i in lista:
                if username == i["User_name"] and password == i["password"]:
                    if username[0] == "A":
                        return 1
                    if username[0] == "B":
                        return 2
        return 3

    def add_new_course(self, rolenumber, course):
        ''' lisää uuden suoritustieto opiskelijalle
            Args:
                rolenumber: käyttäjän roolinumero
                course: kurssi-oliona
        '''
        result1 = self.find_by_coursename_rolenumber(rolenumber, course.course_name)
        list1 = ["0", "1", "2", "3", "4", "5"]
        if (
           len(course.course_name) == 0 or len(rolenumber) == 0 or
           len(course.credits) == 0 or len(course.grade) == 0 or
           course.credits not in list1 or course.grade not in list1 or
           course.course_name is None or rolenumber is None or
           course.credits is None or course.grade is None
        ):
            return False
        if result1 is False:
            return False
        course_repository.create_course(rolenumber, course)
        return True
    def average_grade(self, username):
        ''' laskee opiskelijan keskiarvo
            Args:
                username:käyttäjänimi
            Returns:
                palauttaa keskiarvo tai jos ei ole suoritanut yhtään kurssi niin palauttaa 0.
        '''
        lista = user_repository.find_by_username(username)
        rolenumber = lista[0]["role_number"]
        courses = course_repository.find_all_course_by_student_role_number(
            rolenumber)
        summa = 0
        for i in courses:
            summa += i["grade"]
        if len(courses) != 0:
            return summa/len(courses)
        return summa
    def show_diagram(self,username):
        array=self.find_course_by_username(username)
        array2=[]
        array3=[]
        summa=0
        for i in range(1,len(array)+1):
            array3.append(i)
        for i in range(1,len(array)+1):
            luku=array[i-1]["grade"]
            summa+=luku
            array2.append(summa/i)
        plt.plot(array3,array2,"r-")
        plt.ylabel('average grade')
        plt.xlabel("number of course")
        plt.axis([0,len(array2)+1,0,max(array2)+1])
        plt.show()
    def credit_sum(self, username):
        ''' laskee opintopisteiden summa
            Args:
                username: käyttäjänimi
            Returns:
                palauttaa opintopisteiden summa
        '''
        lista = user_repository.find_by_username(username)
        rolenumber = lista[0]["role_number"]
        courses = course_repository.find_all_course_by_student_role_number(
            rolenumber)
        summa = 0
        for i in courses:
            summa += i["credit"]
        return summa
    def delete_course(self,name,rolenumber):
        delete=course_repository.delete_course(name,rolenumber)
        return delete
