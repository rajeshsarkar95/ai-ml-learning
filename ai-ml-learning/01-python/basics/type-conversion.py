# Python Type Conversion

# 1. Integer to Float
num = 10
result = float(num)
print(result)
print(type(result))

# Float to Integer
price = 99.99
result = int(price)
print(result)
print(type(result))

# 3. Integer to String
age = 21
result = str(age)
print(result)
print(type(result))

# 4 String to Integer
num = "100"
result = int(num)
print(result)
print(type(result))

# 5. String to Float
price = "99.99"
result = float(price)
print(result)
print(type(result))

# Float to String
price = 99.99
result = str(price)
print(result)
print(type(price))

# 7. Integer to Boolean
num = 1
result = bool(num)
print(result)
print(type(result))

# 8. String to Boolean
name = "Rajesh"
result = bool(name)
print(result)
print(type(result))

# 9. List to Tuple
numbers = [1,2,3,4,5,6,7,8]
result = tuple(numbers)
print(result)
print(type(result))

# 11. List to Set
numbers = [1,2,3,4,5,6,7,8,9]
result = set(numbers)
print(result)
print(type(result))

# 12. User input conversion
# age = input("Enter your age:")
print(age)
print(type(age))
# input() always returns a string
age = int(age)
print(age)
print(type(age))

# 13 Practicales examples 
num1 = input("Enter first number")
num2  = input("Enter second number")
num1 = int(num1)
num2 = int(num2)
total = num1 + num2
print("total",total)
# Important concept
# Python has two types of conversion:
# 1. Implicit conversion — Python automatically converts the type.
num = 10
decimal = 2.5
result = num + decimal
print(result)
print(type(result))





