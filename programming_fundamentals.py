"""
python learning lab - Phase 1:programming Fundamentals

Topics Covered:
- Variables & Type Casting
- Conditional Statements
- Loops (for, while)

Author: Manasa Pamarthi
"""

# ============================================================
# TOPIC 1: VARIABLES & TYPE CASTING
# ============================================================

def demonstrate_type_casting():
    print("\n--- Type Casting Demo ---")

    raw_score = "88.5"   # string input

    print("Original value:", raw_score)
    print("Original type:", type(raw_score))

    clean_score = float(raw_score)

    print("Converted value:", clean_score)
    print("New type:", type(clean_score))


def practice_type_casting():
    print("\n--- Practice ---")

    age = "21"
    age = int(age)

    is_eligible = age >= 18

    print("Age:", age)
    print("Eligible to vote:", is_eligible)


# ============================================================
# TOPIC 2: CONDITIONAL STATEMENTS
# ============================================================

def evaluate_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Strong"
    elif score >= 50:
        return "Average"
    else:
        return "Needs Improvement"


def practice_conditionals():
    print("\n--- Practice ---")

    cart_value = 120

    if cart_value > 100:
        shipping = 0
    elif cart_value > 50:
        shipping = 5
    else:
        shipping = 10

    print("Cart Value:", cart_value)
    print("Shipping Fee:", shipping)


# ============================================================
# TOPIC 3: LOOPS
# ============================================================

def demonstrate_loops():
    print("\n--- For Loop ---")
    for i in range(1, 4):
        print("Iteration:", i)

    print("\n--- While Loop ---")
    count = 3
    while count > 0:
        print("Count:", count)
        count -= 1


def practice_loops():
    print("\n--- Loop Practice ---")

    alerts = ["Lag", "CPU High", "Memory Full"]

    for alert in alerts:
        print("Alert:", alert)


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    print("=== Python Fundamentals Learning Lab ===")

    demonstrate_type_casting()
    practice_type_casting()

    print("\nScore Result:", evaluate_score(82))

    practice_conditionals()

    demonstrate_loops()
    practice_loops()
