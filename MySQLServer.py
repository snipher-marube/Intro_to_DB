#!/usr/bin/python3
"""Script to create the alx_book_store database in MySQL"""

import mysql.connector
from mysql.connector import Error, DatabaseError

def create_database():
    """Function to create the database"""
    connection = None
    cursor = None
    
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password=''   # Replace with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            try:
                # Create database if it doesn't exist
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
                
            except DatabaseError as db_err:
                print(f"Database operation failed: {db_err}")
                
    except Error as e:
        print(f"MySQL connection error occurred: {e}")
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        
    finally:
        # Close the connection
        try:
            if cursor is not None:
                cursor.close()
            if connection is not None and connection.is_connected():
                connection.close()
                print("MySQL connection is closed")
        except Error as close_err:
            print(f"Error while closing connection: {close_err}")

if __name__ == "__main__":
    create_database()