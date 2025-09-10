class CarRentalView:
    def display_message(self, message):
        print(message)

    def display_cars(self, cars):
        for car in cars:
            print(f"ID: {car[0]}, Make: {car[1]}, Model: {car[2]}, Year: {car[3]}, "
                  f"Mileage: {car[4]}, Available: {car[5]}")

    def display_rentals(self, rentals):
        for rental in rentals:
            print(f"ID: {rental[0]}, User: {rental[1]}, Car: {rental[2]}, "
                  f"Start: {rental[3]}, End: {rental[4]}, Status: {rental[5]}")