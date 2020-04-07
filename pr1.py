def inputs():
	global a
	a = int(input("Enter your age:  "))
def logic():
	inputs()
	if a > 18:
		print("You can have an ID")
	elif a == 18:
		print("You can have an ID")
	else:
		print("You can't have an ID")
logic()