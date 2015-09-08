__author__ = 'Mobarak'

#creats list
List1 = ["One", 1, "Two", True]

# Page 228: Accessing List
print(List1[1]) # >>> 1

# Page 229 : Accessing List (cont.)
print(List1[1:3]) # >>> [1, 'Two']


print(List1[1:]) # >>> [1, 'Two', True]

# Page 230 : Accessing List (cont.)
print(List1[:3]) # >>> ['One', 1, 'Two']

# To get last value
print(List1[-1]) # >>> True

print(List1[-2]) # >>> Two

print(List1[1:-1]) # >>> [1, 'Two']