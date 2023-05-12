# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus ylläpitää opiskelijoiden opiskelusuorituksia. Sovelluksen käyttäjät ovat opiskelijoita ja opettajia. 
Kirjautumalla omalle tilille opiskelijat voivat nähdä kaikki suoritetut kurssit sekä opintopisteiden summan ja keskiarvon. 
Opettajat voivat tarkistaa tietyn opiskelijan kaikki suoritukset sekä antaa opiskelijoille arvosanan kurssista.

## Käyttäjät

Opiskelijat ovat sovelluksen normaaleja käyttäjiä. Ja opettajat ovat pääkäyttäjiä, joilla on suurempia oikeuksia. 

## Käyttöliittymäluonnos

![](file:///home/shao/Pictures/Kuvakaappaukset/Kuvakaappaus%20-%202023-05-12%2020-09-25.png)

Kun sovellus käynnistetään, kirjautumisnäkymä tulee esille. Käyttäjät voivat siirtyä joko käyttäjän luomisnäkymään 
tai kirjautua sisään. Kun opiskelijat ovat kirjautunut sisään, ne siirtyvät niiden suorituskokoelmaan joka sisältää
kurssilistan sekä opintopisteet ja keskiarvon. Kun opettajat ovat kirjautuneet sisään, ne siirtyvät hakunäkymään ja
opiskelijan numeron avulla opiskelijan suorituskokoelman muokkausnäkymään. 

käyttäjät voivat myös siirtyä setting-näkymään kun on kirjautunut sisään ja kirjautua ulos sielä. 
 
## Toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda uuden käyttäjätunnus järjestelmään "tehty"
  - Käyttäjätunnus täytyy olla uniikki   "tehty"
  - Samalla pitää keksiä salasana ja antaa oman opiskelijanumeron "tehty"
- Käyttäjä voi kirjautua järjestelmään "tehty"
  - Kirjautuminen onnistuu syöttämällä oikea käyttäjätunnus ja salasana "tehty" 
  - Jos salasana tai käyttäjätunnus on väärin, kijautuminen epäonnistuu ja tästä ilmoitetaan järjestelmälle "tehty"

### Kirjautumisen jälkeen

- Opiskelijat eli normaalit käyttäjät näkevät omat suoritustiedot "tehty" 
- Opettajat eli pääkäyttäjät voivat etsiä opiskelijanumeron avulla tietyn opiskelijan suoritustiedot ja muokkaa 
  niitä(uuden kurssin lisääminen, kurssin arvosanan antaaminen). "tehty" 
- käyttäjät voivat kirjautua ulos painamalla  "logout"."tehty" 
- Opettajat voivat poistaa tietyn opiskelijan tiety suoritus. "tehty"
