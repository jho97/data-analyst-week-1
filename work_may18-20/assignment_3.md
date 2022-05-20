1. SELECT last_name || ' ' || 'works in the ' || department || ' department' FROM professors 

2. SELECT 'It is ' || (salary > 9500) || ' that professor' || last_name || ' is highly paid' FROM professors

3. SELECT last_name, UPPER(SUBSTRING(department, 1,3)) as department, salary, hire_date FROM profressors 

4. SELECT MAX (salary) as highest_salary MIN (salary) as lowest_salary FROM professors WHERE last_name != 'Wilson'

5. SELECT MIN (hire_date) FROM professors