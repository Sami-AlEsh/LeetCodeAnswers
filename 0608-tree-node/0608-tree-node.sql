# Write your MySQL query statement below
SELECT id,
CASE
    WHEN p_id IS NULL THEN "Root"
    WHEN (SELECT COUNT(id) FROM Tree t2 WHERE t2.p_id = t1.id) > 0 THEN "Inner"
    ELSE "Leaf"
END AS type
FROM Tree t1;