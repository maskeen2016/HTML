from turtle import *

class Face:

 def __init__ (self, xpos, ypos):

  self.size = 90 
  self.coord = (xpos, ypos)
  self.noseSize = 'small'

  def setSize(self, radius): 
    self.size = radius


    def draw(self): 

        self.goHome() 
        pensize(3) 
        speed(ø) 
        self.drawOutline() 
        self.drawEye(135)
        self.drawEye(45) 
        self.drawMouth() 
        self.drawNose() 
        pensize(5)

        def  gohome(self):
           penup
           goto(self.coord) 

        setheading(0)


        def  drawOutline(self):
          penup()
          forward(self.Size)
          left(0)
          pendown()
          circle(self.size)

          self.goHome()
           