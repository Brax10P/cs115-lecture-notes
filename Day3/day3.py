""""
a = 3
#b = "My name is Braxton"
b = 6.5
c = "My name"

if a > b:
  print("something here")

print(type(a))
print(type(b))
print(type(c))

c = 5
print(type(c))

my_list = ["another string",5, "My age", 5.67]
print(type(my_list))

#accessing a list
print(my_list[0])
print(my_list[3])

#adding to list
my_list.append("milk")
print(my_list)

#acessing first character in list
print(my_list[0][0])

#removing from list
my_list.remove(5) #removes the first instance of 5 in the list
print(my_list)
my_list.pop(2) #pops the item in position 2 from list
print(my_list)

#length of list
print(len(my_list))


#Exercise with list
my_list = ["Call mom", "Walk the dog", "Go to the grocery store"]
print(my_list)
my_list.append("Read a book")
print(my_list)
my_list[1]="Finish Homework"
print(my_list)
my_list.pop(0)
print(my_list)
print(len(my_list))
"""

coordinates = [
  (100,200), 
  (200,300)
]


