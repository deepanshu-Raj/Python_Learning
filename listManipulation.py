import this

print("---------------------------------------------------------")
names = ['alpha','beta','theta']

#traversing the list
for name in names:
	print(name.title(),end = " ")
print()

#len() determines the length of the list.
#range(len(list)) iterates over the entire length of the list
for i in range(len(names)):
	print("Hello ,"+names[i].title()+" !")
print()

#list(range(<start>,<stop>,<update>)) creates a list from the range.
nums = list(range(2,11,2))
print(nums)

#how to use lists with loop - traditional method.
squares = []
for i in range(1,11):
	squares.append(i**2)
print(squares)

#min(<list_name>),max(<list_name>),sum(<list_name>)
print(min(squares))           #1
print(max(squares))           #100
print(sum(squares))           #385

#list comprehesion
cubes = [value**3 for value in range(1,11)]
print(cubes)

#slicing in lists
cubes_part = cubes[:5]
print("the first five elements of cubes are:",end = " ")
for i in cubes_part:
	print(i,end = " ")
print()

#list[-3:] will slice starting from 3rd element from the last of the list to the
#very end of the list 

print(cubes[-3:])

#making a copy of a list
num = [1,2,3,4,5,6]
num1 = num[:]             #deep copy of the list num.
num2 = num                #shallow copy of the list num.

#shallow copy means - we are just making num2 to point to the num list object.
#deep copy means - we actually are creating a new num list and assigning it to num1.

#with deep copy , changes made in the copy aren't reflected in the original list.
#whereas wth shallow copy the changes made in the copy is reflected in the original list also.
num.append(8)
num1.append(7)
num2.append(9)
print(num1)
print(num)
print(num2)
