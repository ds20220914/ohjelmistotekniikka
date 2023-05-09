from database_initialization import initialize_database


def build():
    ''' alustaa tietokannat
    ''' 
    initialize_database()

'''tämä avulla voi komentorivilla kutsua build()'''
if __name__ == "__main__":
    build()
