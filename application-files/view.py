"""
Becky Kozura 
CSC6302 
Final Database! 

View Layer

Using PySimpleGUI of PySimpleSoft, Inc and/or its licensors. 
All rights reserved. Copyright 2021-2023
"""

import PySimpleGUI as sg
import business_logic as bl

# --- Helper function to make blank table for queried data ---
def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    return data

# ------ Student Functions--------
def addStudent(firstName, lastName, dob, email):
    bl.addStudent(firstName, lastName, dob, email)
    print(f"Student added")

def getStudents(window):
    students = bl.getAllStudents()
    data = []
    for student in students:
        for s in student:
            data.append(s)
            print(s)
    return window['-TABLE1-'].update(values=data[:][:])

def removeStudent(studentId):
    bl.removeStudent(studentId)
    print("[LOG] student removed")
    # sg.popup(f'Error:', keep_on_top=True)

# ------ Teacher Functions--------
def addTeacher(firstName, lastName, email):
    bl.addTeacher(firstName, lastName, email)
    print(f"Teacher added")

def getTeachers(window):
    teachers = bl.getAllTeachers()
    data = []
    for teacher in teachers:
        for t in teacher:
            data.append(t)
    return window['-TABLE2-'].update(values=data[:][:])

def removeTeacher(teacherId):
    bl.removeTeacher(teacherId)
    print("[LOG] Teacher removed")

# ------ Class Functions--------
def addClass(className, department, teacherId):
    bl.addClass(className, department, teacherId)
    print(f"Class added")

def getClasses(window):
    classes = bl.getAllClasses()
    data = []
    for cl in classes:
        for c in cl:
            data.append(c)
    return window['-TABLE3-'].update(values=data[:][:])

def removeClass(classId):
    bl.removeClass(classId)
    print("[LOG] Class removed")

# -------- Combination functions ------
def getAllStudentsInAllClasses(window):
    students_in_classes = bl.getAllStudentsInAllClasses()
    data = []
    for student_in_class in students_in_classes:
        for sc in student_in_class:
            data.append(sc)
    return window['-TABLE5-'].update(values=data[:][:])

def addStudentToClass(studentId, classId):
    bl.addStudentToClass(studentId, classId)
    print(f"Student added to class")

def removeStudentFromClass(studentInClassId):
    bl.removeStudentFromClass(studentInClassId)
    print("[LOG] Student removed from class")

def validate(inputs):
    valid = True
    for input in inputs:
        if len(input) < 1:
            valid = False
            return valid
    return valid

def isString(strings):
    for input in strings:
        if input.isalpha() is False:
            valid = False
            return valid
    return valid

# ------ Create headers and blank tables for queries --------
student_headings = ["Student ID", "First Name", "Last Name", "DOB", "Email"]
student_data = make_table(10, len(student_headings))

teacher_headings = ["Teacher ID", "First Name", "Last Name", "Email"]
teacher_data = make_table(10, len(teacher_headings))

class_headings = ["Class ID", "Class Name", "Department", "Teacher ID"]
class_data = make_table(10, len(class_headings))

student_in_class_headings = ["Enrollment ID", "First Name", "Last Name", "Class Name"]
student_in_class_data = make_table(10, len(student_in_class_headings))

