.open --new

CREATE TABLE nouns AS
    SELECT "the dog" AS phrase UNION
    SELECT "the cat"           UNION
    SELECT "the bird";

SELECT subject.phrase || " chased " || object.phrase
    FROM nouns AS subject, nouns AS object
    WHERE subject.phrase != object.phrase;

CREATE TABLE ands AS
    SELECT phrase FROM nouns UNION
    SELECT first.phrase || " AND " || second.phrase
        FROM nouns AS first, nouns AS second
        WHERE first.phrase != second.phrase;

SELECT subject.phrase || " chased " || object.phrase
    FROM ands AS subject, ands AS object
    WHERE subject.phrase != object.phrase;
