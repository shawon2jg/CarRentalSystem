import hashlib
import mysql.connector
from Models.DBConnection import DatabaseConnection

class User(DatabaseConnection):
    def __init__(self):
        super().__init__()

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
            return self.cursor
        except mysql.connector.Error as err:
            print(f"Database Error: {err}")
            self.conn.rollback()

    def register(self, username, password, role='customer'):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        query = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
        self.execute_query(query, (username, hashed_password, role))
        return True

    def login(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        query = "SELECT role FROM users WHERE username = %s AND password = %s"
        self.cursor.execute(query, (username, hashed_password))
        result = self.cursor.fetchone()
        return result[0] if result else None