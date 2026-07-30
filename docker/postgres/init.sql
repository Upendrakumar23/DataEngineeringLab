CREATE TABLE employees
(
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary INTEGER
);


INSERT INTO employees(name,department,salary)
VALUES
('Rahul','IT',70000),
('Amit','HR',50000),
('Neha','Finance',60000);