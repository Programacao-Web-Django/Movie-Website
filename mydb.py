# import mysql.connector
import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '8844' 
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute('CREATE DATABASE base')

print("Tudo certo!")