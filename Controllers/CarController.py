from Models.CarModel import Car


class CarController:
    def __init__(self):
        self.model = Car()

    def add_car(self, make, model, year, mileage, min_rent, max_rent):
        return self.model.add_car(make, model, year, mileage, min_rent, max_rent)

    def update_car(self, car_id, **kwargs):
        return self.model.update_car(car_id, **kwargs)

    def delete_car(self, car_id):
        return self.model.delete_car(car_id)

    def get_available_cars(self):
        return self.model.get_available_cars()