# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus ylläpitää opiskelijoiden opiskelusuorituksia. Sovelluksen käyttäjät ovat opiskelijoita ja opettajia. 
Kirjautumalla omalle tilille opiskelijat voivat nähdä kaikki suoritetut kurssit sekä opintopisteiden summan ja keskiarvon. 
Opettajat voivat muokata opiskelijoiden kurssien tiloja sekä antaa opiskelijoille arvosanan kurssista.

## Käyttäjät

Opiskelijat ovat sovelluksen normaaleja käyttäjiä. Ja opettajat ovat pääkäyttäjiä, joilla on suurempia oikeuksia. 

## Käyttöliittymäluonnos

![](https://github.com/ds20220914/ohjelmistotekniikka/blob/main/harjoitustyo/dokumentaatio/kuvat/Kuvakaappaus%20-%202023-03-23%2003-08-53.png)

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

- Opiskelijat eli normaalit käyttäjät näkevät omat suoritustiedot
  - Painamalla "setting" normaalit käyttäjät pääsevät näkemään oman käyttäjätiedon. 
- Opettajat eli pääkäyttäjät voivat etsiä opiskelijanumeron avulla tietyn opiskelijan suoritustiedot ja muokkaa
  niitä(uuden kurssin lisääminen, kurssin arvosanan antaaminen). "tehty"
  - Painamalla "setting" pääkäyttäjät pääsevät näkemään oman käyttäjätiedon. 
- käyttäjät voivat kirjautua ulos painamalla ensin "setting" ja sitten "logout". 
