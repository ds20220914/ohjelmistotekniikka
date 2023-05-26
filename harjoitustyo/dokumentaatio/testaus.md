# Testausdokumentti

Ohjelmaa on testattu sekä automatisoitusti unittestilla yksikkö- ja integraatiotestin avulla että manuaalisesti järjestelmätason testin avulla eli syötämällä syötekenttiin erilaisia arvoja. 

## Yksikkö- ja integraatiotestaus

Testeille on käytössä omia tietokantoja.

### Sovelluslogiikka

Sovelluslogiikasta vastaava Services-luokka testataan TestService-testiluokalla. 

### Repositorio-luokat

Repositorio-luokkillä UserRepositoryllä ja CourseRepositoryllä on käytössä oma testitiedosto, joka on tarkoitettu ainoastaan testeihin. 
Testitiedostojen nimet ovat määritetty .env.test-tiedostossa. UserRepository-luokan testaamisessa käytetään tests-kansiossa oleva user_repository_test.py-tiedostossa oleva TestUserRepository-testiluokka ja CourseRepository-luokan testaamisessa käytetään tests-kansiossa oleva course_repository_test.py-tiedostossa oleva TestCourseRepository-testiluokka.

### Testikattavuus

Ohjelman testauksen haarautumiskattavuus on 99%. Käyttöliittymää oli kuitenkin jätetty testien ulkopuolelle.
![image](https://github.com/ds20220914/ohjelmistotekniikka/assets/123125841/c0ee8475-6997-4faf-8ae3-49fc3fce3b0f)

Testaamatta jäivät build.py- ja config.py-tiedostojen suorittaminen komentoriviltä. Nämä olisi myös voinut jättää testikattavuuden ulkopuolelle. 

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti syötämällä syötekenttiin erilaisia arvoja.

### Asennus ja konfigurointi

Sovellus on haettu ja testattu sekä macOS- että Linux-ympäristössä, sitä on haettu ja testattu käyttöohjeen kuvaamalla tavalla.

Testaus on suoritettu niin, että jos käyttäjät ja kurssisuoritukset tallettavat tiedostot ovat olleet olemassa, niin talletus suoritetaan niihin, ja jos niitä eivät ole ollut, niin ohjelma luo ne itse.  

### Toiminnallisuudet

Kaikki määrittelydokumentissa ja käyttöohjessa mainitut toiminnallisuudet ovat käyty läpi. Kaikki toiminnallisuudet ovat myös testtu virheellisillä arvoilla unittestin avulla. 

## Sovellukseen jääneet laatuongelmat

Sovellus ei tällä hetkellä ilmoita virheitä seuraavissa tilanteissa:

- SQLite-tietokantaa ei ole alustettu, mikä tarkoittaa sitä, että poetry run invoke build -komentoa ei ole suoritettu komentorivillä.
- Konfiguraation määrittelemiin tiedostoihin ei ole myönnetty luku- tai kirjoitusoikeuksia.

