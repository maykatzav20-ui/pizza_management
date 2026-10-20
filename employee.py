import random
from datetime import date


class Employee:
    def __init__(self, emp_id, first_name, last_name,
                 address, salary, start_date, surprise=None):

        self.id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.salary = salary
        self.start_date = start_date
        self.surprise = surprise

        self.pizza_rank = None
        self.pizza_rank_date = None

        # יצירת דירוג אוטומטית
        self.set_rank()

    def set_rank(self):
        self.pizza_rank = random.randint(1, 100)
        self.pizza_rank_date = date.today()

    def __str__(self):
        return (
            f"Employee: {self.first_name} {self.last_name}, "
            f"ID: {self.id}, Salary: {self.salary}, "
            f"Rank: {self.pizza_rank}"
        )
