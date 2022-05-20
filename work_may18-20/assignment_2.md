1. SELECT student_name FROM students WHERE age BETWEEN 18 AND 20; 

2. SELECT * FROM students WHERE student_name like '%ch%'OR student_name like %nd%;

3. SELECT student_name FROM students WHERE (student_name like '%ae%' OR student_name like '%ph%') AND age != 19; (I used the NOT orginally) 

4. SELECT student_name FROM students ORDER BY age DESC;

5. SELECT student_name, age FROM students ORDER BY age DESC LIMIT 4;

6. SELECT * FROM studnets WHERE age <= 20 AND (student_no BETWEEN 3 AND 5 OR student_no = 7) OR (age > 20 AND student_no >=4);