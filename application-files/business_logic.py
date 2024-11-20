'''
Becky Kozura 
CSC6302
Final Database!

Business Logic Layer
'''

import dal

# ------Read-only methods----------
def getAllTeachers():
        result = dal.getAllTeachers()
        return result

def getAllStudents():
        result = dal.getAllStudents()
        return result

def getAllClasses():
        result = dal.getAllClasses()
        return result

def getAllStudentsInAllClasses():
        result = dal.getAllStudentsInAllClasses()
        return result

# ------ Modify-only methods
def addStudent(firstName, lastName, dob, email):
        dal.addStudent(firstName, lastName, dob, email)

def removeStudent(studentId):
        dal.removeStudent(studentId)

def addTeacher(firstName, lastName, email):
        dal.addTeacher(firstName, lastName, email)

def removeTeacher(teacherId):
        dal.removeTeacher(teacherId)

def addClass(className, department, teacherId):
        dal.addClass(className, department, teacherId)

def addStudentToClass(studentId, classId):
        dal.addStudentToClass(studentId, classId)

def removeStudentFromClass(studentInClassId):
        dal.removeStudentFromClass(studentInClassId)

def removeClass(classId):
        dal.removeClass(classId)

# Main driver code
if __name__ == '__main__':
    teacher = getAllTeachers()
    addStudent("test", "student", "2000-01-01", "test@gmail.com")
    students = getAllStudents()

