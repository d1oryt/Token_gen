import random
while True:
	char1  = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890.-_"
	char2 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890"

	num1 = int(input("Token a générer:"))
	num2 = int(input("Le mot de passe:"))
	Choice1 = str(input("y/n:"))




	if Choice1 == 'y':
		for p in range(num1):
			password = ""
			for c in range(num2):
				password += random.choice(char1)
			print(password)
	if Choice1 == 'n':
		for p in range(num1):
			password = ""
			for c in range(num2):
				password += random.choice(char2)
			print(password)