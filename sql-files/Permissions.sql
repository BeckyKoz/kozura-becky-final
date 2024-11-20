/*
Becky Kozura
CSC6302
Final Database!
Permissions
*/
USE CRM;

-- Create roles for users IN database
DROP ROLE IF EXISTS 'db_read', 'db_modify';

DROP USER IF EXISTS 'db_admin_read'@'localhost';
DROP USER IF EXISTS 'db_admin_modify'@'localhost';
DROP USER IF EXISTS 'db_admin_read'@'%';
DROP USER IF EXISTS 'db_admin_modify'@'%';
DROP USER IF EXISTS 'db_admin_modify'@'localhost';
DROP USER IF EXISTS 'robsand'@'localhost';
DROP USER IF EXISTS 'test_read'@'localhost';
DROP USER IF EXISTS 'db_admin'@'localhost';
DROP USER IF EXISTS 'dbAdmin'@'localhost';
DROP USER IF EXISTS 'read_user'@'%';
DROP USER IF EXISTS 'read_only_user'@'%';
DROP USER IF EXISTS 'modify_user'@'%';
DROP USER IF EXISTS 'db_read'@'%';
DROP USER IF EXISTS 'db_modify'@'%';
DROP USER IF EXISTS 'DBadmin1'@'%';

FLUSH PRIVILEGES;
-- SELECT * FROM mysql.USER;

-- Create roles and users
CREATE ROLE IF NOT EXISTS 'db_read', 'db_modify';

CREATE USER IF NOT EXISTS 'db_admin_read'@'localhost' IDENTIFIED BY 'db123456789';
CREATE USER IF NOT EXISTS 'db_admin_modify'@'localhost' IDENTIFIED BY 'password';

-- Grants modify-only privileges
GRANT CREATE, INSERT, UPDATE ON * TO 'db_modify';

GRANT EXECUTE ON PROCEDURE crm.AddStudent TO 'db_modify';
GRANT EXECUTE ON PROCEDURE crm.RemoveStudent TO 'db_modify';
GRANT EXECUTE ON PROCEDURE crm.AddTeacher TO 'db_modify';
GRANT EXECUTE ON PROCEDURE crm.RemoveTeacher TO 'db_modify';
GRANT EXECUTE ON PROCEDURE crm.AddClass TO 'db_modify';
GRANT EXECUTE ON PROCEDURE crm.RemoveClass TO 'db_modify';
-- GRANT EXECUTE ON PROCEDURE crm.AddAdministrator TO 'db_modify';
-- GRANT EXECUTE ON PROCEDURE crm.RemoveAdministrator TO 'db_modify';
GRANT EXECUTE ON PROCEDURE crm.AddStudentToClass TO 'db_modify';
GRANT EXECUTE ON PROCEDURE crm.RemoveStudentFromClass TO 'db_modify';

-- Grants read-only privileges
GRANT SELECT ON * TO 'db_read';

-- GRANT EXECUTE ON PROCEDURE crm.GetAllAdministrators TO 'db_read';
GRANT EXECUTE ON PROCEDURE crm.GetAllTeachers TO 'db_read';
GRANT EXECUTE ON PROCEDURE crm.GetAllStudents TO 'db_read';
GRANT EXECUTE ON PROCEDURE crm.GetAllClasses TO 'db_read';
GRANT EXECUTE ON PROCEDURE crm.GetAllStudentsInAllClasses TO 'db_read';

-- Grant roles to users
GRANT 'db_read' TO 'db_admin_read'@'localhost';
GRANT 'db_modify' TO 'db_admin_modify'@'localhost';

SET DEFAULT ROLE 'db_read' TO 'db_admin_read'@'localhost';
SET DEFAULT ROLE 'db_modify' TO 'db_admin_modify'@'localhost';

FLUSH PRIVILEGES;
