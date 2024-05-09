.open --new

------------
-- Cities --
------------

CREATE TABLE cities AS
    SELECT 38 AS latitude, 122 AS longitude, "Berkeley" AS name UNION
    SELECT 42,              71,              "Cambridge"        UNION
    SELECT 45,              93,              "Minneapolis"      UNION
    SELECT 33,             117,              "San Diego"        UNION
    SELECT 26,              80,              "Miami"            UNION
    SELECT 90,               0,              "North Pole";

CREATE TABLE cold AS
    SELECT name FROM cities WHERE latitude > 43 UNION
    SELECT "Chicago";

SELECT name, "is cold!" FROM cold;

CREATE TABLE distances AS
    SELECT a.name AS first, b.name AS second,
        60*(a.latitude-b.latitude) AS distance
        FROM cities AS a, cities AS b
        WHERE a.name != b.name
        ORDER BY a.longitude;

SELECT second FROM distances WHERE first="Minneapolis" ORDER BY -distance;