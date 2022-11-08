# Write your MySQL query statement below
SELECT Department.name as Department, Employee.name as Employee, Employee.salary as Salary
FROM Employee JOIN Department ON Employee.departmentId = Department.id
WHERE Employee.salary = (SELECT MAX(salary) FROM Employee GROUP BY departmentId HAVING Department.id = Employee.departmentId)