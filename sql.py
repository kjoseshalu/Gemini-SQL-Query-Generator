import sqlite3

#connect to sqlite
connection=sqlite3.connect("student.db")

# create a cursor object  to insert record,create table
cursor=connection.cursor()

# create a table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

# insert records into the table
cursor.execute('''Insert into STUDENT values('Rahul','Data Science','A',90)''')
cursor.execute('''Insert into STUDENT values('Kirsh','Data Science','B',100)''')
cursor.execute('''Insert into STUDENT values('Pavan','Data Science','A',84)''')
cursor.execute('''Insert into STUDENT values('Vijay','Devops','A',60)''')
cursor.execute('''Insert into STUDENT values('Naveen','Devops','A',40)''')

# Display all the records
print('''The inserted records are''')
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# close the connection
connection.commit()
connection.close()