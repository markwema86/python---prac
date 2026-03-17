# List Comprehension - write like a pro
# This single python feature appears in almost every data science code and is a must-know for any aspiring data scientist. It allows you to create new lists by applying an expression to each item in an iterable, while optionally filtering items using a condition. This results in more concise and readable code compared to traditional loops.
#Slow way
square = []
for i in range(1, 11):
    square.append(i ** 2)
print(square)
# Fast Pythonic way
square = [i ** 2 for i in range(1, 11)]
print(square)
# List comprehension with a condition
even = [x for x  in range(20) if x % 2 == 0]
print(even)
