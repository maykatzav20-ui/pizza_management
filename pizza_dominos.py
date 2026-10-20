from pizza_store import PizzaStore


class PizzaDominos(PizzaStore):
    def calculate_rank(self):
        return sum(
            employee.pizza_rank for employee in self.employees
        )
