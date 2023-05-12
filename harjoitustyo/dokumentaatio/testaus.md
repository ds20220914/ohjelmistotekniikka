# Testausdokumentti

Ohjelmaa on testattu sekä automatisoiduin yksikkö- ja integraatiotestein unittestilla sekä manuaalisesti tapahtunein järjestelmätason testein.

## Yksikkö- ja integraatiotestaus

Testeille on käytössä omia tietokantoja.

### Sovelluslogiikka

Sovelluslogiikasta vastaava Services-luokka testataan TestService-testiluokalla. 

### Repositorio-luokat

Repositorio-luokkia UserRepository ja CourseRepository testataan ainostaan testeissä käytössäolevilla tiedostoilla.
Tiedostojen nimet on konfiguroitu .env.test-tiedostoon. UserRepository-luokkaa testataan TestUserRepository-testiluokalla ja CourseRepository-luokkaa TestCourseRepository-testiluokalla.

### Testikattavuus

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 99%

Testaamatta jäivät build.py- ja config.py-tiedostojen suorittaminen komentoriviltä. Nämä olisi myös voinut jättää testikattavuuden ulkopuolelle. 

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu käyttöohjeen kuvaamalla tavalla sekä macOS- että Linux-ympäristöön. 

Sovellusta on testattu sekä tilanteissa, joissa käyttäjät ja kurssisuoritukset tallettavat tiedostot ovat olleet olemassa ja joissa niitä ei ole ollut jolloin ohjelma on luonut ne itse.

### Toiminnallisuudet

Kaikki määrittelydokumentin ja käyttöohjeen listaamat toiminnallisuudet on käyty läpi. Kaikki toiminnallisuudet ovat myös testattu virheellisillä arvoilla.

## Sovellukseen jääneet laatuongelmat

Tällä hetkellä sovellus ei anna virheilmoituksia seuraavissa tilanteissa:

- SQLite tietokantaa ei ole alustettu, eli poetry run invoke build-komentoa ei ole suoritettu komentorivillä.
- Konfiguraation määrittelemiin tiedostoihin ei ole luku/kirjoitusoikeuksia
