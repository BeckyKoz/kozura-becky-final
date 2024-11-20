/*
Becky Kozura
CSC6302
Final Database!
DDL 
*/
DROP DATABASE IF EXISTS CRM;
CREATE DATABASE IF NOT EXISTS CRM;
USE CRM;

CREATE TABLE IF NOT EXISTS student (
	student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS teacher (
	teacher_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE 
);

CREATE TABLE IF NOT EXISTS class (
	class_id INT AUTO_INCREMENT PRIMARY KEY,
    class_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    teacher_id INT NOT NULL,
	FOREIGN KEY (teacher_id) 
		REFERENCES teacher(teacher_id)
        ON DELETE CASCADE
);

-- Class to show which classes students are enrolled in
CREATE TABLE IF NOT EXISTS student_in_class (
	student_in_class_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    class_id INT NOT NULL,
	FOREIGN KEY (student_id) 
		REFERENCES student(student_id)
        ON DELETE CASCADE,
	FOREIGN KEY (class_id) 
		REFERENCES class(class_id)
        ON DELETE CASCADE
);

-- Prevent duplicate inserts, ensure email formatting
ALTER TABLE student_in_class ADD CONSTRAINT id_studclass_unique UNIQUE(student_id, class_id);
ALTER TABLE class ADD CONSTRAINT id_class_unique UNIQUE(class_name, department, teacher_id);
ALTER TABLE student ADD CONSTRAINT student_email CHECK (student.email LIKE ('%_%@_%.__%'));
ALTER TABLE teacher ADD CONSTRAINT teacher_email CHECK (teacher.email LIKE ('%_%@_%.__%'));

RESTART;