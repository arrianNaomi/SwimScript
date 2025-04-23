import sys

# Initialize an empty stack and program counter
stack = []
pc = 0
lines = []

# Load the program from the specified file
def load_program(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read().strip().split("\n")
    except Exception as e:
        print(f"Error while opening file:\n{e}")
        sys.exit(0)

# Print error message and terminate the program
def err(message):
    print(f"\n{message} at line {pc + 1}")  # +1 to show user-friendly line number
    sys.exit(0)

# Pop a value from the stack with error handling
def pop(index=-1):
    if len(stack) < 1:
        err("Error: Stack underflow")
    return stack.pop(index)

# Execute the SwimScript commands
def execute():
    global pc
    while pc < len(lines):
        parts = lines[pc].split(" ")
        instr = parts[0]
        
        if instr == "START":
            stack.append(0)
        
        elif instr == "STROKE": # Increment by one
            a = pop()
            stack.append(a + 1)

        elif instr == "COUNTDOWN": # Decrement the top value of the stack by 1
            a = pop()
            stack.append(a - 1)

        elif instr == "DIVING":
            if len(parts) < 2:
                err("Error: DIVING requires a number")
            stack.append(int(parts[1]))  # Push specified number onto the stack
        
        elif instr == "SPLASH":
            print(chr(pop()), end="", flush=True)  # Print the char at the top of the stack as a char
        
        elif instr == "SPLOOSH":
            print(int(pop()), end="", flush=True)  # Print the char at the top of the stack as an int
        
        elif instr == "FINISH":
            output = ''.join(chr(pop()) for _ in range(len(stack)))  # Build output from the stack
            print(output, end="", flush=True)
        
        # Duplicate the top value of the stack
        elif instr == "LAP":
            a = pop()
            stack.extend([a, a])
        
        # Converts the top value of the stack to an integer and pushes it back
        elif instr == "TAKEOVER":
            if len(stack) < 1:
                err("Error: Stack underflow in TAKEOVER")
            try:
                # Convert the top value of the stack from ASCII to an integer
                a = pop()
                if isinstance(a, int):  # Ensure the value is an integer
                    a = int(chr(a))  # Convert ASCII value to integer
                stack.append(a)
            except ValueError:
                err("Error: Invalid ASCII value for TAKEOVER")
        
        # Looping conditionally based on the top value of the stack
        elif instr == "DIVE":
            if len(parts) < 2:
                err("Error: Expected instruction argument for DIVE")
            try:
                target_line = int(parts[1]) - 1  # Target line (1-based to 0-based index)
                a = pop()
                if a != 0:
                    pc = target_line - 1  # Move to target line if top of stack is not zero
            except ValueError:
                err("Error: Invalid instruction argument for DIVE")
        
        # Exit the program if the top value of the stack is zero
        elif instr == "EXIT":
            if len(parts) < 2:
                err("Error: Expected instruction argument for EXIT")
            try:
                target_line = int(parts[1]) - 1  # Target line (1-based to 0-based index)
                a = pop()
                if a == 0:
                    pc = target_line - 1  # Move to target line if top of stack is zero
            except ValueError:
                err("Error: Invalid instruction argument for EXIT")
        
        # Moving values to either the top or bottom of the stack
        elif instr == "STYLE":
            if len(parts) < 2:
                err("Error: Expected to specify STYLE")
            if parts[1] == 'BACK': # To tos
                a = pop(0)
                stack.append(a)
            elif parts[1] == 'FREE': # To bos
                a = pop()
                stack.insert(0, a)

        # Takes user input and pushes the ASCII values onto the stack
        elif instr == "CALL":
            user_input = input("Please enter input: ")  # Take user input
            for char in user_input:
                stack.append(ord(char))  # Push ASCII values onto the stack
        
        # Multiply the top two values of the stack and push the result
        elif instr == "HEAT":
            a = int(chr(pop()))
            b = int(chr(pop()))
            stack.append(a * b)

        elif instr == "FALSE":
            if len(parts) < 2 or parts[1] != "START":
                err("Error: Expected instruction argument for FALSE START")
            else:
                pop()
        pc += 1  # Move to the next instruction

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python swim_script.py <filename>")
        sys.exit(0)

    program_file = sys.argv[1]
    lines = load_program(program_file)
    
    execute()
    print('')  # Final newline for cleanliness