from repository.user_repository import user_repository
from repository.course_repository import course_repository
from entities.user import User
import matplotlib.pyplot as plt


class Services:
    ''' sovelluslogiikasta vastaava luokka'''

    def new_user(self, name, password, role_number):
        ''' luo uuden käyttäjän tietokantaan 
            Args:
               name:uuden käyttäjän nimi
               password:uuden käyttäjän salasana
               role_number:uuden käyttäjän roolinumero(opiskelijanumero tai opettajanumero)
            Returns:
               user-olio
        '''
        user = user_repository.create(User(name, password, role_number))
        return user

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
        lista = course_repository.find_all_course_by_student_role_number(
            number)
        return lista

    def find_by_rolenumber(self, rolenumber):
        ''' etsi kurssien suoritustiedot roolinumero(opiskelijanumero) avulla
            Args:
                rolenumber: roolinumero
            Returns:
               palauttaa käyttäjän jokaisen kurssin suoritustiedot tupleina listassa
        '''
        lista = course_repository.find_all_course_by_student_role_number(
            rolenumber)

        return lista

    def find_by_coursename_rolenumber(self, rolenumber, course_name):
        ''' etsi onko tietty kurssin suoritustieto jo olemassa tietokannassa
            Args:
                rolenumber: roolinumero
                course_name: kurssin nimi
            Returns:
                palauttaa True jos kurssitieto jo olemassa, False jos ei ole olemassa
        '''
        lista = course_repository.find_all_course_by_student_role_number(
            rolenumber)
        for i in lista:
            if course_name == i["Course_name"]:
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
        '''
        if username[0] == "A":
            lista = user_repository.find_all()
            for i in lista:
                if username == i["User_name"] and password == i["password"]:
                    return 1
        elif username[0] == "B":
            lista = user_repository.find_all()
            for i in lista:
                if username == i["User_name"] and password == i["password"]:
                    return 2

    def add_new_course(self, rolenumber, course):
        ''' lisää uuden suoritustieto opiskelijalle
            Args:
                rolenumber: käyttäjän roolinumero
                course: kurssi-oliona
        '''
        course_repository.create_course(rolenumber, course)

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
        else:
            return summa
    def show_diagram(self,username):
        array=self.find_course_by_username(username)
        array2=[]
        array3=[]
        for i in range(1,len(array)):
            array3.append(i)
        for i in range(1,len(array)):
            array2.append((array[i]["grade"])/i)
        plt.plot(array3,array2)
        plt.ylabel('average grade')
        plt.xlabel("number of grade")
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
       
  
