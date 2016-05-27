import sys
#NOTES - lists, sets, dictionaries
#A list keeps order, sets and dicts don't
#myList = ['1', 'alex', 'tomato', 'alex']
#print(myList[2])
#print(type(myList))

#myDict = {'1':'Alex', '2':'Divya'}
#print(myDict['1'])
#print(type(myDict))

#items = {"arrow", "spear", "arrow", "arrow", "rock"}
#if "rock" in items:
#    print("Rock exists")
#print(type(items))
#print(len(items)) #repeats aren't allowed in sets

#searching, sorting, ordering, and filtering

#Exercise 1.1 Chapter 1
#Problem: You have an N-element tuple or sequence that you would like to unpack into a collection
#of N variables

#Requirement - the number of variables match the sequence
p = (4,5) #tuple
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, type(name))
print(shares, type(shares))
print(price, type(price))
print(date, type(date))

p = (4,5)
try:
    x,y,z = p
except ValueError as e:
    print("OS error: {0}".format(e))

#unpacking works on any object that is iterable
s = 'hello'
a,b,c,d,e = s
print(a, type(a))





#questions
#1. How do you know what objects are iterable?
#2. What are generators that I keep hearing about?
#3. Strings, files, iterators, and generators are examples of iterable objects


