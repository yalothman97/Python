print("Python Calculator")

num1 = (input("Insert a number: "))
if num1.isdigit():
	pass
else:
	print("Invalid, please only use numbers")
	num1 = input("Try again: ")

num2 = (input("Insert another number: "))
if num2.isdigit():
	pass
else:
	print("Invalid, please only use numbers")
	num2 = input("Try again: ")

op = input("Insert a mathematical operation (+,-,*,/): ")
if op == "+":
	print("The answer is")
	print(float(num1) + float(num2))
elif op == "-":
	print("The answer is")
	print(float(num1) - float(num2))
elif op == "*":
	print("The answer is")
	print(float(num1) * float(num2))
elif op == "/":
	print("The answer is")
	print(float(num1) / float(num2))
else:
	print("Only use mathematical operations")
	op = input("Try again: ")