CREATE VIEW pracownicy_sklepow AS (
    SELECT  s.id_sklep as "id sklepu", s.miasto "miasto", s.ulica as "ulica", s.nr_domu as "numer domu",
            s.nr_mieszkania as "numer mieszkania", p.imie as "imie",
            p.nazwisko as "nazwisko", p.email as "email",
            p.nr_telefonu as "numer telefonu",
            CASE p.rola
                WHEN 1 THEN 'kierownik sklepu'
                WHEN 2 THEN 'pracownik sklepu'
            END AS "rola"
            FROM sklep.sklep s 
            JOIN sklep.pracownik p USING (id_sklep) 
);

CREATE VIEW pracownicy_magazynow AS (
    SELECT  m.id_magazyn as "id magazynu", m.miasto "miasto", m.ulica as "ulica", m.nr_domu as "numer domu",
            m.nr_mieszkania as "numer mieszkania", p.imie as "imie",
            p.nazwisko as "nazwisko", p.email as "email",
            p.nr_telefonu as "numer telefonu",
            CASE p.rola
                WHEN 3 THEN 'kierownik magazynu'
                WHEN 4 THEN 'pracownik magazynu'
            END AS "rola"
            FROM sklep.magazyn m
            JOIN sklep.pracownik p USING (id_magazyn) 
);

CREATE VIEW produkty_w_magazynach AS (
    SELECT  p.id_produkt as "id produktu", p.nazwa, pns.ilosc, m.id_magazyn as "id magazynu", m.miasto "miasto", m.ulica as "ulica", m.nr_domu as "numer domu",
            m.nr_mieszkania as "numer mieszkania"
            FROM sklep.produkt p
            JOIN sklep.produkty_na_stanie pns USING(id_produkt)
            JOIN sklep.magazyn m USING(id_magazyn)
            ORDER BY p.id_produkt
);

CREATE VIEW produkty_w_sklepach AS (
    SELECT  p.id_produkt as "id produktu", p.nazwa, pns.ilosc, s.id_sklep as "id sklepu", s.miasto "miasto", s.ulica as "ulica", s.nr_domu as "numer domu",
            s.nr_mieszkania as "numer mieszkania"
            FROM sklep.produkt p
            JOIN sklep.produkty_na_stanie pns USING(id_produkt)
            JOIN sklep.sklep s USING(id_sklep)
            ORDER BY p.id_produkt
);

CREATE VIEW zamowienia_zarys AS (
    SELECT k.id_klient, k.imie, k.nazwisko, wynik.id_zamowienie as "numer zamowienia", wynik.cena as "łączny koszt produktow", z.cena_dostawy, z.status_zamowienia FROM
        (SELECT id_zamowienie, SUM(cena*ilosc) cena
         FROM sklep.zamowienie_produkty 
         GROUP BY id_zamowienie) wynik
         JOIN sklep.zamowienie z ON wynik.id_zamowienie = z.id_zamowienie
         JOIN sklep.klient k USING(id_klient)
         ORDER BY k.id_klient
);

CREATE VIEW zamowienia_produkty AS(
select k.id_klient, k.imie, k.nazwisko, wynik.id_zamowienie, p.nazwa, p.opis, zp.ilosc, zp.cena, wynik.cena_wielu
    FROM
    (SELECT id_zamowienie, id_zamowienie_produkty, SUM(cena*ilosc) cena_wielu
         FROM sklep.zamowienie_produkty 
         GROUP BY id_zamowienie_produkty, id_produkt) wynik
         JOIN sklep.zamowienie z USING(id_zamowienie)
         JOIN sklep.zamowienie_produkty zp on wynik.id_zamowienie_produkty=zp.id_zamowienie_produkty
         JOIN sklep.produkt p USING(id_produkt)
         JOIN sklep.klient k USING(id_klient)
         ORDER BY id_klient, z.id_zamowienie
         );



-- id_klient, imie, nazwisko, ilosc zamowien klienta, najwiecej zamawiany produkt, nazwa produktu, ilosc zamowionego produktu
CREATE VIEW zamowienia_klientow AS(
select wynik_max_ilosc.id_klient, k.imie, k.nazwisko, p.nazwa, p.opis, wynik_max_ilosc.max_ilosc, wynik_ilosc_zamowien.ilosc_zamowien
from(
    select k.id_klient, max(wynik_ilosc_produktu.ilosc_produktu) max_ilosc
    from(
        select z.id_klient, zp.id_produkt, SUM(zp.ilosc) ilosc_produktu
        from sklep.zamowienie_produkty zp
        join sklep.zamowienie z on z.id_zamowienie = zp.id_zamowienie
        group by z.id_klient, zp.id_produkt) wynik_ilosc_produktu
        join sklep.klient k on k.id_klient = wynik_ilosc_produktu.id_klient
        group by k.id_klient) wynik_max_ilosc
        join (
            select id_klient, count(id_klient) ilosc_zamowien
            from sklep.zamowienie
            group by id_klient
        )   wynik_ilosc_zamowien
        on wynik_ilosc_zamowien.id_klient = wynik_max_ilosc.id_klient
        join sklep.klient k on wynik_max_ilosc.id_klient = k.id_klient
        join (
            select z.id_klient, zp.id_produkt, SUM(zp.ilosc) ilosc_produktu
            from sklep.zamowienie_produkty zp
            join sklep.zamowienie z on z.id_zamowienie = zp.id_zamowienie
            group by z.id_klient, zp.id_produkt
        ) wynik_ilosc_produktu on wynik_ilosc_produktu.id_klient = wynik_max_ilosc.id_klient
        join sklep.produkt p on p.id_produkt = wynik_ilosc_produktu.id_produkt
        where wynik_ilosc_produktu.ilosc_produktu = wynik_max_ilosc.max_ilosc
    );
        


