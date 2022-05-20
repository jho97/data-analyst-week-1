<!-- Example -->
SELECT first_name, salary,
CASE 
	WHEN salary < 100000 THEN 'Under paid'
	WHEN salary > 100000 AND salary < 160000 THEN 'Paid well'
	ELSE 'Executive'
END as catergory
FROM employees
ORDER BY salary DESC;

<!-- ------------------------------------------------------------------------------ -->
<!-- Return the number of people that fall under each category -->
SELECT a.category, COUNT(*) FROM (
SELECT first_name, salary,
CASE 
	WHEN salary < 100000 THEN 'Under paid'
	WHEN salary > 100000 AND salary < 160000 THEN 'Paid well'
	ELSE 'Executive'
END as catergory
FROM employees
ORDER BY salary DESC;
) AS a
GROUP BY a.category


<!-- ------------------------------------------------------------------------------ -->
<!-- Making our rows into columns -->
SELECT 
SUM(CASE WHEN salary < 100000 THEN 1 ELSE 0) AS under_paid,
SUM(CASE WHEN salary > 100000 AND salary < 160000 THEN 1 ELSE 0) AS paid_well,
SUM(CASE WHEN salary > 160000 THEN 1 ELSE 0 END) AS executive
FROM employees


<!-- ------------------------------------------------------------------------------ -->

