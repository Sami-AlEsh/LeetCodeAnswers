# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE P1 FROM Person AS p1 LEFT JOIN Person AS p2 ON p1.email = p2.email 
WHERE p1.id > p2.id