"""
Python Data Structures Practice

Topics Covered:
- Lists & Slicing
- Tuples
- Dictionaries & Sets

Author: Manasa Pamarthi
"""

# ============================================================
# TOPIC 1: LISTS & SLICING
# ============================================================

def demonstrate_lists():
    print("\n--- Lists Demo ---")

    tech_stack = ["Python", "Java", "SQL"]
    tech_stack.append("Git")

    print("Tech Stack:", tech_stack)

    primary_skills = tech_stack[0:2]
    print("Primary Skills:", primary_skills)


def practice_lists():
    print("\n--- Lists Practice ---")

    prices = [100, 250, 400, 150]

    premium_prices = prices[2:]

    print("All Prices:", prices)
    print("Premium Prices:", premium_prices)


# ============================================================
# TOPIC 2: TUPLES
# ============================================================

def demonstrate_tuples():
    print("\n--- Tuples Demo ---")

    db_config = ("localhost", 3306, "root")

    print("Host:", db_config[0])
    print("Port:", db_config[1])


def practice_tuples():
    print("\n--- Tuples Practice ---")

    server_location = (16.506, 80.648)

    print("Server Location:", server_location)


# ============================================================
# TOPIC 3: DICTIONARIES & SETS
# ============================================================

def demonstrate_dict_and_set():
    print("\n--- Dictionary & Set Demo ---")

    dev_profile = {
        "name": "Manasa Pamarthi",
        "role": "Python Engineer"
    }

    print("Role:", dev_profile["role"])

    raw_logs = ["Error", "Warning", "Error", "Success"]
    unique_logs = set(raw_logs)

    print("Unique Logs:", unique_logs)


def practice_dict_and_set():
    print("\n--- Dictionary Practice ---")

    inventory = {"Laptop": 1200, "Mouse": 25, "Keyboard": 45}

    inventory["Mouse"] = 30

    print("Inventory:", inventory)
    print("Mouse Price:", inventory["Mouse"])


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    print("=== Python Data Structures Module ===")

    demonstrate_lists()
    practice_lists()

    demonstrate_tuples()
    practice_tuples()

    demonstrate_dict_and_set()
    practice_dict_and_set()

    print("\n--- End of Module ---")
