from pizza_store import PizzaStore


class PizzaHut(PizzaStore):
    def calculate_rank(self):
        if not self.employees:
            return 0

        total_rank = sum(
            employee.pizza_rank for employee in self.employees
        )

        return total_rank / len(self.employees)
