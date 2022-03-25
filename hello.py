print("hello man")

a = float(input("Select first num ----> "))
operation = input("What do we do? (+, -, *, /) ----> ")
b = float(input("Select second num ----> "))


if operation == "+":
	c = a + b
elif operation == "-":
	c = a - b
elif operation == "*":
	c = a * b
elif operation == "/":
	c = a / b
	
print("Result ----> " + str(c))

#hello.py