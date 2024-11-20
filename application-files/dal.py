'''
Becky Kozura 
CSC6302 
Final Database!

Data Access Layer
'''

import mysql.connector

def userConnection(db_user, db_password):
    try:
        mydb = mysql.connector.connect(host = 'localhost', user = db_user, password = db_password, database = "CRM")
        return mydb
    except Exception as e:
        print(f"An error occurred while trying to connect to database: {e}")

def getAllTeachers():
    mydb = userConnection('db_admin_read', 'db123456789')
    cursor = mydb.cursor()
    cursor.callproc("GetAllTeachers", args=())
    results = []
    for result in cursor.stored_results():
        results.append(result.fetchall())
    cursor.close()
    return results

def getAllStudents():
    mydb = userConnection('db_admin_read', 'db123456789')
    cursor = mydb.cursor()
    cursor.callproc("GetAllStudents", args=())
    results = []
    for result in cursor.stored_results():
        results.append(result.fetchall())
    cursor.close()
    return results

def getAllClasses():
    mydb = userConnection('db_admin_read', 'db123456789')
    cursor = mydb.cursor()
    cursor.callproc("GetAllClasses", args=())
    results = []
    for result in cursor.stored_results():
        results.append(result.fetchall())
    cursor.close()
    return results

def getAllStudentsInAllClasses():
    mydb = userConnection('db_admin_read', 'db123456789')
    cursor = mydb.cursor()
    cursor.callproc("GetAllStudentsInAllClasses", args=())
    results = []
    for result in cursor.stored_results():
        results.append(result.fetchall())
    cursor.close()
    print(results)
    return results

def addStudent(firstName, lastName, dob, email):
    mydb = userConnection('db_admin_modify', 'password')
    cursor = mydb.cursor()
    cursor.callproc("AddStudent", args=(firstName, lastName, dob, email,))
    results = mydb.commit()    # must remember this step
    cursor.close()
    return results

def removeStudent(studentId):
    # try:
        mydb = userConnection('db_admin_modify', 'password')
        cursor = mydb.cursor()
        cursor.callproc("RemoveStudent", args=(studentId,))
        results = mydb.commit()    # must remember this step
        cursor.close()
        return results
    # except Exception as e:
    #     print(e)

def addTeacher(firstName, lastName, email):
        mydb = userConnection('db_admin_modify', 'password')
        cursor = mydb.cursor()
        cursor.callproc("AddTeacher", args=(firstName, lastName, email,))
        results = mydb.commit()    # must remember this step
        print(results)
        cursor.close()
        return results

def removeTeacher(teacherId):
        mydb = userConnection('db_admin_modify', 'password')
        cursor = mydb.cursor()
        cursor.callproc("RemoveTeacher", args=(teacherId,))
        results = mydb.commit()    # must remember this step
        cursor.close()
        return results

def addClass(className, department, teacherId):
        mydb = userConnection('db_admin_modify', 'password')
        cursor = mydb.cursor()
        cursor.callproc("AddClass", args=(className, department, teacherId,))
        results = mydb.commit()    # must remember this step
        cursor.close()
        return results

def addStudentToClass(studentId, classId):
        mydb = userConnection('db_admin_modify', 'password')
        cursor = mydb.cursor()
        cursor.callproc("AddStudentToClass", args=(studentId, classId))
        results = mydb.commit()    # must remember this step
        cursor.close()
        print(results)
        return results

def removeStudentFromClass(studentInClassId):
        mydb = userConnection('db_admin_modify', 'password')
        cursor = mydb.cursor()
        cursor.callproc("RemoveStudentFromClass", args=(studentInClassId,))
        results = mydb.commit()    # must remember this step
        cursor.close()
        return results

def removeClass(classId):
        mydb = userConnection('db_admin_modify', 'password')
        cursor = mydb.cursor()
        cursor.callproc("RemoveClass", args=(classId,))
        results = mydb.commit()    # must remember this step
        cursor.close()
        return results

if __name__ == '__main__':
    getAllTeachers()
    removeTeacher(2)
    addTeacher("asdf", "dad", "asdfasdf@gmail.com")
    getAllTeachers()
    getAllStudents()
    getAllClasses()
    addStudentToClass(5, 2)
    getAllStudentsInAllClasses()

