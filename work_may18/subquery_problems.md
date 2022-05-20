<!-- All the employees that work in the United States -->
SELECT * FROM employees
WHERE region_in IN (SELECT region_id FROM regions WHERE country = 'United States')
<!-- --                                  -- -->


<!-- Returns all the employees that work in the kids division AND the dates at which those employees were hired is greater than all of the fire_dtes of employees who work in the maintenance department -->

Select * 
FROM employees
WHERE department = ANY (SELECT department FROM departments WHERE division = 'Kids')
AND hire_date > ALL (SELECT hire_date FROM employees WHERE department = 'Maintenance')

<!--                             -->

<!-- Return 1 data that shows the most recurring salary  -->
SELECT salary FROM (
Select salary, count(*)
FROM employees
GROUP BY salary
ORDER BY count (*) DESC, salary DESC 
LIMIT 1
) AS a

<!--                -->

<!-- Returning multiple names with their unique id -->
SELECT * FROM dupes
WHERE id IN (
	SELECT min(id)
	FROM dupes
	GROUP BY name
)
<!--                -->

<!-- Finding the average, excluding extreme data points -->
SELECT ROUND(AVG(salary))
FROM employees
WHERE salary NOT IN (
    (SELECT MIN(salary) FROM employees),
    (SELECT(MAX(salary) FROM employees)
)