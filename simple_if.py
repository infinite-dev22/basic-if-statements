#if statements
#
#types:
#1)	if
#2)	if...else
#3)	if...elif...else

#1) plain if statement

#getting user input.
user_age = input("Hello, how old are you: \n")

#since user input is string type, we make the digits string too.
#note: you can explicitly convert the data type of inpit with 'int' keyword.
if user_age < "18" and user_age <= "12":
	print("you are a child and not a teenager")
	
if user_age < "18" and user_age >= "13":
	print("you are a child and a teenager")
	
if user_age >= "18" and user_age < "20":
	print("you are an adult and a teenager")	
	
if user_age >= "20" and user_age <= "45":
	print("you are a youthful adult, and not a teenager")
	
if user_age >="20" and user_age >"45":
	print("you are an adult, and not a teenager or youth")


#2) if else statement

login_pass = "Xhvkns/2853jh@dkg"

password = input("\vEnter password: \n")

if password == login_pass:
	print("Access granted \n User logged in.")
else:
		print("Access denied \nwrong password entered")
		
#3) if...elif...else statement
# with this kimd of if statement, you can have as many 'elif' phrases 
#as one wishes but only one 'if' and 'else' phrase.
# instead of using multiple 'if' statements like was done in 1), 
#we can use the 'if...elif...else' statement.

print("Available professions:\n 1->Doctor \n 2->Nurse \n 3->Sudent \n 4->Software Engineer")

#explicitly converting input value from string type to integer type.
profession = int(input("Hello, what is your profession: \n"))

if profession == 1:
	print("you are a Doctor")
	
elif profession == 2:
	print("you are a Nurse")
	
elif profession == 3:
	print("you are Student")	
	
elif profession == 4:
	print("you are a Software engineer/coder/programer")
	
else:
	print("please select from options above \nby entering the number.")