class Rectangle(): 

     
    def  __init__(self, length, width):
             
      self.length = length 
      self.width = width

    def rectangle_area(self): 
       
       return self.length*self.width



newRectangle = Rectangle(12, 10)


print("Demition of Rectangle Lenght : %d  Width : %d" % (newRectangle.length,newRectangle.width) )

print("Area of Rectangle :", newRectangle.rectangle_area())