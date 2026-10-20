Pizza Management System
Project Overview
The Pizza Management System is a Python application developed using Object-Oriented Programming (OOP) principles.
The system manages pizza stores and their employees. It supports employee management, employee ranking, salary expense calculations, and employee rewards.
Features
•	Manage pizza store information.
•	Add and remove employees.
•	Track employee details and rankings.
•	Calculate employee-related expenses.
•	Calculate and update store rankings.
•	Identify top-performing employees.
•	Provide surprises or rewards to employees.
Project Structure
pizza_management/
│
├── main.py
├── employee.py
├── pizza_store.py
├── pizza_hut.py
├── pizza_dominos.py
└── surprise.py
Classes Description
1. Employee
The Employee class represents an employee working at a pizza store.
It stores employee information, such as:
•	Employee ID
•	First name and last name
•	Address
•	Salary
•	Start date
•	Pizza ranking
•	Ranking date
•	Assigned surprise, if available
It also supports updating an employee's ranking and displaying employee information.
2. PizzaStore
The PizzaStore class represents the base class for pizza stores.
It contains general store information and employee management functionality.
Its responsibilities include:
•	Managing store details and employees.
•	Calculating the number of employees.
•	Calculating employee expenses.
•	Calculating and updating the store ranking.
•	Hiring and removing employees.
•	Identifying the best-performing employees.
•	Managing employee surprises.
3. PizzaHut
The PizzaHut class inherits from PizzaStore.
It implements the store-ranking calculation based on the average ranking of its employees.
4. PizzaDominos
The PizzaDominos class inherits from PizzaStore.
It implements the store-ranking calculation based on the sum of its employees' rankings.
5. Surprise
The Surprise class represents a surprise or reward assigned to an employee.
It provides functionality for activating the surprise.
Object-Oriented Programming Concepts
The project demonstrates the following OOP concepts:
•	Encapsulation: Organizing data and related functionality within classes.
•	Inheritance: PizzaHut and PizzaDominos inherit from PizzaStore.
•	Polymorphism: Different store types implement their own ranking calculations.
•	Abstraction: The base store class defines common behavior for specialized store classes.
Requirements
•	Python 3
•	PyCharm or another Python IDE
No external libraries are required if the project uses only Python's standard library.
How to Run
1.	Clone or download this repository.
2.	Open the project in PyCharm.
3.	Make sure Python 3 is installed.
4.	Open main.py.
5.	Run the program.
Alternatively, run the following command from the project directory:
python main.py
Example Output
The program displays information about pizza stores, including their IDs, employee counts, and rankings.
Example:
Pizza Hut, ID: 101, Employees: 2, Rank: 43.5
Pizza Dominos, ID: 102, Employees: 1, Rank: ...
The exact output depends on the data and calculations defined in main.py.
Author
Developed as a Python Object-Oriented Programming practice project.
