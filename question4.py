text = input("Enter text: ")

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
other = 0

for char in text:

    if char.isupper():
        uppercase += 1

    elif char.islower():
        lowercase += 1

    elif char.isdigit():
        digits += 1

    elif char == " ":
        spaces += 1

    else:
        other += 1

print("\nUppercase Letters:", uppercase)
print("Lowercase Letters:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Other Characters:", other)