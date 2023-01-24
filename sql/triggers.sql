CREATE OR REPLACE FUNCTION get_products_out_of_magazine() RETURNS TRIGGER AS 
$$
BEGIN
    IF EXISTS(SELECT id_produkt, ilosc FROM sklep.produkty_na_stanie WHERE id_magazyn = 1 AND id_produkt = NEW.id_produkt AND ilosc >= NEW.ilosc)
        THEN UPDATE sklep.produkty_na_stanie SET ilosc = (ilosc-NEW.ilosc) WHERE id_produkt=NEW.id_produkt AND id_magazyn = 1;
        RETURN NEW;
    END IF;
END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER order_products
    BEFORE INSERT OR UPDATE ON sklep.zamowienie_produkty
    FOR EACH ROW
    EXECUTE PROCEDURE get_products_out_of_magazine();

CREATE OR REPLACE FUNCTION 