-- Parents of curly dogs
SELECT parent FROM parents, dogs WHERE child = name AND fur = "curly";

-- Siblings
SELECT a.child AS first, b.child AS second
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child;

-- Grandparents
CREATE TABLE grandparents AS
  SELECT a.parent AS grandog, b.child AS granpup
    FROM parents AS a, parents AS b
    WHERE b.parent = a.child;

-- Grandogs with the same fur AS their granpups

-- My solution
SELECT a.parent AS grandog, b.child AS granpup, a_dog.fur
    FROM parents AS a, parents AS b, dogs AS a_dog, dogs AS b_dog
    WHERE a.child = b.parent
        AND a.parent = a_dog.name
        AND b.child = b_dog.name
        AND a_dog.fur = b_dog.fur;

-- class solution
SELECT grandog, granpup, c.fur FROM grandparents, dogs AS c, dogs AS d
  WHERE grandog = c.name AND
        granpup = d.name AND
        c.fur = d.fur;