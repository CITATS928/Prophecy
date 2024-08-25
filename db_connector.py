import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
    host='localhost',
    user='qian',
    password='zipcode0',
    database='Prophecy'
    )
    return connection

def fetch_browsing_history():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    #query = "SELECT * FROM Chrome_History ORDER BY visit_date DESC, visit_time DESC"
    query = "SELECT * FROM Chrome_History LIMIT 1000"
    cursor.execute(query)
    history = cursor.fetchall()
    connection.close()
    return history