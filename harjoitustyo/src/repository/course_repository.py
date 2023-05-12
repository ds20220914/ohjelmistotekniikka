from database_connection import get_database_connection
from database_connection import get_course_connection


class CourseRepository:
    ''' luokka joka vastaa kurssisuorituksien tietokannan operaatioita
        Attribuutit:
           connection1: Tietokantayhteyden Connection-olio(käyttäjätiedon tietokanta)
           connection2: Tietokantayhteyden Connection-olio(kurssitiedon tietokanta)
    '''

    def __init__(self, connection1, connection2):
        ''' luokan konstruktori.
            Args:
                 connection1: Tietokantayhteyden Connection-olio(käyttäjätiedon tietokanta)
                 connection2: Tietokantayhteyden Connection-olio(kurssitiedon tietokanta)
        '''
        self._connection1 = connection1
        self._connection2 = connection2

    def create_course(self, role_number, course):
        ''' luoda uusi kurssisuoritus tietokantaan
            Args:
               role_number: suorituksen "opiskelijan" opiskelijanumero
               course: Tallennettava kurssisuoritus course-oliona.
            Returns:
               palauttaa user-olio
        '''
        db_connection = self._connection2.cursor()
        db_connection.execute("INSERT INTO Course (Role_number, Course_name, grade, credit) "
                              "VALUES (?, ?, ?, ?)",
                              (role_number, course.course_name, course.grade, course.credits))
        self._connection2.commit()

    def find_all_course(self):
        ''' palauttaa kaikkien kurssisuorituksien tiedot
            Returns:
                palauttaa jokaisen kurssisuorituksen kurssinimi,
                     opintopiste ja arvosana tupleina listassa
        '''
        db_connection = self._connection2.cursor()
        lista = db_connection.execute("SELECT * FROM Course ").fetchall()
        return list(lista)

    def find_all_course_by_student_role_number(self, rolenumber):
        ''' palauttaa kaikkien kurssisuorituksien tiedot opiskelijanumeron perusteella
            Returns:
                palauttaa opiskelijanumeron perusteella jokaisen kurssisuorituksen kurssinimi,
                    opintopiste ja arvosana tupleina listassa
        '''
        db_connection = self._connection2.cursor()
        lista = db_connection.execute(
            "SELECT * FROM Course WHERE Role_number=?", (rolenumber,)).fetchall()
        return list(lista)
    def delete_course(self,name,rolenumber):
        cursor = self._connection2.cursor()
        cursor.execute("delete from Course WHERE Role_number=? and Course_name=?",
            (rolenumber,name,))
        self._connection2.commit()
        return True
    def delete_all(self):
        ''' poistaa kaikki suoritukset'''
        cursor = self._connection2.cursor()
        cursor.execute("delete from Course")
        self._connection2.commit()


course_repository = CourseRepository(
    get_database_connection(), get_course_connection())
