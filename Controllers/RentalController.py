from Models.RentalModel import RentalModel

class RentalController:
    def __init__(self):
        self.model = RentalModel()

    def book_rental(self, user_id, car_id, start_date, end_date):
        return self.model.book_rental(user_id, car_id, start_date, end_date)

    def get_rentals(self, status=None):
        return self.model.get_rentals(status)

    def manage_rental(self, rental_id, status):
        return self.model.update_rental_status(rental_id, status)