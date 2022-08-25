import mysql.connector

connection = mysql.connector.connect(
    user='radmin', password='radmin', host='proxysql', port=6032, database="db"
)
if connection:
    print("DB Connected!")

cursor = connection.cursor()
cursor.execute('Select * FROM students')
students = cursor.fetchall()
connection.close()

print(students)
