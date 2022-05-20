1. Is the students table directly related to the courses table? Why or why not?
The tables are not directly related, but they do overlap in the student_enrollement table.

<!--   --------------------------------------------------------------------------------- -->

2. Using subqueries only, write a SQL statement that returns the names of those students that are taking the courses Physics and US History.

SELECT student_name
FROM students 
WHERE student_no 
IN (SELECT student_no FROM student_enrollment WHERE course_no 
IN (SELECT course_no FROM courses WHERE course_title 
IN ('Physics', 'US History')));

<!--   --------------------------------------------------------------------------------- -->

3. Using subqueries only, write a query that returns the name of the student that is taking the highest number of courses.

SELECT student_name 
FROM students
WHERE student_no
IN (SELECT student_no 
FROM (SELECT student_no, COUNT(course_no) AS course_cnt
FROM STUDENT_ENROLLMENT
GROUP BY student_no
ORDER BY course_cnt DESC 
LIMIT 1) AS a 
)

<!--   --------------------------------------------------------------------------------- -->

4. Subqueries can be used in the FROM clause and the WHERE clause but cannot be used in the SELECT Clause.

False, subqueries can be used is the FROM, WHERE, SELECT, and HAVING clause.

<!--   --------------------------------------------------------------------------------- -->

5. Write a query to find the student that is the oldest. You are not allowed to use LIMIT or the ORDER BY clause to solve this problem.

SELECT * 
FROM students
WHERE age = (SELECT MAX(age) FROM students)

<!--   --------------------------------------------------------------------------------- -->


