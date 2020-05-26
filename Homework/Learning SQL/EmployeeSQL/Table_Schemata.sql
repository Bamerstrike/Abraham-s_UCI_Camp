drop table IF EXISTS department;
drop table IF EXISTS department_employee;
drop table IF EXISTS department_manager;
drop table IF EXISTS employees;
drop table IF EXISTS salaries;
drop table IF EXISTS titles;

create table department(
	Dept_number varchar primary key,
	Dept_name varchar(255)
);

create table department_employee(
	Employee_number int,
	Dept_number varchar,
	Start_Date date,
	End_Date date,
	foreign key (Dept_number) references department(Dept_number)
);

create table department_manager(
	Dept_number varchar,
	Employee_number int primary key,
	Start_Date date,
	End_Date date,
	foreign key (Dept_number) references department(Dept_number)
);

create table employees(
	Employee_number int primary key,
	Birthday varchar,
	First_name varchar,
	Last_name varchar,
	Gender varchar,
	Start_Date date
);

create table salaries(
	Employee_number int primary key,
	Salary int,
	Start_Date date,
	End_Date date
);

create table titles(
	Employee_number int,
	title varchar,
	Start_Date date,
	End_Date date
);


select * from department;
select * from department_employee;
select * from department_manager;
select * from employees;
select * from salaries;
select * from titles;
