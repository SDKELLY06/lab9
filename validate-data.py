name = input("Please Enter Your Name: ")
mobile = input("Please Enter Mobile Number: ")

if len(name) <= 15 and len(mobile) <= 10:
	print("PASS")
else:
	print("FAIL")
