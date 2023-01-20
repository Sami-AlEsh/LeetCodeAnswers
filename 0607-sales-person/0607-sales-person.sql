# Write your MySQL query statement below
SELECT name FROM SalesPerson WHERE sales_id not in (
    SELECT SalesPerson.sales_id
    FROM Company INNER JOIN Orders ON Company.com_id = Orders.com_id
    INNER JOIN SalesPerson ON SalesPerson.sales_id = Orders.sales_id
    WHERE Company.name = "RED"
)
