#7.write a python program to check the sizes of given two lists are same.
list_1 = [1, 2, 3, 4, 5]
list_2 = [2, 3, 1, 5, 4]
list_3 = [1, 5, 6, 3, 4]
list_1.sort()
list_2.sort()
list_3.sort()
if list_1 == list_2:
   print("The list_1 and list_2 are the same")
else:
   print("The list_1 and list_2 are not the same")
if list_1 == list_3:
   print("The list_1 and list_3 are the same")
else:
   print("The list_1 and list_3 are not the same")