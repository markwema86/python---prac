# The 6 types of Variables and Data Types in Python you will constantly use in Data Science
age = 25  # Integer (int) - whoole number
salary = 175000000000.50  # Float (float) - decimal number
name = "Alice"  # String (str) - text 
is_hired = True  # Boolean (bool) - True or False
scores = [85, 90, 78]  # List (list) - ordered, mutable collection of items
person = {"name": "Alice", "age": 25, "is_hired": True}  # Dictionary (dict) - unordered, mutable collection of key-value pairs
# Displaying the variables and their types
print(f"Age: {age} (Type: {type(age)})")
print(f"Salary: {salary} (Type: {type(salary)})")
print(f"Name: {name} (Type: {type(name)})")
print(f"Is Hired: {is_hired} (Type: {type(is_hired)})")
print(f"Scores: {scores} (Type: {type(scores)})")
print(f"Person: {person} (Type: {type(person)})")

# Control Flow - If, For, While
# If /elif /else
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
# For Loop
exam_scores = [85, 90, 78]
passing = []
for score in exam_scores:
    if score >= 80:
        passing.append(score)
print(f"Passing Scores: {passing}")
# While Loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
    
