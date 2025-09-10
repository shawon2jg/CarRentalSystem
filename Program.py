from datetime import datetime
from Controllers.CarController import CarController
from Controllers.RentalController import RentalController
from Controllers.UserController import UserController
from Views.CarRentalView import CarRentalView

class CarRentalSystem:
    def __init__(self):
        self.user_controller = UserController()
        self.car_controller = CarController()
        self.rental_controller = RentalController()
        self.view = CarRentalView()

    def run(self):
        while True:
            print("\n1. Register\n2. Login\n3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                username = input("Username: ")
                password = input("Password: ")
                role = input("Role (customer/admin): ").lower()
                if self.user_controller.register(username, password, role):
                    self.view.display_message("Registration successful")

            elif choice == '2':
                username = input("Username: ")
                password = input("Password: ")
                role = self.user_controller.login(username, password)
                if role:
                    self.view.display_message(f"Logged in as {role}")
                    if role == 'admin':
                        self.admin_menu()
                    else:
                        self.customer_menu()
                else:
                    self.view.display_message("Invalid credentials")

            elif choice == '3':
                break

    def admin_menu(self):
        while True:
            print("\nAdmin Menu:")
            print("1. Add Car\n2. Update Car\n3. Delete Car\n4. View Rentals\n5. Manage Rentals\n6. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                make = input("Make: ")
                model = input("Model: ")
                year = int(input("Year: "))
                mileage = int(input("Mileage: "))
                min_rent = int(input("Minimum rent period (days): "))
                max_rent = int(input("Maximum rent period (days): "))
                if self.car_controller.add_car(make, model, year, mileage, min_rent, max_rent):
                    self.view.display_message("Car added successfully")

            elif choice == '2':
                car_id = int(input("Car ID: "))
                updates = {}
                if input("Update make? (y/n): ").lower() == 'y':
                    updates['make'] = input("New make: ")
                if input("Update model? (y/n): ").lower() == 'y':
                    updates['model'] = input("New model: ")
                if updates and self.car_controller.update_car(car_id, **updates):
                    self.view.display_message("Car updated successfully")

            elif choice == '3':
                car_id = int(input("Car ID: "))
                if self.car_controller.delete_car(car_id):
                    self.view.display_message("Car deleted successfully")

            elif choice == '4':
                rentals = self.rental_controller.get_rentals()
                self.view.display_rentals(rentals)

            elif choice == '5':
                rental_id = int(input("Rental ID: "))
                status = input("Status (approve/reject): ").lower()
                if status in ['approved', 'rejected'] and self.rental_controller.manage_rental(rental_id, status):
                    self.view.display_message(f"Rental {status} successfully")

            elif choice == '6':
                break

    def customer_menu(self):
        while True:
            print("\nCustomer Menu:")
            print("1. View Available Cars\n2. Book Rental\n3. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                cars = self.car_controller.get_available_cars()
                self.view.display_cars(cars)

            elif choice == '2':
                user_id = int(input("Your User ID: "))
                car_id = int(input("Car ID: "))
                start_date = datetime.strptime(input("Start date (YYYY-MM-DD): "), '%Y-%m-%d')
                end_date = datetime.strptime(input("End date (YYYY-MM-DD): "), '%Y-%m-%d')
                if self.rental_controller.book_rental(user_id, car_id, start_date, end_date):
                    self.view.display_message("Rental booked successfully")

            elif choice == '3':
                break

if __name__ == "__main__":
    app = CarRentalSystem()
    app.run()