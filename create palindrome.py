import sys

if len(sys.argv) < 2:
    print("Please provide a string as a command-line argument.")
    sys.exit()

string = sys.argv[1]
processed = string.lower().replace(" ", "")
reverse_str = processed[::-1]

if processed == reverse_str:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is NOT a palindrome.")
