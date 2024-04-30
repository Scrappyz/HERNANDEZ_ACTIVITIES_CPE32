# Exercise 4
grades = {"Michael": 75, "Preetam": 85, "Justin": 80, "Alondra": 95, "Arnelieh": 83}

for name, grade in grades.items():
    if grade > 90:
        print(name + " has a grade of A")
    elif grade > 75:
        print(name + " has a grade of B")
    elif grade > 65:
        print(name + " has a grade of C")