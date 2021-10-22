DROP DATABASE restaurants;
DROP USER restaurantsuser;

CREATE DATABASE restaurants;
CREATE USER restaurantsuser WITH PASSWORD 'restaurants';
GRANT ALL PRIVILEGES ON DATABASE restaurants TO restaurantsuser;