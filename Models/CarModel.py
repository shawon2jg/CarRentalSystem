import mysql.connector
from Models.DBConnection import DatabaseConnection

class Car(DatabaseConnection):
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

    def add_car(self, make, model, year, mileage, min_rent, max_rent):
        query = """INSERT INTO cars (make, model, year, mileage, available, min_rent_period, max_rent_period)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        self.execute_query(query, (make, model, year, mileage, True, min_rent, max_rent))
        return True

    def update_car(self, car_id, **kwargs):
        updates = ', '.join(f"{key} = %s" for key in kwargs)
        query = f"UPDATE cars SET {updates} WHERE id = %s"
        params = list(kwargs.values()) + [car_id]
        self.execute_query(query, params)
        return True

    def delete_car(self, car_id):
        query = "DELETE FROM cars WHERE id = %s"
        self.execute_query(query, (car_id,))
        return True

    def get_available_cars(self):
        query = "SELECT * FROM cars WHERE available = TRUE"
        self.cursor.execute(query)
        return self.cursor.fetchall()