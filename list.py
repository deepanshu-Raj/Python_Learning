#zen of python programming and programming in general.
import this

fruits = ['apple','orange','banana','pears','pomegranate']
print(fruits)

for i in fruits:
	print(i,end = " ")
print()

#index start form (0 - len(list)-1) from left to right
#index start from (-1 - -len(list)) from right to left
#-1 index means 1st element from last.
#0 means first element from start.
for i in range(len(fruits)):
	print(fruits[i].title(),end = " ")
print() 

#lists are mutable - can be modified.


#To change an element, use the name of the list followed
#by the index of the element you want to change, and then provide the new
#value you want that item to have
fruits[2] = "grapes"
print(fruits)

#implest way to add a new element to a list is to append the item to the
#list.
fruits.append('guava')
print(fruits)

#different datatypes can be stored in the same list.
fruits.append(12)
print(fruits)

#list.insert(<index_where_to_insert>,val)
fruits.insert(0,'kiwi')
print(fruits)

#delete an element in the list.
#1) del list_name[index]
#deletes the last element from the list.
del fruits[len(fruits)-1]

#2) pop() - only pop() deletes the last element from the list.
#pop(<index>) - deletes the element at index from the list. 
#you can work with this deleted element afer poping
fruits.pop()
fruits.pop(0)

#3) <list_name>.remove(<element's_name>) - deletes the first occurence of 
#that element from the list.
fruits.append("orange")
#gives the count of the element present in the list
print(fruits.count("orange"))

fruits.remove("orange")
print(fruits)

#finding length of a list
c = 0
for i in fruits:
	c+=1;
print("{} : {}".format("length",c))
#finding length using len() function.
print("{} : {}".format("length",len(fruits)))

#sorting the list using sort function
#<list_name>.sort() sorts the list but changes the ordering permanently.
fruits.sort()
print(fruits)
#<list_name>.sort(reverse = True) will sort the list in descending order.
#permanent change in ordering
fruits.sort(reverse = True)
print(fruits)

#sorted(list,reverse= t/f) will just display the list in the order mentioned
#no change in the original ordering.
print(sorted(fruits,reverse = True))
print(sorted(fruits))

print(fruits)
