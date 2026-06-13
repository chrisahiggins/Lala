import sys

if len(sys.argv) != 3:
    print("Usage: add.py <number1> <number2>")
    sys.exit(1)

a = float(sys.argv[1])
b = float(sys.argv[2])
print(f"{a} + {b} = {a + b}")
