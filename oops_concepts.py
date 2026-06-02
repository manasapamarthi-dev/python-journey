"""
Python Learning Lab - Phase 4: Object-Oriented Programming (OOPs)

Topics Covered:
- Classes & Objects (Blueprints & Instances)
- Encapsulation (Data Security using Private attributes)
- Inheritance & Polymorphism (Code Reusability & Method Overriding)

Author: Manasa Pamarthi
"""

# ============================================================
# TOPIC 1: CLASSES, OBJECTS & ENCAPSULATION
# ============================================================

class Developer:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.__salary = salary  # Private attribute

    def display_profile(self):
        print(f"Developer: {self.name} | Role: {self.role}")

    @property
    def salary(self):
        return self.__salary


def demonstrate_oops_basics():
    print("\n--- Classes & Encapsulation Demo ---")

    dev1 = Developer("Manasa", "Python Engineer", 85000)
    dev1.display_profile()

    print("Salary Secure Access:", dev1.salary)


def practice_oops_basics():
    print("\n--- OOPs Basics Practice ---")

    class BankAccount:
        def __init__(self, owner, balance):
            self.owner = owner
            self.__balance = balance

        def deposit(self, amount):
            self.__balance += amount
            print("Deposited:", amount)

        def withdraw(self, amount):
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Insufficient balance")

        def check_balance(self):
            print(f"{self.owner} Balance: {self.__balance}")

    account = BankAccount("Manasa Pamarthi", 5000)
    account.check_balance()
    account.deposit(1000)
    account.withdraw(2000)
    account.check_balance()


# ============================================================
# TOPIC 2: INHERITANCE & POLYMORPHISM
# ============================================================

class Employee:
    def __init__(self, name):
        self.name = name

    def work_hours(self):
        return "Standard working hours: 8 hours/day"


class Manager(Employee):
    def work_hours(self):
        return "Manager working hours: 9-10 hours/day (Includes meetings)"


class Vehicle:
    def start_engine(self):
        return "Generic engine starting..."


class Car(Vehicle):
    def start_engine(self):
        return "Car engine: Vroom Vroom!"


class ElectricCar(Car):
    def start_engine(self):
        return "Electric motor silent start ⚡"


def demonstrate_inheritance():
    print("\n--- Inheritance & Polymorphism Demo ---")

    emp = Employee("Rahul")
    mgr = Manager("Suresh")

    print(f"{emp.name} -> {emp.work_hours()}")
    print(f"{mgr.name} -> {mgr.work_hours()}")

    my_car = ElectricCar()
    print("Vehicle Action:", my_car.start_engine())


def practice_inheritance():
    print("\n--- Inheritance Practice ---")

    class VehicleTest:
        def start_engine(self):
            return "Generic engine sound..."

    class CarTest(VehicleTest):
        def start_engine(self):
            return "Car Engine Started... Vroom Vroom!"

    my_car = CarTest()
    print("Car Action:", my_car.start_engine())


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    print("=== Python Learning Lab: Phase 4 (OOPs) ===")

    demonstrate_oops_basics()
    practice_oops_basics()

    demonstrate_inheritance()
    practice_inheritance()

    print("\n--- End of Module 4 ---")
