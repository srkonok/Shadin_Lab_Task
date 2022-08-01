import mysql.connector
import json

def confunc():
	mydb = mysql.connector.connect(
            host="remotemysql.com",
            port="3306",
            user="1eQAzD8RMj",
            passwd="R9Uin6Sq5V",
            database="1eQAzD8RMj"
        )
                                    
	return mydb