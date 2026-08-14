employee = ("Arjun", "Developer", 45000, 3)

# Unpack the tuple
name, designation, monthly_salary, experience = employee

# Calculate annual salary
annual_salary = monthly_salary * 12

# Calculate bonus
if experience < 2:
    bonus = annual_salary * 0.05

elif experience <= 5:
    bonus = annual_salary * 0.10

else:
    bonus = annual_salary * 0.15

# Calculate total annual compensation
total_compensation = annual_salary + bonus

# Display employee details
print("Employee Name:", name)
print("Designation:", designation)
print("Experience:", experience, "years")
print("Monthly Salary: ₹", monthly_salary)
print("Annual Salary: ₹", annual_salary)
print("Bonus: ₹", bonus)
print("Total Annual Compensation: ₹", total_compensation)