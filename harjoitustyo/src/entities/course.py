class Course:
    ''' luokka, jonka avulla määritellään kurssien kurssitiedot
        Attribuutit: 
           course_name:kurssin nimi
           course_credits: kurssin opintopiste
           grade: kurssin arvosana
    '''

    def __init__(self, course_name, course_credits, grade=None):
        self.course_name = course_name
        self.credits = course_credits
        self.grade = grade
