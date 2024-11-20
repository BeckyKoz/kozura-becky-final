/*
Becky Kozura
CSC6302
Final Database!
DML 
*/

USE CRM;

-- DML for Student table
INSERT INTO student (first_name, last_name, dob, email)
	VALUES ROW ("Madeline", "Kozura", "2013-09-20", "maddy@gmail.com"),
	ROW ("Charlotte", "Kozura", "2016-06-03", "char@gmail.com"), 
	ROW ("Daniel", "Broadwater", "2013-04-16", "daniel@gmail.com"), 
    ROW ("Julia", "Ames", "2016-12-22", "julia@gmail.com"), 
	ROW ("Calvin", "Ames", "2019-04-01", "calvin@gmail.com"),
	ROW ("Meg", "Haswell", "2005-08-26", "meg@gmail.com"), 
	ROW ("Norah", "Haswell", "2007-06-07", "norah@gmail.com"), 
	ROW ("Maren", "Carr", "2014-07-28", "maren@gmail.com"); 

-- DML for Teacher table
INSERT INTO teacher (first_name, last_name, email)
	VALUES ROW ("Karen", "True", "mrstrue@gmail.com"),
	ROW ("Becky", "Kozura", "mrsk@gmail.com"),
	ROW ("Ann", "Noyes", "mrsnoyes@gmail.com"),
	ROW ("Katie", "Ames", "mrsames@gmail.com"),
	ROW ("Chris", "Kozura", "mrk@gmail.com"),
	ROW ("Jamie", "Boccia", "mrb@gmail.com");

-- DML for Class table
INSERT INTO class (class_name, department, teacher_id)
	VALUES ROW ("PreAlgebra", "Math", 4),
	ROW ("Creative Writing", "English", 1),
	ROW ("Band", "Fine Arts", 6),
	ROW ("Physics", "Science", 5),
	ROW ("Civics", "Social Studies", 3),
    ROW ("Computer Science", "Science", 2);

-- DML for student_in_class
INSERT INTO student_in_class (student_id, class_id)
	VALUES ROW (1, 2),
	ROW (1, 3),
	ROW (1, 5),
	ROW (2, 1),
	ROW (2, 4),
	ROW (3, 2),
	ROW (3, 4),
	ROW (4, 2),
	ROW (4, 3),
	ROW (5, 1),
	ROW (5, 5),
	ROW (6, 2),
	ROW (6, 4),
	ROW (7, 1),
	ROW (7, 2),
	ROW (7, 3);