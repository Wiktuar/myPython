input = [15, 'abc', 25, 'kml']

list1 = [i for i in input if str(i).isdigit() == True]
list2 = [i for i in input if str(i).isdigit() == False]
print(list1)
print(list2)

