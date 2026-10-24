class Parrot: 


    # class attribute 
    species = "bird" 

    # instance attribute
    def  init_(self, name, age):
     self.name = name 
     self.age = age


     # instantiate the Parrot class 
    blueparrot = Parrot("Bluy", 10) 
    greenyparrot = Parrot("greeny", 15) 


    # access the class attributes 
    print("Blu is a {}".format(blueparrot. species)) 
    print("Woo is also a {}". format(greenyparrot. species)) 


    # access the instance attributes 
    print("{} is {} years old".format( blueparrot.name, blueparrot.age))
    print("{} is {}years old".format( greenyparrot.name, greenyparrot.age))


    # access the instance attributes 
    print("{} is {}years old".format( blueparrot.name, blueparrot.age)) 
    print("{} is {}years old".format( greenyparrot.name, greenyparrot.age)) 