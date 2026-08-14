message = input("Enter a message: ")

print("\nFirst 5 Characters:", message[:5])
print("Last 5 Characters:", message[-5:])
print("Characters from Index 2 to 7:", message[2:8])
print("Every Second Character:", message[::2])
print("Message in Reverse:", message[::-1])
print("Message Without First and Last Character:", message[1:-1])