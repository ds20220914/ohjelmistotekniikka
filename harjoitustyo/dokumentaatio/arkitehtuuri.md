# Arkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on kolmetasoista kerrosarkitehtuuria, koodin pakkausrakenne on seuraava:
![image](https://user-images.githubusercontent.com/123125841/232858513-9cde1e88-860d-4e3c-b81d-42232314dd61.png)

Pakkaus ui sisältää koodeja käyttöliitymästä, pakkaus repository sisältää koodeja tietokannan muokkaamisesta(esim. tiedon lisääminen,etsiminen),
pakkaus service sisältää opintoseurantajärjestelmän sovelluslogiikka ja palveluja, pakkaus entities sisältää luokat, jotka kuvastavat eri käyttäjäosapuolet.

## Käyttöliittymä

Käyttöliittymä sisältää 4 erilaista näkymää

- Kirjautuminen
- Opiskelija näkee omat suoritukset
- Opettaja lisää opiskelijalle suoritukset
- Opettaja tarkistaa tietyn opiskelijan suoritukset

Näkymistä yksi on aina kerrallaan näkyvänä.Näkymien näyttämisestä vastaa UI-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. 
Se kutsuu studyMonitoring_services.py:n Services-luokan metodeja sekä CourseRepository ja UserRepository luokan metodeja.

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat User ja Course, jotka kuvaavat käyttäjiä ja käyttäjien kursseja. 
Käyttäjän rooli voi olla joko opiskelija tai opettaja sen käyttäjänimen mukaan. 

![image](https://user-images.githubusercontent.com/123125841/232853146-d382fe93-52f0-49f0-8166-0c89283995e9.png)


Toiminnallisista kokonaisuuksista vastaa Services-luokka. Luokka tarjoaa käyttäjäliittymän toiminnolla oma metodi:
- login(username,password)
- new_user(name, password, role_number)
- find_by_rolenumber(rolenumber)
- find_by_coursename_rolenumber(rolenumber, course_name)
- login(self, username, password)
- add_new_course(self, rolenumber, course)
- average_grade(self, username)
- show_diagram(self,username)
-  credit_sum(self, username)
-  delete_course(self,name,rolenumber)

Services pysty hyödyntää käyttäjien ja kurssisuorituksien tietoja niiden tallennuksesta vastaavan pakkauksessa repositories sijaitsevien luokkien UserRepository ja CourseRepository kautta.

![image](https://user-images.githubusercontent.com/123125841/232852927-8929ff2e-c666-4fd2-9dc6-5b5e449fee65.png)

## Tietojen pysyväistallennus

Pakkauksen "repository" luokat UserRepository ha CourseRepository hoitavat tietojen talletamista ja etsimistä. UserRepository-luokka käsittelee käyttäjätunnusta, salasanaa ja rolenumberia talletava tietokanta, ja CourseRepository-luokka käsittelee kurssisuoritusta talletava tietokanta.  

### Tiedostot

Sovellus talletaa suoritustiedot ja käyttäjientiedot erillisiin tiedostoihin. Tiedostojen nimet määrittelee .env tiedosto.

## Päätoiminnallisuudet 

Seuraavaksi kuvataan ohjelman päätoiminnallisuudet sekvenssikaavion avulla. 

### Käyttäjän kirjaantuminen

Kirjautumisnäkymän syötekenttiin syötetään käyttäjätunnus ja salasana, ja sitten klikataan "login" painike. 
Sen jälkeen ohjelma toimii seuraavasti:
![IMG_20230424_042237_edit_636331484921267](https://user-images.githubusercontent.com/123125841/233883137-539f8768-dede-4a1a-8617-4e2f96e94de8.jpg)
![IMG_20230424_042247_edit_636342987711419](https://user-images.githubusercontent.com/123125841/233883177-e7c84130-0f1c-45c0-9e8f-0442eecf01ed.jpg)


Kun käyttäjä on painanut "login" painike, ohjelma kutsuu sovelluslogiikan Services metodia login ja antaa parametriksi käyttäjätunnus ja salasana. Sen jälkeen sovelluslogiikka kutsuu UserRepository, ja sen avulla selvittää onko käyttäjätunnus ja salasana oikea. 
Jos salasana ja käyttäjätunnus on oikea, sitten UserRepository määrittää käyttäjätunnuksen perusteella, että onko käyttäjä "opettaja" vai "oppilas".
Ja sitten sen perusteella käyttöliittymä antaa joko TeacherView eli "opettajan" näkymä tai StudentView eli "oppilaiden" näkymä. 

### Uuden käyttäjän luominen

Kun käyttäjä painaa "Register"-painike uuden käyttäjän luomisnäkymässä, ohjelma toimii seuraavasti:
![IMG_20230424_042343_edit_636399330713845](https://user-images.githubusercontent.com/123125841/234088976-5a853ee9-7524-4715-bd24-0e69a2313f57.jpg)

Tapahtumakäsittelijä kutsuu UserRepository, ja selvittää sen find_all metodin avulla, onko käyttäjänimi jo olemassa. Jos ei ole, niin tapahtumakäsittelijä kutsuu
sovelluslogiikan metodia new_user, joka kutsuu UserRepository:n metodi create, ja sen avulla tallentaa uuden käyttäjän käyttäjätunnus, salasana ja rolenumber. Jos uuden käyttäjän luonti onnistuu, ohjelma palaa automaattisesti kirjautumisnäkymään, jos luominen ei onnistu, ohjelma ilmoittaa error viesti. 

### Kurssisuorituksen lisääminen

"Oppilaiden" kurssisuorituksen lisääminen onnistuu ainoastaan "opettajilla". Suorituksen lisämisnäkymä pääsee klikkaamalla "add new course". 
Kun "opettajat" ovat täydentänyt "oppilaan" rolenumber ja suoritustiedot, klikkaamalla "add course performance" sovelluksen kontrolli toimii seuraavasti:
![Kuvakaappaus - 2023-04-24 21-52-24](https://user-images.githubusercontent.com/123125841/234089236-ea016dda-8e3b-41c8-aa68-3fc9d3807182.png)


Tapahtumakäsittelijä kutsuu sovelluslogiikan metodi find_by_coursename_rolenumber, joka kutsuu CourseRepository:n metodi find_all_course_by_student_rolenumber ja palauttaa lista kyseisen oppilaan suoritustiedoista. Jos tämä uusi suoritustieto ei ole listassa, niin tapahtumakäsittelijä kutsuu sovelluslogiikasta add_new_course joka taas kutsuu CourseRepository:sta metodi create_course, joka lisää kyseisen oppilaan suoritustieto tietokantaan.  

### Kurssisuorituksen poistaminen

"Oppilaiden" kurssisuorituksen poistaminen onnistuu ainoastaan "opettajilla". Suorituksen poistaminen onnistuu etsimällä kyseisen opiskelijan suoritukset ja painamalla "search".
Kun "opettajat" ovat löytänyt kyseisen opiskelijan kaikki suoritustiedot, laitamalla suorituksen nimi ja painamalla "delete by coursename" niin poistaminen onnistuu:
![image](https://github.com/ds20220914/ohjelmistotekniikka/assets/123125841/1f7339e1-a2ab-41b8-b7eb-14c20bdb6208)

Tapahtumakäsittelijä kutsuu sovelluslogiikan metodi delete_course, joka kutuu CourseRepository:n metodi delete_course, joka poistaa kyseisen suoritus kyseisestä opiskelijasta, jos suoritus on olemassa. 
