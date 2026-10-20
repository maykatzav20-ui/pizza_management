from datetime import date

from employee import Employee
from pizza_hut import PizzaHut
from pizza_dominos import PizzaDominos


# יצירת עובדים
e1 = Employee(
    1, "Dana", "Levi", "Tel Aviv", 10000, date(2024, 1, 1)
)

e2 = Employee(
    2, "Noam", "Cohen", "Haifa", 12000, date(2023, 5, 1)
)

e3 = Employee(
    3, "Maya", "Israel", "Jerusalem", 11000, date(2022, 3, 1)
)


# יצירת שתי הפיצריות
hut = PizzaHut(
    101, "Pizza Hut", "Tel Aviv", "03-1111111",
    [e1, e2]
)

dominos = PizzaDominos(
    102, "Pizza Dominos", "Haifa", "04-2222222",
    [e3]
)


# הצגת פרטי הפיצריות
print(hut)
print(dominos)

print("Pizza Hut expenses:", hut.calculate_employee_expenses())
print("Dominos expenses:", dominos.calculate_employee_expenses())


# הוספת עובד
hut.hire_employee(e3)

print("Employees in Pizza Hut:", hut.number_of_employees)
print("Updated Pizza Hut rank:", hut.rank)


# ניסיון להוסיף עובד שכבר מועסק בחנות
hut.hire_employee(e1)


# בדיקת תוקף הדירוגים: יום אחד
hut.calculate_ranged_rank(1)

print("Pizza Hut rank after checking dates:", hut.rank)


# מתן הפתעה לעובד או לעובדים הטובים ביותר
hut.give_surprise_to_best_employees()

# הפעלת הפתעה
hut.activate_employee_surprise(e1)


# התפטרות עובד
hut.resign_employee(e1)

print("Employees after resignation:", hut.number_of_employees)
print("Employee surprise after resignation:", e1.surprise)
print("Final Pizza Hut rank:", hut.rank)