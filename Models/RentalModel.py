import mysql.connector
from Models.DBConnection import DatabaseConnection

class RentalModel(DatabaseConnection):
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

    def book_rental(self, user_id, car_id, start_date, end_date):
        days = (end_date - start_date).days
        query = """INSERT INTO rentals (user_id, car_id, start_date, end_date, status, total_cost)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        total_cost = self.calculate_cost(car_id, days)
        self.execute_query(query, (user_id, car_id, start_date, end_date, 'pending', total_cost))
        self.update_car_availability(car_id, False)
        return True

    def calculate_cost(self, car_id, days):
        query = "SELECT daily_rate FROM cars WHERE id = %s"
        self.cursor.execute(query, (car_id,))
        daily_rate = self.cursor.fetchone()[0] or 50  # Default rate if None
        return daily_rate * days

    def update_car_availability(self, car_id, available):
        query = "UPDATE cars SET available = %s WHERE id = %s"
        self.execute_query(query, (available, car_id))

    def get_rentals(self, status=None):
        query = "SELECT * FROM rentals"
        if status:
            query += " WHERE status = %s"
            self.cursor.execute(query, (status,))
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_rental_status(self, rental_id, status):
        query = "UPDATE rentals SET status = %s WHERE id = %s"
        self.execute_query(query, (status, rental_id))
        if status in ['approved', 'rejected']:
            query = "SELECT car_id FROM rentals WHERE id = %s"
            self.cursor.execute(query, (rental_id,))
            car_id = self.cursor.fetchone()[0]
            self.update_car_availability(car_id, status == 'rejected')
        return True