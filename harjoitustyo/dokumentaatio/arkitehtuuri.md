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
Services pysty hyödyntää käyttäjien ja kurssisuorituksien tietoja niiden tallennuksesta vastaavan pakkauksessa repositories sijaitsevien luokkien UserRepository ja CourseRepository kautta.

![image](https://user-images.githubusercontent.com/123125841/232852927-8929ff2e-c666-4fd2-9dc6-5b5e449fee65.png)
