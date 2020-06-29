#zen of python programming and programming in general.
import this

print("hello world")
name = "deepanshu raj"
# string.title() creates the initials of the name in uppercase. 
print(name.title())

#working with string datatypes
#you can concatenate strings, on your will.
name = "deepanshu" + " raj"
print(name.title())
print(name.upper())
print(name.lower())

#interpretation becomes very easy.
message = "Hello! ," + name.title() + "."
print(message)

#<string>.strip() helps to remove whitespace from both left/right sides of the string

#string conversion using str().
age = 23
message = "happy " + str(age) + "rd birthday!!"
print(message)
#use of string formatting.
print("happy {}rd birthday!!".format(age))
