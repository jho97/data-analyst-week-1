<!-- correlated subqueries pull from the outer query-->
SELECT first_name, salary
FROM employees emp1
WHERE salary > (SELECT round (AVG(salary))
                FROM employees emp2 WHERE emp1.department = emp2.department)