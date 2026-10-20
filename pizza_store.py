from datetime import date
from surprise import Surprise


class PizzaStore:
    def __init__(self, store_id, name, address,
                 phone_number, employees=None):

        self.id = store_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.employees = list(employees) if employees else []

        # הדירוג מחושב כבר בזמן יצירת הפיצרייה
        self.rank = self.calculate_rank()

    @property
    def number_of_employees(self):
        return len(self.employees)

    def calculate_employee_expenses(self):
        return sum(employee.salary for employee in self.employees)

    def calculate_rank(self):
        raise NotImplementedError(
            "Subclasses must implement calculate_rank()"
        )

    def update_rank(self):
        self.rank = self.calculate_rank()
        return self.rank

    def hire_employee(self, employee):
        # לא ניתן להעסיק עובד שכבר נמצא ברשימה
        if employee in self.employees:
            print("Employee already works at this store.")
            return False

        self.employees.append(employee)
        self.update_rank()
        return True

    def resign_employee(self, employee):
        # בדיקה שהעובד אכן שייך לפיצרייה
        if employee not in self.employees:
            print("Employee does not work at this store.")
            return False

        # החזרת ההפתעה בעת עזיבת העובד
        employee.surprise = None

        self.employees.remove(employee)
        self.update_rank()
        return True

    def calculate_ranged_rank(self, rank_range):
        if rank_range < 0:
            raise ValueError("rank_range cannot be negative")

        today = date.today()

        for employee in self.employees:
            days_passed = (
                today - employee.pizza_rank_date
            ).days

            if days_passed > rank_range:
                print(
                    f"{employee.first_name} {employee.last_name} "
                    "needs to rank again."
                )
                employee.set_rank()

        # הדירוג של החנות מתעדכן בעקבות שינויי דירוג העובדים
        self.update_rank()
        return self.rank

    def give_surprise_to_best_employees(self):
        if not self.employees:
            print("There are no employees in this store.")
            return

        best_rank = max(
            employee.pizza_rank for employee in self.employees
        )

        for employee in self.employees:
            if employee.pizza_rank == best_rank:
                employee.surprise = Surprise()

    def activate_employee_surprise(self, employee):
        if employee not in self.employees:
            print("Employee does not work at this store.")
            return False

        if employee.surprise is None:
            print("This employee has no surprise.")
            return False

        if not callable(
            getattr(employee.surprise, "activate_surprise", None)
        ):
            raise TypeError(
                "Surprise must have activate_surprise()"
            )

        employee.surprise.activate_surprise()
        return True

    def __str__(self):
        return (
            f"{self.name}, ID: {self.id}, "
            f"Employees: {self.number_of_employees}, "
            f"Rank: {self.rank}"
        )
