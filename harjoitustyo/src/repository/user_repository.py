from database_connection import get_database_connection
from database_connection import get_course_connection


class UserRepository:
    ''' luokka joka vastaa käyttäjien tietokannan operaatioita.
        Attribuutit:
            connection1: Tietokantayhteyden Connection-olio(käyttäjätiedon tietokanta)
            connection2: Tietokantayhteyden Connection-olio(kurssitiedon tietokanta)
    '''
    def __init__(self, connection1, connection2):
    '''luokan konstruktori.
       Args:
           connection1: Tietokantayhteyden Connection-olio(käyttäjätiedon tietokanta)
           connection2: Tietokantayhteyden Connection-olio(kurssitiedon tietokanta)
    '''
        self._connection1 = connection1
        self._connection2 = connection2

    def create(self, user):
    '''luoda uusi käyttäjä tietokantaan
       Args:
           user: Tallennettava käyttäjä User-oliona.
       Returns:
           palauttaa user-olio
    '''
        db_connection = self._connection1.cursor()
        db_connection.execute("INSERT INTO User (User_name, password, role_number) "
                              "VALUES (?, ?, ?)",
                              (user.username, user.password, user.role_number))
        self._connection1.commit()
        return user

    def find_all(self):
    '''palauttaa kaikkien käyttäjien tiedot
       Returns:
           palauttaa jokaisen käyttäjän käyttäjätunnus,salasana ja roolinumero tupleina listassa
    '''
        db_connection = self._connection1.cursor()
        lista = db_connection.execute("SELECT * FROM User ").fetchall()
        return list(lista)
    def find_by_username(self,username):
    '''palauttaa käyttäjän käyttäjätunnus, salasana ja roolinumero käyttäjänimen avulla
       Args:
           username:käyttäjän käyttäjätunnus
       Returns:
           palauttaa tuplena käyttäjän käyttäjätunnus, salasana ja roolinumero
    '''
        db_connection = self._connection1.cursor()
        lista = db_connection.execute("SELECT * FROM User WHERE User_name=?",(username,)).fetchall()
        return lista
    def delete_all(self):
    '''poistaa kaikki käyttäjät'''
        cursor = self._connection1.cursor()
        cursor.execute("delete from User")
        self._connection1.commit()


user_repository = UserRepository(
    get_database_connection(), get_course_connection())
