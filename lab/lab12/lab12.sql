.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color="blue" AND pet="dog";

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color="blue" AND pet="dog";


CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest LIMIT 20;


CREATE TABLE matchmaker AS
  SELECT s1.pet, s1.song, s1.color, s2.color
  FROM students AS s1, students AS s2
  WHERE s1.pet = s2.pet AND s1.song = s2.song AND s1.time < s2.time;



CREATE TABLE sevens AS
  SELECT s.seven
  FROM students AS s, numbers AS n
  WHERE s.time = n.time AND s.number = 7 AND n.'7' = 'True';
