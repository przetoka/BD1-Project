ALTER TABLE sklep.pracownik ADD CONSTRAINT pracownik_sklep
FOREIGN KEY (id_sklep) REFERENCES sklep.sklep (id_sklep);
ALTER TABLE sklep.pracownik ADD CONSTRAINT pracownik_magazyn
FOREIGN KEY (id_magazyn) REFERENCES sklep.magazyn (id_magazyn);

ALTER TABLE sklep.produkty_na_stanie ADD CONSTRAINT produkty_na_stanie_sklep
FOREIGN KEY (id_sklep) REFERENCES sklep.sklep (id_sklep);
ALTER TABLE sklep.produkty_na_stanie ADD CONSTRAINT produkty_na_stanie_magazyn
FOREIGN KEY (id_magazyn) REFERENCES sklep.magazyn (id_magazyn);
ALTER TABLE sklep.produkty_na_stanie ADD CONSTRAINT produkty_na_stanie_produkt
FOREIGN KEY (id_produkt) REFERENCES sklep.produkt (id_produkt);

ALTER TABLE sklep.zamowienie_produkty ADD CONSTRAINT zamowienie_produkty_produkt
FOREIGN KEY (id_produkt) REFERENCES sklep.produkt (id_produkt);
ALTER TABLE sklep.zamowienie_produkty ADD CONSTRAINT zamowienie_produkty_zamowienie
FOREIGN KEY (id_zamowienie) REFERENCES sklep.zamowienie (id_zamowienie);

ALTER TABLE sklep.zamowienie ADD CONSTRAINT zamowienie_klient
FOREIGN KEY (id_klient) REFERENCES sklep.klient (id_klient);
ALTER TABLE sklep.zamowienie ADD CONSTRAINT zamowienie_pracownik
FOREIGN KEY (id_pracownik) REFERENCES sklep.pracownik (id_pracownik);