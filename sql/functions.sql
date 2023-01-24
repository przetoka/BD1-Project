-- generuje losowy numer telefonu
CREATE OR REPLACE FUNCTION numer_telefonu()
RETURNS integer
    AS 'SELECT trunc(random() * 899999999 + 100000000)::int;'
LANGUAGE SQL;

-- generuje email
CREATE OR REPLACE FUNCTION email(imie text, nazwisko text)
RETURNS text
    AS $$ 
        SELECT $1 || $2 || '@mail.pl';
    $$
LANGUAGE SQL;