def make_window(theme):
    '''
    Constructs the window using individual layout arrays. All elements and initial styles 
    are implemented here. 
    '''
    sg.theme(theme)
    menu_def = [['&Application', ['&Exit']], ['&Help', ['&About']] ]

    student_layout =  [
        [sg.Text('')], 
        [sg.Text('LOOK UP ALL STUDENTS')], 
        [sg.Table(
            values=student_data[:][:], 
            headings=student_headings, 
            auto_size_columns=False,
            col_widths=[10,10,10,10,30],
            display_row_numbers=False,
            justification='left',
            right_click_selects=True,
            num_rows=8,
            alternating_row_color='light gray',
            key='-TABLE1-',
            enable_events=True,
            expand_x=True,
            expand_y=True,
            tooltip='Student table')],
        [sg.Button('Query Students'), sg.Text('   (<---Start here!)')],
        [sg.HorizontalSeparator(
            pad=(5,15),
        )],
        [sg.Text('ADD A STUDENT')], 
        [sg.Text('  (DOB must be in format \'YYYYMMDD\', with no dashes  ---   Email must be in format \'x@x.xx\', with at least one letter for each x.)')],
        [sg.Text('First Name', size=(12, 1)), sg.InputText(key='-FIRST_NAME-')],
        [sg.Text('Last Name', size=(12, 1)), sg.InputText(key='-LAST_NAME-')],
        [sg.Text('Date of Birth', size=(12, 1)), sg.InputText(key='-DOB-')],
        [sg.Text('Email Address', size=(12, 1)), sg.InputText(key='-EMAIL-')],
        [sg.Button('Add Student')], # clear fields on press
        [sg.HorizontalSeparator(
            pad=(5, 15),
        )],
        [sg.Text('REMOVE A STUDENT BY ID')], 
        [sg.Text('  (Query students to look up student IDs. Null deletions do not cause an error.)')],
        [sg.Text('Student ID', size=(10, 1)), sg.InputText(key='-STUDENT_ID-')],
        [sg.Button('Remove Student')],
        [sg.Text('')]
    ]

    teacher_layout = [
        [sg.Text('')], 
        [sg.Text('LOOK UP ALL TEACHERS')], 
        [sg.Table(
            values=teacher_data[:][:], 
            headings=teacher_headings, 
            auto_size_columns=False,
            col_widths=[10,10,10,30],
            display_row_numbers=False,
            justification='left',
            right_click_selects=True,
            num_rows=8,
            alternating_row_color='light gray',
            key='-TABLE2-',
            enable_events=True,
            expand_x=True,
            expand_y=True,
            tooltip='Teacher table')],
        [sg.Button('Query Teachers'), sg.Text('   (<---Start here!)')],
        [sg.Text('')], 
        [sg.HorizontalSeparator()],
        [sg.Text('')], 
        [sg.Text('ADD A TEACHER')], 
        [sg.Text('  (Email must be in format \'x@x.xx\', with at least one letter for each x.)')],
        [sg.Text('First Name', size=(12, 1)), sg.InputText(key='-FIRST_NAME_T-')],
        [sg.Text('Last Name', size=(12, 1)), sg.InputText(key='-LAST_NAME_T-')],
        [sg.Text('Email Address', size=(12, 1)), sg.InputText(key='-EMAIL_T-')],
        [sg.Button('Add Teacher')],
        [sg.Text('')], 
        [sg.HorizontalSeparator()],
        [sg.Text('')], 
        [sg.Text('REMOVE A TEACHER BY ID')], 
        [sg.Text('  (Query teachers to look up teacher IDs. Null deletions do not cause an error.)')],
        [sg.Text('Teacher ID', size=(10, 1)), sg.InputText(key='-TEACHER_ID-')],
        [sg.Button('Remove Teacher')],
        [sg.Text('')]
    ]

    student_in_class_layout = [
        [sg.Text('')], 
        [sg.Text('LOOK UP ALL STUDENT ENROLLMENTS')],
        [sg.Table(
            values=student_in_class_data[:][:], 
            headings=student_in_class_headings, 
            auto_size_columns=False,
            col_widths=[12,12,12,30],
            display_row_numbers=False,
            justification='left',
            right_click_selects=True,
            num_rows=8,
            alternating_row_color='light gray',
            key='-TABLE5-', 
            enable_events=True,
            expand_x=True,
            expand_y=True,
            tooltip='student enrollment table')],
        [sg.Button('Query All Student Enrollments'), sg.Text('   (<---Start here!)')],
        [sg.Text('')], 
        [sg.HorizontalSeparator()],
        [sg.Text('')], 
        [sg.Text('ADD A STUDENT TO A CLASS')], 
        [sg.Text('  (You must look up both the individual\'s Student ID and the Class ID. NOTE: Enrollment in class will not work if Student ID and Class ID do not BOTH exist.)')], 
        [sg.Text('Student ID', size=(10, 1)), sg.InputText(key='-STUDENT_ID_SC-')],
        [sg.Text('Class ID', size=(10, 1)), sg.InputText(key='-CLASS_ID_SC-')],
        [sg.Button('Add Student Enrollment')],
        [sg.Text('')], 
        [sg.HorizontalSeparator()],
        [sg.Text('')], 
        [sg.Text('REMOVE A STUDENT FROM A CLASS')], 
        [sg.Text('  (Be sure to use the "Enrollment ID" in query table above. Null deletions do not cause an error.)')],
        [sg.Text('Enrollment ID', size=(15, 1)), sg.InputText(key='-STUDENT_IN_CLASS_ID-')],
        [sg.Button('Remove Student Enrollment')],
        [sg.Text('')]
    ]

    class_layout = [
        [sg.Text('')], 
        [sg.Text('LOOK UP ALL CLASSES')], 
        [sg.Table(
            values=class_data[:][:], 
            headings=class_headings, 
            auto_size_columns=False,
            col_widths=[12,12,12,32],
            display_row_numbers=False,                    
            justification='left',
            right_click_selects=True,
            num_rows=8,
            alternating_row_color='light gray',
            key='-TABLE3-', 
            enable_events=True,
            expand_x=True,
            expand_y=True,
            tooltip='Class table')],
        [sg.Button('Query Classes'), sg.Text('   (<---Start here!)')],
        [sg.Text('')], 
        [sg.HorizontalSeparator()],
        [sg.Text('')], 
        [sg.Text('ADD A CLASS')], 
        [sg.Text('  (To find the Teacher ID, use the Teachers tab to look up available teachers. NOTE: Creation of class will not work if Teacher ID does not exist.)')], 
        [sg.Text('Class Name', size=(10, 1)), sg.InputText(key='-CLASS_NAME-')],
        [sg.Text('Department', size=(10, 1)), sg.InputText(key='-DEPARTMENT-')],
        [sg.Text('Teacher ID', size=(10, 1)), sg.InputText(key='-TEACHER_ID_FK-')],
        [sg.Button('Add Class')],
        [sg.Text('')], 
        [sg.HorizontalSeparator()],
        [sg.Text('')], 
        [sg.Text('REMOVE A CLASS BY ID')], 
        [sg.Text('  (Query classes to look up class IDs. Null deletions do not cause an error.)')],
        [sg.Text('Class ID', size=(10, 1)), sg.InputText(key='-CLASS_ID-')],
        [sg.Button('Remove Class')],
        [sg.Text('')]        
    ]
        
    # ------ Assemble single layout array --------
    layout = [ 
        [sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)],
        [sg.Text('Kozura Academy Database View', 
            size=(38, 1), 
            justification='center', 
            font=("Helvetica", 16), 
            relief=sg.RELIEF_RIDGE, 
            k='-TEXT HEADING-', 
            enable_events=True)]
    ]
    
    layout +=[[sg.TabGroup([
        [sg.Tab('Students', student_layout),
        sg.Tab('Teachers', teacher_layout),
        sg.Tab('Classes', class_layout),
        sg.Tab('Enrollments', student_in_class_layout),
        ]], 
        key='-TAB GROUP-', 
        expand_x=True, 
        expand_y=True, 
        enable_events=True),
    ]]
    layout[-1].append(sg.Sizegrip())

    # ------ Create main window object --------
    window = sg.Window('Kozura School Database View', 
        layout, 
        right_click_menu_tearoff=True, 
        grab_anywhere=True, 
        resizable=True, 
        margins=(0,0), 
        use_custom_titlebar=True, 
        finalize=True, 
        keep_on_top=True)
    window.set_min_size(window.size)
    return window

