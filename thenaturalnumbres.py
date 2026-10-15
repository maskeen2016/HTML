numberlist= ('9', '100',' 2000','88', '999', '100000000') 

print("Length of list:", len(numberlist))
print("First Element:", numberlist[0])
print("Last Element:", numberlist[-1])


numberlist.append('100000000')
print("Updated List :", numberlist)

numberlist.remove('9')
print("Updated List :", numberlist)

numberlist.sort()
print("Sorted List:", numberlist)

numberlist.pop(1)
print("Updated List :", numberlist)

numberlist.reverse()
print("Reversed List :", numberlist)

print("Multiplication on List :",numberlist*2)

numberlist = numberlist[0:4]
print("Sliced List :", numberlist)

numberlist.clear()
print("Updated List :", numberlist)