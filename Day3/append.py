list1 = [1,3,2]
list2 =[5]
list_add = list1+list2


def add(element):
    if type(element) != list:
        newList = [element]
        finalList = list1+newList
    else:
        finalList = list1+element
    return finalList

print(list_add)
result = add([2,3,4,5])
result1 = add(23)
list1 = result
print(result)
print(result1)
print(type(result))
print(type(result1))

