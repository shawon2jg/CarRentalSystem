I'll create a Car Rental System using Python with MySQL, implementing OOP principles and MVC architecture. The system will include user management, car management, and rental booking functionality as specified.

This implementation includes:

1. **OOP Principles**:
   - **Encapsulation**: Data and methods are encapsulated in classes (UserModel, CarModel, RentalModel).
   - **Abstraction**: Abstract base class DatabaseConnection defines a contract for database operations.
   - **Inheritance**: Model classes inherit from DatabaseConnection.
   - **Polymorphism**: execute_query method is implemented differently in each model class.

2. **MVC Architecture**:
   - **Model**: UserModel, CarModel, RentalModel handle data and database operations.
   - **View**: CarRentalView handles user interface and output display.
   - **Controller**: UserController, CarController, RentalController manage the business logic.

3. **Requirements Implementation**:
   - User Management: Registration and login with role-based access (customer/admin).
   - Car Management: Admin can add, update, and delete car records in the database.
   - Rental Booking: Customers can view available cars and book rentals with automatic cost calculation.
   - Rental Management: Admins can view and manage (approve/reject) rental requests.

To use this system:
1. Install MySQL and the `mysql-connector-python` package (`pip install mysql-connector-python`).
2. Update the DB_CONFIG with your MySQL credentials.
3. Run the script, which will create the necessary database tables and start the application.

The system provides a command-line interface for both customers and admins to interact with the car rental system, with all data persisted in the MySQL database.