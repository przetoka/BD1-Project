CREATE SCHEMA sklep;

CREATE TABLE sklep.sklep(
    id_sklep INTEGER NOT NULL,
    miasto VARCHAR(50) NOT NULL,
    ulica VARCHAR(50) NOT NULL,
    kod_pocztowy VARCHAR(50) NOT NULL,
    nr_domu INTEGER NOT NULL,
    nr_mieszkania INTEGER,
    CONSTRAINT sklep_pkey PRIMARY KEY (id_sklep)
);

CREATE TABLE sklep.magazyn(
    id_magazyn INTEGER NOT NULL,
    miasto VARCHAR(50) NOT NULL,
    ulica VARCHAR(50) NOT NULL,
    kod_pocztowy VARCHAR(50) NOT NULL,
    nr_domu INTEGER NOT NULL,
    nr_mieszkania INTEGER,
    CONSTRAINT magazyn_pkey PRIMARY KEY (id_magazyn)
);

CREATE TABLE sklep.pracownik(
    id_pracownik INTEGER NOT NULL,
    imie VARCHAR(50) NOT NULL,
    nazwisko VARCHAR(50) NOT NULL,
    id_sklep INTEGER,
    id_magazyn INTEGER,
    nr_telefonu INTEGER NOT NULL,
    email VARCHAR(50) NOT NULL,
    haslo VARCHAR(50) NOT NULL,
    rola INTEGER NOT NULL,
    CONSTRAINT pracownik_pkey PRIMARY KEY (id_pracownik)
);

CREATE TABLE sklep.produkt(
    id_produkt INTEGER NOT NULL,
    cena FLOAT NOT NULL,
    nazwa VARCHAR NOT NULL,
    opis VARCHAR NOT NULL,
    kategoria VARCHAR NOT NULL, 
    CONSTRAINT produkt_pkey PRIMARY KEY (id_produkt)
);

CREATE TABLE sklep.produkty_na_stanie(
    id_sklep INTEGER,
    id_magazyn INTEGER,
    id_produkt INTEGER NOT NULL,
    ilosc INTEGER NOT NULL
);

CREATE TABLE sklep.zamowienie_produkty(
    id_zamowienie_produkty INTEGER NOT NULL,
    id_zamowienie INTEGER NOT NULL,
    id_produkt INTEGER NOT NULL,
    cena FLOAT NOT NULL,
    ilosc INTEGER NOT NULL,
    CONSTRAINT zamowienie_produkty_pkey PRIMARY KEY (id_zamowienie_produkty)
);

CREATE TABLE sklep.zamowienie(
    id_zamowienie INTEGER NOT NULL,
    id_klient INTEGER NOT NULL,
    cena_dostawy FLOAT NOT NULL,
    data_zlozenia DATE NOT NULL,
    status_zamowienia VARCHAR NOT NULL,
    sposob_platnosci VARCHAR(50) NOT NULL,
    status_platnosci VARCHAR(50) NOT NULL,
    id_pracownik INTEGER NOT NULL,
    CONSTRAINT zamowienie_pkey PRIMARY KEY (id_zamowienie)
);

CREATE TABLE sklep.klient(
    id_klient INTEGER NOT NULL,
    imie VARCHAR(50) NOT NULL,
    nazwisko VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    nr_telefonu INTEGER NOT NULL,
    miasto VARCHAR(50) NOT NULL,
    ulica VARCHAR(50) NOT NULL,
    kod_pocztowy VARCHAR(50) NOT NULL,
    nr_domu INTEGER NOT NULL,
    nr_mieszkania INTEGER,
    CONSTRAINT klient_pkey PRIMARY KEY (id_klient)
);
