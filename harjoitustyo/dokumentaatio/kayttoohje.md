# Käyttöohje

Lataa projektin viimeisimmän [releasen]() lähdekoodi valitsemalla Assets-osion alta Source code.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

*poetry install*

Jonka jälkeen suorita alustustoimenpiteet komennolla:

*poetry run invoke build*

Nyt ohjelman voi käynnistää komennolla:

*poetry run invoke start*

## Kirjautuminen

Sovellus käynnistyy kirjautumisnäkymään:

Jos käyttäjätunnus ja salasana ovat olemassa, paina "Login" ja kirjautuminen onnistuu.

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on myös mahdollista siirtyä käyttäjän luomisnäkymään painamalla "Register".

Uusi käyttäjä luodaan syöttämällä ohjeen mukaan oikeita tietoja syötekenttiin ja painamalla "Register".

Jos luominen onnistuu, siirrytään kirjautumisnäkymään. 

## Suorituksen lisääminen opiskelijalle sekä opiskelijan suorituksien tarkistaminen (opettajat)

Kun "opettaja" on onnistunut kirjautumaan sisään, hän voi lisätä tietylle opiskelijalle suorituksia. 
Painamalla "Add new course" "opettaja" siirtyy suorituksen lisäämisnäkymään. 

Kun "opettaja" on täytänyt suoritustiedot sekä suorittajan opiskelijanumero, painamalla "Add new course" suoritus tallentuu tietokantaan. 

Kun "opettaja" on kirjautunut sisään, hän voi myös tarkista tietyn opiskelijan kaikki suoritustiedot, täytämällä opiskelijanumero ja painalla "search".

## Oman suorituksen näkeminen 

Kun "opiskelija" on onnistunut kirjautumaan sisään, hän näkee kaikki hänen suoritustiedot, keskiarvo sekä opintopisteiden summa. 


## Ulos kirjautuminen

Ulos kirjautuminen onnistuu painamalla "logout".  
