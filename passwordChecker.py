import pwnedpasswords
i = 1
while i > 0:
	password = input("Enter q to Quit.. \nEnter password: ")
	if password == "q":
		break
	checkList = pwnedpasswords.							check(password)
	print(checkList)
	i = i+1
