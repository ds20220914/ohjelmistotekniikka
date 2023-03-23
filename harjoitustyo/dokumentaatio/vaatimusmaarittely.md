# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus ylläpitää opiskelijoiden opiskelusuorituksia. Sovelluksen käyttäjät ovat opiskelijoita ja opettajia. 
Kirjautumalla omalle tilille opiskelijat voivat nähdä kaikki suoritetut kurssit sekä opintopisteiden summa ja keskiarvo. 
Opettajat voivat muokata opiskelijoiden kurssien tilat sekä antaa opiskelijoille arvosana kurssista.

## Käyttäjät

Opiskelijat ovat sovelluksen normaalia käyttäjiä. Ja opettajat ovat pääkäyttäjiä, joilla on suurempia oikeuksia. 

## Käyttöliittymäluonnos

![](https://github.com/ds20220914/ohjelmistotekniikka/blob/main/harjoitustyo/dokumentaatio/kuvat/Kuvakaappaus%20-%202023-03-23%2002-22-05.png)

Kun sovellus käynnistetään, kirjautumisnäkymä tulee esille. Käyttäjät voivat siirtyä joko käyttäjän luomisnäkymään 
tai kirjautua sisään. Kun opiskelijat ovat kirjautunut sisään, ne siirtyvät niiden suorituskokoelmaan joka sisältää
kurssilista sekä opintopisteet ja keskiarvo. Kun opettajat ovat kirjautunut sisään, ne siirtyvät hakunäkymään ja
opiskelijan numeron avulla opiskelijan suorituskokoelman muokkausnäkumään. 

käyttäjät voivat myös siirtyä setting-näkymään kun on kirjautunut sisään ja kirjautua ulos sielä. 
 
## Toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi luoda uuden käyttäjätunnus järjestelmään
  - Käyttäjätunnus täytyy olla uniikki
  - Samalla pitää keksiä salasana ja antaa oman opiskelijanumeron
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen onnistuu syöttämällä oikea käyttäjätunnus ja salasana 
  - Jos salasana tai käyttäjätunnus on väärin, kijautuminen epäonnistuu ja tästä ilmoitetaan järjestelmälle

### Kirjautumisen jälkeen

- Opiskelijat eli normaalit käyttäjät näkevät omat suoritustiedot
  - Painamalla "setting" normaalit käyttäjät pääsevät näkemään oman käyttäjätiedon. 
- Opettajat eli pääkäyttäjät voivat etsiä opiskelijanumeron avulla tietyn opiskelijan suoritustiedot ja muokkaa
  niitä(uuden kurssin lisääminen, kurssin arvosanan antaaminen). 
  - Painamalla "setting" pääkäyttäjät pääsevät näkemään oman käyttäjätiedon. 
- käyttäjät voivat kirjautua ulos painamalla ensin "setting" ja sitten "logout". 
