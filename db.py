import mysql.connector

def connect():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",          
            password="",          
            database="student_db" 
        )
        print("Database connection successful!")  # <- debug message
        return db
    except mysql.connector.Error as err:
        print("MySQL connection failed:", err)
        exit()  
