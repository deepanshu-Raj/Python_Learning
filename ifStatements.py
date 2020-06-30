cars = ['audi','bmw','toyota']

#using if/else conditionals.

for car in cars:
	if(car == 'bmw'):
		print(car.upper(),end = " ")
	else:
		print(car.title(),end = " ")
print()

#using in , not in , and , or in logical expressions.

#use of in
car = 'honda'
cars.append("honda")
if car in cars:
	print("{} is present in {}".format(car,"cars"))

#use of not in
cars.pop()
if car not in cars:
	print("{} is not present in {}".format(car,"cars"))
	
age = 21
height = 180

#use of and statement
if(height>= 181 and age<=21):
	print("you go bro!!")
else:
	print("you need to grow bro!!")

#use of or statement
if(height>= 181 or age<=21):
	print("you are grown up")
else:
	print("you gottcha grow!!")

#•	 Admission for anyone under age 4 is free.
#•	 Admission for anyone between the ages of 4 and 18 is $5.
#•	 Admission for anyone age 18 or older is $10

#code:
age_ = 16
if(age_ < 4):
	print("no fee to be charged")
elif(age_>=4 and age_<18):
	print("you got to pay $5")
else:
	print("pay $10, to get admission")	
