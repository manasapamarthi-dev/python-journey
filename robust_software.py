"""
Python Learning Lab - Phase 3: Robust Software Development

Topics Covered:
- Exception Handling (try-except-finally)
- File I/O Streams (Reading, Writing, and Appending files)

Author: Manasa Pamarthi
"""

# ============================================================
# TOPIC 1: EXCEPTION HANDLING (CRASH-PROOF CODE)
# ============================================================

def demonstrate_exceptions():
    print("\n--- Exception Handling Demo ---")
    
    try:
        numerator = 10
        denominator = 0  # This triggers ZeroDivisionError
        result = numerator / denominator
        print("Result:", result)

    except ZeroDivisionError:
        print("[ERROR HANDLED]: Cannot divide by zero!")

    finally:
        print("Execution Completed: Finally block always runs.")


def practice_exceptions():
    print("\n--- Exception Practice ---")
    
    user_input = "Python3"
    
    try:
        converted_data = int(user_input)
        print("Converted Data:", converted_data)

    except ValueError:
        print(f"[SAFE HANDLED]: '{user_input}' cannot be converted to integer.")


# ============================================================
# TOPIC 2: FILE I/O OPERATIONS (DATA HANDLING)
# ============================================================

def demonstrate_file_io():
    print("\n--- File I/O Demo ---")
    
    filename = "server_logs.txt"
    
    # Writing data
    with open(filename, "w") as file:
        file.write("System Status: Operational\nDatabase: Connected\n")

    print(f"File created: {filename}")

    # Reading data (Added .strip() to clean trailing blank spaces)
    print("Reading file content:")
    with open(filename, "r") as file:
        content = file.read()
        print(content.strip())


def practice_file_io():
    print("\n--- File I/O Practice ---")
    
    log_file = "system_alerts.log"
    
    # Appending logs
    with open(log_file, "a") as file:
        file.write("[ALERT]: High memory usage detected!\n")

    print(f"Log updated in: {log_file}")

    # Reading appended data back to verify transaction flow
    print("Verifying Appended Logs:")
    with open(log_file, "r") as file:
        content = file.read()
        print(content.strip())


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    print("=== Python Learning Lab: Phase 3 ===")

    demonstrate_exceptions()
    practice_exceptions()

    demonstrate_file_io()
    practice_file_io()

    print("\n--- End of Module 3 ---")
