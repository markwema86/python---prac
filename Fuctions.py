# Basic FUctions
def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index (BMI) given weight in kilograms and height in meters."""
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)
result = calculate_bmi(70, 1.75)
print(f"Your BMI is: {result}")

#Lambda Functions
# A lambda function to calculate the area of a circle given its radius
calculate_area = lambda radius: 3.14159 * radius ** 2
print(f"Area of the circle: {calculate_area(5)}")