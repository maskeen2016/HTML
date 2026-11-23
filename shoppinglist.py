filename = "shopping_list.txt"
shopping_file = open(filename,"w")

shopping_file.write ("Shopping List\n")
shopping_file.write ("1. Milk\n")
shopping_file.write ("2. Bread\n")
shopping_file.write ("3. Pulses\n")
shopping_file.write ("4. Suger\n")
shopping_file.write ("5. Chocolates\n")
shopping_file.write ("6. Biscuits\n")
shopping_file.write ("7. Surf\n")
shopping_file.write ("2. Dresses\n")
shopping_file.write ("2. Heels\n")
shopping_file.write ("2. Makeup Kits\n")
shopping_file.write ("2. Earrings\n")
shopping_file.write ("2. Chains\n")
shopping_file.write ("1. Sofa\n")
shopping_file.close()

shopping_file = open(filename, "r")
content = shopping_file.read()
print(content)
shopping_file.close()

shopping_file = open(filename, "a")
shopping_file.write("5. Rice\n")
shopping_file.write("6. Butter\n")
shopping_file.close()

line_number = 1

for line in shopping_file:
    print("Line", line_number, ":", line.strip())
    line_number = line_number + 1