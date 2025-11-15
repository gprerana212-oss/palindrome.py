string = "GADAG"


cleaned = string.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")
