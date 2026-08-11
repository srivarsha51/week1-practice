expenses = [250, 1200, 450, 800, 150, 2000, 350]

# Calculate total expense
total_expense = sum(expenses)

# Calculate average expense
average_expense = total_expense / len(expenses)

# Find highest and lowest expense
highest_expense = max(expenses)
lowest_expense = min(expenses)

# Count expenses above and below/equal to ₹500
above_500 = 0
below_or_equal_500 = 0

for expense in expenses:
    if expense > 500:
        above_500 += 1
    else:
        below_or_equal_500 += 1

# Display results
print("Total Expense: ₹", total_expense)
print("Average Expense: ₹", average_expense)
print("Highest Expense: ₹", highest_expense)
print("Lowest Expense: ₹", lowest_expense)
print("Number of Expenses Above ₹500:", above_500)
print("Number of Expenses Below or Equal to ₹500:", below_or_equal_500)

# Display expenses greater than average
print("\nExpenses Above Average:")

for expense in expenses:
    if expense > average_expense:
        print(expense)