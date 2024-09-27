import sqlite3

def create_database():
     conn = sqlite3.connect('School.db')
     cursor = conn.cursor()
     cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            age INTEGER,
            grade TEXT NOT NULL,
            enrollment_date DATE DEFAULT CURRENT_DATE
        )
    ''')
     cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL,
            teacher_name TEXT NOT NULL
        )
    ''')
     conn.commit()
     conn.close()

def register_student():
    full_name = input("Введите полное имя студента:")
    age = int(input("Введите возраст студента: "))
    grade = input("Введите класс студента: ")
    conn = sqlite3.connect('School.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (full_name, age, grade)
        VALUES (?, ?, ?)
    ''', (full_name, age, grade))
    conn.commit()
    conn.close()
    print("Студент успешно зарегистргрирован!")

def add_subject():
    subject_name = input("Введите название предмета")
    teacher_name = input("Введите имя учителя")
    conn = sqlite3.connect('School.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO subjects (subject_name, teacher_name)
        VALUES (?, ?)
    ''', (subject_name, teacher_name))
    conn.commit()
    conn.close()
    print("Предмет успешно добавлен!")

def get_students():
    conn = sqlite3.connect('School.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    for student in students:
        print(student)
    conn.close()

def get_subjects():
    conn = sqlite3.connect('School.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM subjects')
    subjects = cursor.fetchall()
    for subject in subjects:
        print(subject)
    conn.close()

def get_students_by_grade(grade):
    conn = sqlite3.connect('School.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE grade = ?', (grade,))
 
    students = cursor.fetchall()
 
    for student in students:
        print(student)
    conn.close()

def update_student_age(student_id, new_age):
    conn = sqlite3.connect('School.db')
 
    cursor = conn.cursor()
 
    cursor.execute('''
        UPDATE students
        SET age = ?
        WHERE id = ?
    ''', (new_age, student_id))
    conn.commit()
    conn.close()
    print(f"Возраст студента с ID {student_id} обновлен на {new_age}")

def delete_student(student_id):
    conn = sqlite3.connect('School.db')
    cursor = conn.cursor()
 
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
 
    print(f"Студент с ID{student_id}был удален")

def get_student_count_by_grade():
    conn = sqlite3.connect('School.db')
    cursor = conn.cursor()
    cursor.execute('SELECT grade, COUNT(*) FROM students GROUP BY grade')
    counts = cursor.fetchall()
 
    for grade, count in counts:
        print(f"В кассе {grade} всего студеентов: {count}")
    conn.close()

def get_teacher_subjects(teacher_name):
    conn = sqlite3.connect('School.db')
    cursor = conn.cursor()
    cursor.execute('SELECT subject_name FROM subjects WHERE teacher_name = ?', (teacher_name,))
    subjects = cursor.fetchall()
 
    for subject in subjects:
        print(subject[0])
    conn.close()

create_database()

register_student()


add_subject()

print("Список студентов:")

get_students()

print("Список предлетов:")

get_subjects()
grade_input = input("Введите класс для поиска студентов: ")

get_students_by_grade(grade_input)

student_id_input = int(input("Введите ID студента для обновления возраста: "))
new_age_input = int(input("Введите новый возраст: "))

update_student_age(student_id_input, new_age_input)
delete_student(student_id_input)

print("Количество студентов в каждом классе:")

get_student_count_by_grade()

teacher_name_input = input("Введите имя учителя для поиска предметов: ")

get_teacher_subjects(teacher_name_input)
 
 
 
 
 
"""
 Задача 1: Создание базы данных и таблиц
1) Создайте базу данных с именем School.db.
2) В этой базе данных создайте две таблицы:
                 students:
                id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
               full_name (TEXT, NOT NULL)
               age (INTEGER)
               grade (TEXT, NOT NULL)
               enrollment_date (DATE, DEFAULT: текущая дата)
               subjects:
               id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
               subject_name (TEXT, NOT NULL)
               teacher_name (TEXT, NOT NULL)


Задача 2: Добавление данных в таблицы
    1) Создайте функцию register_student(), которая запрашивает у пользователя данные о студенте (полное имя, возраст, класс) и добавляет эту информацию в таблицу students.
   2) Создайте функцию add_subject(), которая запрашивает у пользователя название предмета и имя учителя, и добавляет эту информацию в таблицу subjects.


Задача 3: Запросы и выборки данных
   1) Создайте функцию get_students(), которая выводит всех студентов из таблицы students.
   2) Создайте функцию get_subjects(), которая выводит все предметы из таблицы subjects.
   3) Напишите функцию get_students_by_grade(grade), которая принимает на вход класс и выводит всех студентов, обучающихся в этом классе.


Задача 4: Обновление и удаление данных
   1) Создайте функцию update_student_age(student_id, new_age), которая обновляет возраст студента с заданным student_id на новое значение new_age.
   2) Создайте функцию delete_student(student_id), которая удаляет студента с заданным student_id из таблицы students.


Задача 5: Дополнительные задания (по желанию)
   1) Реализуйте функцию get_student_count_by_grade(), которая выводит количество студентов в каждом классе.
   2) Реализуйте функцию get_teacher_subjects(teacher_name), которая принимает имя учителя и выводит все предметы, которые он преподает.


Дополнительные указания:
При работе с базой данных используйте параметризацию запросов для предотвращения SQL-инъекций.
Постарайтесь структурировать код так, чтобы каждая функция выполняла одну задачу и была легко читаемой.
Это задание поможет вам закрепить основные навыки работы с базой данных SQLite3: создание таблиц, добавление, выборка, обновление и удаление данных.
4o"""