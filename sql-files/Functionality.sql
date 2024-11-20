/*
Becky Kozura
CSC6302
Final Database!
Functionality
*/

USE CRM;

DROP PROCEDURE IF EXISTS GetAllTeachers;
delimiter $$

CREATE PROCEDURE GetAllTeachers()
	BEGIN
		SELECT *
		FROM teacher;
	END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS GetAllStudents;
delimiter $$

CREATE PROCEDURE GetAllStudents()
	BEGIN
		SELECT *
		FROM student;
	END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS GetAllClasses;
delimiter $$

CREATE PROCEDURE GetAllClasses()
	BEGIN
		SELECT *
		FROM class;
	END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS GetAllStudentsInAllClasses;
delimiter $$
CREATE PROCEDURE GetAllStudentsInAllClasses()
	BEGIN
		SELECT student_in_class_id, student.first_name, student.last_name, class.class_name
        FROM student_in_class
        INNER JOIN student
        ON student.student_id = student_in_class.student_id
        INNER JOIN class
        ON student_in_class.class_id = class.class_id;
	END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS AddStudentToClass;
delimiter $$
CREATE PROCEDURE AddStudentToClass(desiredStudentId INT, desiredClassId INT)
	BEGIN
		INSERT IGNORE INTO student_in_class (student_id, class_id)
        VALUES (desiredStudentId, desiredClassId);
	END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS RemoveStudentFromClass;
delimiter $$
CREATE PROCEDURE RemoveStudentFromClass(desiredId INT)
	BEGIN
		DELETE FROM student_in_class
        WHERE (student_in_class_id = desiredId);
	END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS AddStudent;
delimiter $$
CREATE PROCEDURE AddStudent(first_name VARCHAR(50), last_name VARCHAR(100), DOB DATE, email VARCHAR(100))
	BEGIN
		INSERT INTO student (first_name, last_name, dob, email)
        VALUES (first_name, last_name, DOB, email);
	END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS RemoveStudent;
delimiter $$
CREATE PROCEDURE RemoveStudent(desiredId INT) 
	BEGIN
		DELETE FROM student 
        WHERE (student_id = desiredId);
	END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS AddClass;
delimiter $$
CREATE PROCEDURE AddClass(classname VARCHAR(50), dept VARCHAR(100), teacherid INT) 
	BEGIN
		INSERT IGNORE INTO class (class_name, department, teacher_id)
		VALUES (classname, dept, teacherid);
    END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS RemoveClass;
delimiter $$
CREATE PROCEDURE RemoveClass(desiredId INT)
	BEGIN
		DELETE FROM class 
        WHERE (class_id = desiredId);
	END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS AddTeacher;
delimiter $$
CREATE PROCEDURE AddTeacher(fname VARCHAR(50), lname VARCHAR(100), email VARCHAR(100))
	BEGIN
		INSERT INTO teacher (first_name, last_name, email)
        VALUES (fname, lname, email);
	END;
$$
delimiter ;

DROP PROCEDURE IF EXISTS RemoveTeacher;
delimiter $$
CREATE PROCEDURE RemoveTeacher(desiredId INT)
	BEGIN
		DELETE FROM teacher 
        WHERE (teacher_id = desiredId);
	END;
$$
delimiter ;