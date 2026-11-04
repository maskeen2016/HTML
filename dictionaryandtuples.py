# empty dictionary 
my_dict = {}

# dictionary with integer keys 
my_dict = {

1: 'apple',  
2: 'ball'  
}

# dictionary with mixed keys

my_dict = {

'name': 'Maskeen',    
 1: [2, 3, 4]
}

my_dict = {

'name': 'Baaz',    
'age': '4'
}

# Output: Baaz

print (my_dict ['name'])
print(my_dict.get('age'))

# update value 

my_dict['age'] = 4
print(my_dict)

# add item

my_dict['adress'] = ['Punjab']
print (my_dict)

# remove particular element 
my_dict.pop ('age')
print (my_dict)

# access a particular element 
print ("Adress:",my_dict.get ('adress'))
