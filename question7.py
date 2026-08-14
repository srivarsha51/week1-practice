values = [10, 10, 20, 20, 20, 30, 10, 10, 40]

result = []

for value in values:
    
    if len(result) == 0 or value != result[-1]:
        result.append(value)

print("Original List:")
print(values)

print("\nResult:")
print(result)