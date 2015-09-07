__author__ = 'Mobarak'

"""
? append(): Adds a new entry to the end of the list.
? clear(): Removes all entries from the list.
? copy(): Creates a copy of the current list and places it in a new list.
? extend(): Adds items from an existing list and into the current list.
? insert(): Adds a new entry to the position specified in the list.
? pop(): Removes an entry from the end of the list.
? remove(): Removes an entry from the specified position in the list.
"""

List1=[]                # Creates a List

print(List1)            # >>> []

# gets the length of the List
print(len(List1))       # >>> 0

# Insert some data to list with append('value')
# append() add value at the end of list
List1.append(1)

print(List1)            # >>> [1]

# gets the length of the List
print(len(List1))       # >>> 1
print(List1[0])         # >>> 1

#inset some data to list
List1.insert(0,0)
print(List1)            # >>> [0,1]

# Remember: append() add value at the end of list
List1.append(2)
print(List1)            #>>>[0, 1, 2]

# insert value on position 4
List1.insert(4,4)
print(List1)            #>>>[0, 1, 2, 4]

# Now insert value on position 3
List1.insert(3,3)
print(List1)            #>>>[0, 1, 2, 3, 4]

# copy List1 and assigns to List2
List2 = List1.copy()
print(List2)            #>>>[0, 1, 2, 3, 4]


print(">>> List1.extend(List2)")
# copies all the elements in List2 to the end of List1.
List1.extend(List2)
print(List1)            #>>>[0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
print(List2)            #>>>[0, 1, 2, 3, 4]


print(">>> List2.pop()")
#.pop() removes value from the end of a list
listPop = List2.pop()   # assings value 4
print(List2)            #>>>[0, 1, 2, 3]
print(listPop)          #>>> 4

print(">>> List2.remove(1)")
# revoves List2[1]
List2.remove(1)
print(List2)            #>>>[0, 2, 3]

print(">>> List2.clear()")
# All clear = erase all value from list
List2.clear()
print(List2)            # >>> []
print(len(List2))       # >>> 0

