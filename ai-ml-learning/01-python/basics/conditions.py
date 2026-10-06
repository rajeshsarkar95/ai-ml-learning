# Python Conditions
# 1. Simple if statement
age = 21
if age >= 18:
    print("You are an adult")
# 2. if-else
age = 16
if age >= 18:
    print("You can vote")
else:
    print("you cannot votes")

#if-elif-else
marks = 75
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F") 

# 4. Multiple conditions using and
age = 21
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry not allowed")

# 5. Multiple conditions using or

day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")

# 6. not operator
is_rainings = False
if not is_rainings:
    print("You can go outside")

# 7. Nested if
age = 21
has_license = True

if age >= 18:
    print("You are eligible by age")

    if has_license:
        print("You can drive")
    else:
        print("You need a driving license")
else:
    print("You are underage")

# 8. Comparing numbers
num = 10
if num > 0:
    print("Positive Numbers")
elif num < 0:
    print("Negetive Numbers")
else:
    print("Zero")

# 9 .Even or add
num = 9
if num % 2 == 0:
    print("Even number")
else:
    print("odd number")

# 10 Checking a string
name = "Rajesh"
if name == str or "Rajesh":
    print("name is String") 
else:
    print("name is not String")

# 11. Membership condition
skills = ["Python","Javascript","React"]
if "Python" in skills:
    print("Python is availabkle")

# 12 . Checking empty values
name = ""
if name:
    print("Name is availble")
else:
    print("Name is empty")

# 13. Ternary operator
age = 21
message = "Adult" if age >= 18 else "Minor"
print(message)
# 14. Practical marks example
marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Marks:", marks)
print("Grade:", grade) 

# 15. Practical login example     
username = "rajesh"
password = "123456"
entered_username = "Rajesh"
entered_password = "123456"
if entered_password == username and entered_password == password:
    print("Login password")
else:
    print("Invalide username or password")            