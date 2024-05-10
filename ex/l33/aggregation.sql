select max(legs) from animals;

select sum(weight) from animals;

select max(legs - weight) + 5 from animals;

select min(legs), max(weight) from animals where kind <> "t-rex";

select max(legs) + min(weight) from animals;


select count(legs) from animals;

select count(*) from animals;

select count(distinct legs) from animals;


select kind, max(weight) from animals;

select kind, max(legs) from animals;

select kind, avg(weight) from animals;
