ALTER TABLE sklep.sklep ADD CHECK (kod_pocztowy ~'[0-9]{2}-[0-9]{3}');

ALTER TABLE sklep.magazyn ADD CHECK (kod_pocztowy ~'[0-9]{2}-[0-9]{3}');

ALTER TABLE sklep.pracownik ADD CHECK (nr_telefonu < 1000000000 AND nr_telefonu >= 100000000);
ALTER TABLE sklep.pracownik ADD CHECK((rola < 3 AND id_sklep IS NOT NULL AND id_magazyn IS NULL)
    OR (rola > 2  AND id_sklep IS NULL AND id_magazyn IS NOT NULL));
ALTER TABLE sklep.pracownik ADD CHECK (email ~'^([a-zA-Z0-9_\-]+\.)*[a-zA-Z0-9_\-]+@([a-zA-Z0-9_\-]+\.)+(com|org|edu|net|ca|au|coop|de|ee|es|fm|fr|gr|ie|in|it|jp|me|pl|nl|nu|ru|uk|us|za)$');
ALTER TABLE sklep.pracownik ADD CHECK(rola < 5 AND rola > 0);

ALTER TABLE sklep.klient ADD CHECK (nr_telefonu < 1000000000 AND nr_telefonu >= 100000000);
ALTER TABLE sklep.klient ADD CHECK (kod_pocztowy ~'[0-9]{2}-[0-9]{3}');
ALTER TABLE sklep.klient ADD CHECK (email ~'^([a-zA-Z0-9_\-]+\.)*[a-zA-Z0-9_\-]+@([a-zA-Z0-9_\-]+\.)+(com|org|edu|net|ca|au|coop|de|ee|es|fm|fr|gr|ie|in|it|jp|me|pl|nl|nu|ru|uk|us|za)$');

