1. SELECT state, MAX(supply)
FROM fruit_imports
GROUP BY state
LIMIT 1

2. SELECT season, MAX(cost_per_unit)
FROM fruit_imports
GROUP BY season

3. SELECT state, name, COUNT(*)
FROM fruit_imports
GROUP BY state, name
HAVING COUNT(*) > 1

4. SELECT season,COUNT(name)
FROM fruit_imports
GROUP BY season
HAVING COUNT(name) = 3 OR COUNT(name) = 4

5. SELECT state, SUM(supply * cost_per_unit) AS total_cost
FROM fruit_imports
GROUP BY state
ORDER BY total_cost DESC
LIMIT 1

6. SELECT COUNT(COALESCE(fruit_name, 'SOMEVALUE')) AS fruit_count
FROM fruits

QUESTION <!-- WHAT's THE VALUE OF SOMEVALUE? --> 