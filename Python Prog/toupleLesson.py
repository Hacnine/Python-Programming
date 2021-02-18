#to change the value of touple

thisToupel = ("apple", "banana", "cherry")
newList = list(thisToupel)
newList[1] = "mango"
backToTauple = tuple(newList)
print(backToTauple)
lenght = len(backToTauple)
print(lenght)

for item in backToTauple:
    print(item)

oneItem = ('one',)
oneItem.__class_getitem__()
print(oneItem)
#it can not be toupe because of commas

oneItem = ('one')
print(oneItem)