def main():
    '''
    Driver code. Initializes main window and runs event loop,  which controls the buttons. 

    The window.read() function returns a tuple: an event and all values. 
    Input is gathered and parsed using key-value pairs. The events are all 
    defined in the event loop. 
    '''
    sg.theme('light green 2')
    window = make_window(sg.theme())
    sg.popup('Welcome to the Kozura School Database! (README)', 
            '\nTo begin, select a tab and use the \'Query\' button to fetch information from the database.', 
            'Navigate between tabs to search different tables of data.', 
            'Use the \'Add\' and \'Delete\' buttons on each tab for additional functionality.', 
            'If you experience unexpected behavior, double-check that you are using valid inputs.', 
            'For example, if you delete a class, any corresponding entries in the \'Enrollment\' table will also have been deleted.', 
            '', keep_on_top=True)

    # This is an Event Loop 
    while True:
        event, values = window.read(timeout=10)
       
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('============ Event = ', event, ' ==============')
            print('-------- Values Dictionary (key=value) --------')
            for key in values:
                print(key, ' = ',values[key])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break

        if event == 'About':
            print("[LOG] Clicked About!")
            sg.popup('Kozura School Database ',
                     'Visit each of the tabs to see available options for using the database. \n',
                     keep_on_top=True)
        
        elif event == 'Add Student':
            fname = values['-FIRST_NAME-']
            lname = values['-LAST_NAME-']
            dob = values['-DOB-']
            email = values['-EMAIL-']
            inputs = [fname, lname, dob, email] 
            valid = False
            valid = validate(inputs)
            if valid is False:
                sg.popup(f'Oops! One or more inputs are probably missing.', keep_on_top=True)
            else:
                try:
                    addStudent(fname, lname, dob, email)
                    getStudents(window)
                    print("[LOG] student added")
                except Exception as e:
                    sg.popup(f'Oops! Make sure you have: \n--Entered a valid DOB, such as 19991130 \n--Entered a unique email \n--Entered an email in the format \'x@x.xx\'. \n\nERROR: \n{e}', keep_on_top=True)
        
        elif event == 'Query Students':
            try:
                getStudents(window)
            except Exception as e:
                sg.popup(f'Error: {e}', keep_on_top=True)

        elif event == 'Remove Student':
            student = values['-STUDENT_ID-']
            try:
                removeStudent(student)
                getStudents(window)
                print("[LOG] student removed")     
                sg.popup(f'Student with ID {student} has been removed. \n(If that Student ID did not exist, no changes have been made.)', keep_on_top=True)
            except Exception as e:
                sg.popup(f'Error: \nMake sure your Student ID is valid', keep_on_top=True)

        elif event == 'Add Teacher':
            fname = values['-FIRST_NAME_T-']
            lname = values['-LAST_NAME_T-']
            email = values['-EMAIL_T-']
            inputs = [fname, lname, email] 
            valid = validate(inputs)
            if valid is False:
                sg.popup(f'Error: missing an input field', keep_on_top=True)
            else:
                try:
                    addTeacher(fname, lname, email)
                    getTeachers(window)
                    print("[LOG] teacher added")
                except Exception as e:
                    sg.popup(f'Oops! Make sure you have: \n--Entered a unique email \n--Entered an email in the format \'x@x.xx\'. \n\nERROR: \n{e}', keep_on_top=True)

        elif event == 'Query Teachers':
            getTeachers(window)

        elif event == 'Remove Teacher':
            teacher = values['-TEACHER_ID-']
            try:
                removeTeacher(teacher)
                getTeachers(window)
                print("[LOG] Teacher removed!")
                sg.popup(f'Teacher with ID {teacher} has been removed. \n(If that Teacher ID did not exist, no changes have been made.)', keep_on_top=True)
            except Exception as e:
                sg.popup(f'Error: Not a valid Teacher ID', keep_on_top=True)

        elif event == 'Add Class':
            cname = values['-CLASS_NAME-']
            dept = values['-DEPARTMENT-']
            teacher = values['-TEACHER_ID_FK-']
            inputs = [cname, dept, teacher] 
            valid = False
            valid = validate(inputs)
            if valid is False:
                sg.popup(f'Error: missing an input field', keep_on_top=True)
            else:
                try:
                    addClass(cname, dept, teacher)
                    getClasses(window)
                    print("[LOG] Class added")
                except Exception as e:
                    sg.popup(f'Error: {e}', keep_on_top=True)

        elif event == 'Query Classes':
            getClasses(window)

        elif event == 'Remove Class':
            classId = values['-CLASS_ID-']
            try:
                removeClass(classId)
                getClasses(window)
                print("[LOG] Class removed!")
                sg.popup(f'Class with ID {classId} has been removed. \n(If that Class ID did not exist, no changes have been made.)', keep_on_top=True)
            except Exception as e:
                sg.popup(f'Error: Not a valid Class ID', keep_on_top=True)

        elif event == 'Add Student Enrollment':
            studentId = values['-STUDENT_ID_SC-']
            classId = values['-CLASS_ID_SC-']
            inputs = [studentId, classId] 
            valid = False
            valid = validate(inputs)
            if valid is False:
                sg.popup(f'Error: missing an input field', keep_on_top=True)
            else:
                try:
                    addStudentToClass(studentId, classId)
                    getAllStudentsInAllClasses(window)
                    print("[LOG] Student added to class")
                except Exception as e:
                    sg.popup(f'Error: {e}', keep_on_top=True)
        
        elif event == 'Query All Student Enrollments':
            getAllStudentsInAllClasses(window)

        elif event == 'Remove Student Enrollment':
            studentInClass = values['-STUDENT_IN_CLASS_ID-']
            try:
                removeStudentFromClass(studentInClass)
                getAllStudentsInAllClasses(window)
                print("[LOG] Student removed from class!")
                sg.popup(f'Student enrollment with ID {studentInClass} has been removed. \n(If that enrollment ID did not exist, no changes have been made.)', keep_on_top=True)
            except Exception as e:
                sg.popup(f'Error: Not a valid Enrollment ID', keep_on_top=True)

    window.close()
    exit(0)

if __name__ == '__main__':
    main()