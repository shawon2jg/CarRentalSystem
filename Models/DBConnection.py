import mysql.connector
from abc import ABC, abstractmethod

# Database Configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'carrentaldb'
}

class DatabaseConnection(ABC):
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()

    @abstractmethod
    def execute_query(self, query, params=None):
        pass

    def close(self):
        self.cursor.close()
        self.conn.close()