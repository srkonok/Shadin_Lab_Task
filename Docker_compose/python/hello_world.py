import mysql.connector
import MySQLdb as mdb

connection = mdb.connect(
    user='monitor', password='monitor', host='proxysql', port="6033", database="db"
)
if connection:
    print("DB Connected!")

cursor = connection.cursor()
cursor.execute('Select * FROM students')
students = cursor.fetchall()
connection.close()

print(students)
