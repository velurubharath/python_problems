def greet(name):
    return f"Hello {name}"

print(greet("Bharath"))

#Lambda function
square = lambda x: x*x

print(square(6))

numbers = [1,2,3,4]

#List comprehension
square = [x*x for x in numbers]

print(square)

#Exception Handling
try:
    num = 10/0
except ZeroDivisionError:
    print("Cannot divide num by zero")

#File Handling
#Read file
with open("test.txt","r") as file:
    print(file.read())

#Write file
with open("test.txt","w") as file:
    file.write("Hello")


#File Append
with open("test.txt","a") as file:
    file.write(" new Line")

