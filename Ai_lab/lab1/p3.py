# logic_gates.py

def and_gate(a, b):
    """Returns the result of Logical AND operation."""
    return a and b

def or_gate(a, b):
    """Returns the result of Logical OR operation."""
    return a or b

def not_gate(a):
    """Returns the result of Logical NOT operation."""
    return not a

def nand_gate(a, b):
    """Returns the result of Logical NAND operation."""
    return not (a and b)

def nor_gate(a, b):
    """Returns the result of Logical NOR operation."""
    return not (a or b)

def xor_gate(a, b):
    """Returns the result of Logical XOR operation (Exclusive OR)."""
    return a != b  # In Python, XOR for booleans is effectively 'not equal'

def xnor_gate(a, b):
    """Returns the result of Logical XNOR operation (Exclusive NOR)."""
    return a == b  # XNOR is effectively 'equal' for booleans

def to_bool(value):
    """Converts integer 0/1 to boolean False/True."""
    return value != 0

def to_int(value):
    """Converts boolean False/True to integer 0/1."""
    return 1 if value else 0

def display_result(gate_name, a, b=None, result=None):
    """Helper to print results in a consistent format."""
    if b is None:
        # For single input gates like NOT
        print(f"{gate_name}({to_int(a)}) = {to_int(result)}")
    else:
        # For dual input gates
        print(f"{gate_name}({to_int(a)}, {to_int(b)}) = {to_int(result)}")

def get_input(prompt):
    """Helper to safely get 0 or 1 from user."""
    while True:
        try:
            val = int(input(prompt))
            if val in (0, 1):
                return val
            print("Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        print("\n===== Logic Gates Implementation =====")
        print("1. AND Gate")
        print("2. OR Gate")
        print("3. NOT Gate")
        print("4. NAND Gate")
        print("5. NOR Gate")
        print("6. XOR Gate")
        print("7. XNOR Gate")
        print("8. Test All Gates")
        print("0. Exit")
        
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid choice! Please enter a number.")
            continue

        if choice == 0:
            print("Exiting...")
            break

        if choice == 8:
            input1 = get_input("Enter first input (0 or 1): ")
            input2 = get_input("Enter second input (0 or 1): ")

            a = to_bool(input1)
            b = to_bool(input2)

            print("\n----- Results -----")
            display_result("AND  ", a, b, and_gate(a, b))
            display_result("OR   ", a, b, or_gate(a, b))
            display_result("NOT A", a, b=None, result=not_gate(a))
            display_result("NOT B", b, b=None, result=not_gate(b))
            display_result("NAND ", a, b, nand_gate(a, b))
            display_result("NOR  ", a, b, nor_gate(a, b))
            display_result("XOR  ", a, b, xor_gate(a, b))
            display_result("XNOR ", a, b, xnor_gate(a, b))

        elif choice == 3:
            input_val = get_input("Enter input (0 or 1): ")
            a = to_bool(input_val)
            result = not_gate(a)
            display_result("NOT", a, b=None, result=result)

        elif 1 <= choice <= 7:
            input1 = get_input("Enter first input (0 or 1): ")
            input2 = get_input("Enter second input (0 or 1): ")

            a = to_bool(input1)
            b = to_bool(input2)
            result = False
            gate_name = ""

            if choice == 1:
                result = and_gate(a, b)
                gate_name = "AND"
            elif choice == 2:
                result = or_gate(a, b)
                gate_name = "OR"
            elif choice == 4:
                result = nand_gate(a, b)
                gate_name = "NAND"
            elif choice == 5:
                result = nor_gate(a, b)
                gate_name = "NOR"
            elif choice == 6:
                result = xor_gate(a, b)
                gate_name = "XOR"
            elif choice == 7:
                result = xnor_gate(a, b)
                gate_name = "XNOR"

            display_result(gate_name, a, b, result)

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

# python p3.py