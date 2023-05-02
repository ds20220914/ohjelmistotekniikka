# Studentmonitoring-App (opintoseuranta järjestelmä)

Sovelluksen avulla käyttäjien on mahdollista ylläpitää kurssien suoritustiedot. 
Sovellusta voi käyttää monta käyttäjää, ja kaikilla on oma rooli käyttäjätunnuksen perusteella.
Rooleja on "oppilas" ja "opettaja".



### Dokumentaatio

[Vaatimusmäärittely](https://github.com/ds20220914/ohjelmistotekniikka/blob/main/harjoitustyo/dokumentaatio/vaatimusmaarittely.md)

[Tunti/työaikakirjanpito](https://github.com/ds20220914/ohjelmistotekniikka/blob/main/harjoitustyo/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/ds20220914/ohjelmistotekniikka/blob/main/harjoitustyo/dokumentaatio/changelog.md)

[arkitehtuuri](https://github.com/ds20220914/ohjelmistotekniikka/blob/main/harjoitustyo/dokumentaatio/arkitehtuuri.md)

[Releasit](https://github.com/ds20220914/ohjelmistotekniikka/releases)

[Käyttöohje](https://github.com/ds20220914/ohjelmistotekniikka/blob/main/harjoitustyo/dokumentaatio/kayttoohje.md)

# Asennus

### 1. Asenna riippuvuuden komennolla harjoitustyo-alihakemistossa:

*poetry install*

### 2. Tietokannan alustustoimenpiteet harjoitustyo-alihakemistossa:

*poetry run invoke build*

### 3. Käynnistä sovellus harjoitustyo-alihakemistossa:

*poetry run invoke start* 

# Komentorivitoiminnot

## Ohjelman suorittaminen

### Ohjelman pystyy suorittamaan komennolla:

*poetry run invoke start*

## Testaus

### Testit suoritetaan komennolla:

*poetry run invoke test*

## Testikattavuus

### Testikattavuusraportin voi generoida komennolla:

*poetry run invoke coverage-report*

### Raportti generoituu htmlcov-hakemistoon

## pylint

### Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

*poetry run invoke lint*
