-- 2.1
SELECT name FROM records WHERE supervisor = "Oliver Warbucks";

-- 2.2
SELECT name FROM records WHERE supervisor = name;

-- 2.3
SELECT name FROM records WHERE salary > 50000 ORDER BY name;

-- 3.1
SELECT day, time
FROM records AS r, meetings AS m
WHERE r.supervisor = "Oliver Warbucks" AND r.division = m.division;

-- 3.2
SELECT f_r.name, s_r.name
FROM records AS f_r, records AS s_r, meetings AS f_m, meetings AS s_m
WHERE f_r.division = f_m.division AND
      s_r.division = s_m.division AND
      f_m.time = s_m.time AND
      f_m.day = s_m.day AND
      f_r.name < s_r.name;

-- 3.3
-- YES!

-- 3.4
SELECT e.name FROM records AS e, records AS s WHERE e.supervisor = s.name AND e.division <> s.division;

-- 4.1
SELECT SUM(salary) FROM records GROUP BY supervisor;

-- 4.2
SELECT day FROM records, meetings WHERE records.division = meetings.division GROUP BY day HAVING COUNT(*) < 5;

-- 4.3
SELECT name, division FROM records WHERE salary < 100000 GROUP BY division HAVING COUNT(*) > 1;

-- 5.1
CREATE TABLE num_taught AS
  SELECT professor, course, COUNT(*) AS times FROM courses GROUP BY professor, course;

-- 5.2
SELECT f.professor, s.professor, f.course
FROM num_taught AS f, num_taught AS s
WHERE f.course = s.course AND f.times = s.times AND f.professor < s.professor;

-- 5.3
SELECT f.professor, s.professor
FROM courses AS f, courses AS s
WHERE f.course = s.course AND f.semester = s.semester AND f.professor < s.professor
GROUP BY f.course, f.semester
HAVING COUNT(*) > 1;
