# CREATE DATABASE IF NOT EXISTS alx_book_store
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kisumu@333%%",
    database="alx_book_store"
)

mycursor = mydb.cursor()
mycursor.execute("""
CREATE DATABASE IF NOT EXIST alx_book_store
""")
