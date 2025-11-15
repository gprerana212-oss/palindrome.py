# palindrome.py

# Program to check if a string is a palindrome using if–else statements

string = input("Enter a string: ")

# Convert to lowercase and remove spaces
processed = string.lower().replace(" ", "")

# Reverse the string manually
reverse_str = processed[::-1]

if processed == reverse_str:
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is NOT a palindrome.")
