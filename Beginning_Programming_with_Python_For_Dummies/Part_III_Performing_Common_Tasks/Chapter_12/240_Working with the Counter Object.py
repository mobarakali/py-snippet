__author__ = 'Mobarak'

from collections import Counter

MyList = [1,2,3,4,1,2,3,1,2,1,5]
ListCount = Counter(MyList)

print(ListCount)

for ThisItem in ListCount.items():
    print("ItemL ", ThisItem[0],
          " Appears: ", ThisItem[1])

print("The value 1 appears {0} times.".format(ListCount.get(3)))


