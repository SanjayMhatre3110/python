# SQL query practice ( partition by + Group by + rollup + order by + UDF + Store procedure (SP) + CTE )
-  partition by
SELECT
f.film_id,
title,
length,
fc.category_id,
round(avg(length) over(PARTITION BY fc.category_id),2) as avg_category_legnth
FROM film f
left join film_category fc
ON f.film_id = fc.film_id
order by 1;
;
- Group by + roll up
select * from payment;

SELECT 
TO_CHAR( payment_date,'MONTH') as mnt,
extract(week from payment_date) wk,
staff_id,
SUM(amount)
from payment
GROUP BY
	rollup(
	TO_CHAR( payment_date,'MONTH'),
	extract(week from payment_date),
	staff_id
	)
order by 1,2,3

- UDF
create function name_search3(nm1 varchar, nm2 varchar )
	returns int
	language plpgsql
as
$$
DECLARE
pm3 INT;
BEGIN
SELECT sum(amount)
INTO pm3
FROM payment p
LEFT JOIN customer c
ON p.customer_id = c.customer_id
WHERE c.first_name = nm1 and c.last_name = nm2
limit 1;
RETURN pm3;
END;
$$

SELECT name_search3('MARY','SMITH')

select 
sum(amount)
from payment p
LEFT JOIN customer c
ON p.customer_id =c.customer_id  
where c.first_name = 'MARY' and c.last_name = 'SMITH'


SELECT * FROM employees order by salary

- Store procedure (SP)
BEGIN;
UPDATE employees
SET salary = 100
WHERE emp_id = 2;
COMMIT;


create or replace procedure emp_swap (emp1 INT, emp2 INT)
	LANGUAGE plpgsql
AS
$$
DECLARE 
salary1 decimal(8,2);
salary2 decimal(8,2);
position1 text;
position2 text;
BEGIN
--takes the emp position and salary
select salary
into salary1
from employees
where emp_id = emp1;

select salary
into salary2
from employees
where emp_id = emp2;

select position_title
into position1
from employees
where emp_id = emp1;

select position_title
into position2
from employees
where emp_id = emp2;

--update the inputs as per requirement
update employees
SET salary = salary2
where emp_id = emp1;
 
update employees
SET salary = salary1
where emp_id = emp2;

update employees
SET position_title = position2
where emp_id = emp1;
 
update employees
SET position_title = position1
where emp_id = emp2;
commit;
end;
$$

call emp_swap(1,2)

select * from employees where emp_id in (1,2)



SELECT * FROM rental


select
customer_id,
count(*),
p.sum(amount)
from rental r
Left JOIN payment p 
ON r.customer_id = p.customer_id
group by customer_id

select * from customer



- CTE ( common table expression)

WITH customer_totals AS (
    SELECT c.customer_id, c.first_name, c.last_name,
           COUNT(r.rental_id) AS rental_count,
           SUM(p.amount) AS total_amount
    FROM customer c
    JOIN rental r ON c.customer_id = r.customer_id
    JOIN payment p ON c.customer_id = p.customer_id AND p.rental_id = r.rental_id
    GROUP BY c.customer_id, c.first_name, c.last_name
)
 
SELECT customer_id, first_name, last_name, rental_count, total_amount
FROM customer_totals
WHERE rental_count > (SELECT AVG(rental_count) FROM customer_totals);








