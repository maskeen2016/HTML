fruitlist = ['StrawBerry','Cherry','BlackBerry','BlueBerry' ]

print("Length of list:", len(fruitlist))
print("First Element:", fruitlist[0])
print("Last Element:", fruitlist[-1])

fruitlist.append('Cherry')
print("Updated List :", fruitlist)

fruitlist.remove('BlackBerry')
print("Updated List :", fruitlist)

fruitlist.sort()
print("Sorted List:", fruitlist)

fruitlist.pop(1)
print("Updated List :", fruitlist)

fruitlist.reverse()
print("Reversed List :", fruitlist)

print("Multiplication on List :", fruitlist*2)

fruitlist = fruitlist[0:4]
print("Sliced List :", fruitlist)

fruitlist.clear()
print("Updated List :", fruitlist)