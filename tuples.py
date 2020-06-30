#an immutable list is known as a tuple
dimensions = (200,50)
for i in range(len(dimensions)):
	print(dimensions[i],end = " ")
print()

#Although you can’t modify a tuple, you can assign a new value to a variable
#that holds a tuple. So if we wanted to change our dimensions, we could
#redefine the entire tuple.

dimensions = (400,100) #will work perfectly fine
print(dimensions)
