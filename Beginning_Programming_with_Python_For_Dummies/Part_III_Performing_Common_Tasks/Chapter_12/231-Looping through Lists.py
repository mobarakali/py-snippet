__author__ = 'Mobarak'
List1 = [1,2,3,4,5]
for item in List1:
    print(item)
"""
>>>1
   2
   3
   4
   5
"""
for item in List1:
    print(item, end=', ')
"""
>>>1, 2, 3, 4, 5,

Probel: output adds extra ',' at the end
"""
# Solved ',' problem
for item in List1:
    if (item == List1[-1]):
        print(item)
    else:
        print(item, end=', ')
"""
Output:
>>>1, 2, 3, 4, 5
"""