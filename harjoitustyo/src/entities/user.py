class User:
    '''luokka, jonka avulla määritellään käyttäjien käyttäjätiedot
       Attribuutit:
           username:käyttäjän käyttäjänimi
           password: käyttäjän salasana
           number: roolinumero, eli opiskelijanumero tai opettajanumero
    '''
    def __init__(self, username, password, number):
        self.username = username
        self.password = password
        self.role_number = number
