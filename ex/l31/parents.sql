.open --new

-- Parents
create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

-- Children of Abraham
select child from parents where parent = "abraham";

-- Fillmores
select parent from parents where parent > child;

-- All items
select * from parents;