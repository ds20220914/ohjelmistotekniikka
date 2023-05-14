# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/ds20220914/ohjelmistotekniikka/releases/tag/viikko5) lähdekoodi valitsemalla Assets-osion alta Source code.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

*poetry install*

Jonka jälkeen suorita alustustoimenpiteet komennolla:

*poetry run invoke build*

Nyt ohjelman voi käynnistää komennolla:

*poetry run invoke start*

## Kirjautuminen

Sovellus käynnistyy kirjautumisnäkymään:
![Kuvakaappaus - 2023-05-02 20-35-08](https://user-images.githubusercontent.com/123125841/235743403-04893fce-fc96-48d2-a80f-22338ceb2814.png)

Jos käyttäjätunnus ja salasana ovat olemassa, paina "Login" ja kirjautuminen onnistuu.

## Uuden käyttäjän luominen

Kirjautumisnäkymästä on myös mahdollista siirtyä käyttäjän luomisnäkymään painamalla "Register".
![Kuvakaappaus - 2023-05-02 20-36-00](https://user-images.githubusercontent.com/123125841/235743560-051d6319-6a1b-4b51-b0d0-b6619948357a.png)
![Kuvakaappaus - 2023-05-02 20-36-26](https://user-images.githubusercontent.com/123125841/235743681-586c1925-d251-4221-9e35-6d6f04a31145.png)

Uusi käyttäjä luodaan syöttämällä ohjeen mukaan oikeita tietoja syötekenttiin ja painamalla "Register".
(Role number eli roolinumero on sinun opiskelijanumero tai opettajanumero)
Jos luominen onnistuu, siirrytään kirjautumisnäkymään. 

## Suorituksen lisääminen opiskelijalle sekä opiskelijan suorituksien tarkistaminen (opettajat)

Kun "opettaja" on onnistunut kirjautumaan sisään, hän voi lisätä tietylle opiskelijalle suorituksia. 
Painamalla "Add new course" "opettaja" siirtyy suorituksen lisäämisnäkymään. 
![Kuvakaappaus - 2023-05-02 20-49-26](https://user-images.githubusercontent.com/123125841/235744888-20d8987c-4a27-49cf-91b3-1f492661f5cf.png)

Kun "opettaja" on täytänyt suoritustiedot sekä suorittajan opiskelijanumero, painamalla "Add course performance" suoritus tallentuu tietokantaan. 
![Kuvakaappaus - 2023-05-02 20-39-03](https://user-images.githubusercontent.com/123125841/235744244-dc722656-af60-4870-9287-ab75927160e9.png)

Kun "opettaja" on kirjautunut sisään, hän voi myös tarkista tietyn opiskelijan kaikki suoritustiedot, täytämällä opiskelijanumero ja painalla "search".
![Kuvakaappaus - 2023-05-02 20-38-05](https://user-images.githubusercontent.com/123125841/235744044-bf12a76f-9b02-4faf-8b94-d5f5b90669f0.png)
![Kuvakaappaus - 2023-05-02 20-39-46](https://user-images.githubusercontent.com/123125841/235744464-fc9d820a-20e9-4c48-a4a0-e373fd29c799.png)

## Oman suorituksen näkeminen 

Kun "opiskelija" on onnistunut kirjautumaan sisään, hän näkee kaikki hänen suoritustiedot, keskiarvo sekä opintopisteiden summa. 
![Kuvakaappaus - 2023-05-02 20-41-00](https://user-images.githubusercontent.com/123125841/235744626-59ebefd4-267c-4ee5-8b30-dd4dad62255f.png)

## oman suorituksen diagrammi
![image](https://github.com/ds20220914/ohjelmistotekniikka/assets/123125841/8d2df9f0-f02b-4e97-abcf-fe97230cb129)
Opiskelija näkee myös oman suorituksien keskiarvon diagrammi painamalle "show average grade diagram".


## Ulos kirjautuminen

Ulos kirjautuminen onnistuu painamalla "logout".  
