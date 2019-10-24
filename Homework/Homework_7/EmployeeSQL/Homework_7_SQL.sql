-- 1. List the following details of each employee: employee number, last name, first name, gender, and salary.
select employees.Employee_number, employees.Last_name, employees.First_name, employees.Gender, salaries.salary
from salaries
inner join employees on employees.Employee_number=salaries.Employee_number;

-- 2. List employees who were hired in 1986.
select * from employees
WHERE start_date >= '19860101 00:00:00.000'
  AND start_date < '19861231 23:59:59.999';


-- 3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
select DM.Dept_number,department.Dept_name, DM.Employee_number, employees.Last_name, employees.First_name, DM.Start_Date, DM.End_Date
from department_employee as DM
join department on DM.Dept_number = department.Dept_number
join employees on DM.Employee_number = employees.Employee_number;

-- 4. List the department of each employee with the following information: employee number, last name, first name, and department name.
Select em.employee_number as "Employee Number", 
em.last_name as "Last Name", 
em.first_name as "First Name", 
department.Dept_name as "Department"
from employees as em
join department_employee on em.employee_number = department_employee.employee_number
join department on department_employee.Dept_number = department.Dept_number;

-- 5. List all employees whose first name is "Hercules" and last names begin with "B."
Select em.last_name as "Last name", em.first_name as "First Name" 
from employees as em
where em.first_name = 'Hercules'
and em.last_name like 'B%';

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
Select em.employee_number as "Employee Number", 
em.last_name as "Last Name", 
em.first_name as "First Name", 
department.Dept_name as "Department"
from employees as em 
join department_employee on em.employee_number = department_employee.employee_number 
join department on department_employee.Dept_number = department.Dept_number
where department.Dept_name = 'Sales';

-- 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
Select em.employee_number as "Employee Number", 
em.last_name as "Last Name", 
em.first_name as "First Name", 
department.Dept_name as "Department"
from employees as em 
join department_employee on em.employee_number = department_employee.employee_number 
join department on department_employee.Dept_number = department.Dept_number
where department.Dept_name = 'Sales' or department.Dept_name = 'Development';

-- 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
Select em.last_name, count(em.last_name) from employees as em
group by em.last_name
order by last_name desc;
