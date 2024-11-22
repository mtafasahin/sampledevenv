CREATE DATABASE mtafasahindb;
CREATE USER mtafasahin WITH PASSWORD 'mypassword';
ALTER ROLE mtafasahin SET client_encoding TO 'utf8';
ALTER ROLE mtafasahin SET default_transaction_isolation TO 'read committed';
ALTER ROLE mtafasahin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE mtafasahindb TO mtafasahin;
