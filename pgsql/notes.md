# pg notes
ROLLUP allows you to aggregate data hierarchically. It produces subtotals for each group at different levels of aggregation and adds a grand total at the end.
Cube works same as roll up and gives the aggrigated output and hierarchicalli.

- WHERE → Filters rows before grouping.
- HAVING → Filters groups after aggregation.
- INNER JOIN	Returns rows that have matching values in both tables.	Only customers who placed orders.
- LEFT JOIN	Returns all rows from the left table, and matching rows from the right table. Non-matching rows show NULL.	All customers, with orders if they exist.
- RIGHT JOIN	Returns all rows from the right table, and matching rows from the left table. Non-matching rows show NULL.	All orders, with customer details if they exist.
- FULL JOIN	Returns all rows when there is a match in either table. Non-matching rows show NULL.	All customers and all orders, matched where possible.

- DELETE → Removes rows, can use WHERE, logs each row.
- TRUNCATE → Removes all rows, faster, minimal logging.
- DROP → Removes entire table structure.
- Transaction → to update the data / can be update any column ( Begin; update; commit )
- Store procedure → are work like UDF but it dow not return any value / we can modify the data by passing parameter and chnage their values ( works like excel formula it takes inpput and make operation)
- UDF ( User Define function ) → we can give the inputs and take the return UDF do the calculation or opertaion and returns the output
- Index - can help read query to run faster but makes write query slower / we can create index on multi column and drop the index as well
- CTE (Common table expression ) work same as view but in this we can add complex query in CTE and call that in main query
