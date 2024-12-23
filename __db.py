# | ID | Name   | Age | Email           |
# |----|--------|-----|-----------------|
# | 1  | Ali    | 25  | ali@example.com |
# | 2  | Sara   | 30  | sara@example.com |



# row  سطر : A single record in a table containing all attribute values of an entity.
#           Ali , Sara

# column ==in db==> field => ستون : A field representing a specific attribute of entities, such as name, age, or email.
#                                    Name , Age , Email


# primary key => کلید اصلی => منحسر به فرده :  A unique identifier for each record, ensuring no duplicates or null values, used to distinguish rows in a table.
#                                            ID


# به مجموع اطلاعات میگن table
# به مجموع table ها میگن database





# if we have 2 teachers
# and teacher 1 shouldn't see the students of teacher 2
# this is relationship  so  we have to make a primary key
# we have to make a new field that used for id of students of each teacher
# | ID | Name  | Age | Email           | students |
# |----|-------|-----|-----------------|----------|
# | 1  | MONA  | 25  | mona@example.com| [1,2,3]  |
# | 2  | sara  | 30  | sara@example.com|





# databases :
# SQL databases = table :       # SQL   PostgreSQL   Oracle  MySQL  SQLLite
# NoSQL = no table :            # MongoDB


import sqlite3 as sql

# I want to connect to sqlite

# students => Table

conn = sql.connect("db.db")   ## connect or make a database   Database == db
#                   name  .  db

cursor = conn.cursor()              ## create Object as cursor

# create Table :
cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY, name TEXT NOT NULL,age INTEGER ,grade INTEGER,email TEXT)''')


conn.commit() # commit/save changes



# create Table :
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT NOT NULL,age INTEGER,email TEXT)''')


conn.commit() # commit/save changes



cursor.execute('''
INSERT INTO teachers(name, grade, email)
VALUES (?,?,?)
''',('mona',18,"mona.asghari@gmail.com")
)

conn.commit()








##############################################
# fetchone          |
# fetchall          |
# fetchmany         |
##############################################




























