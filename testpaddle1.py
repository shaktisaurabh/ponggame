from turtle import Turtle
class paddle(Turtle):#Turtle class is the superclass of paddle class
    def __init__(self,pos):#the paddle class by default also has an argument called pos
        super().__init__()#by this all attributes and methods of Turtle class can be used by paddle class
        self.color("white")#the color of turtle becomes white
        self.penup()#the pen is pulled up so that a line is not drawn while the square shaped turtle is moved across different positions on
        #x-axis
        self.shape("square")#the shape of turtle is square
        self.shapesize(stretch_wid=5,stretch_len=1)#default shape of a square is 20 by 20,here the width is increased 5 times to 100 and the length
        #remains same
        self.goto(pos)#then turtle goes to a the given position that is passed above
    def move_up(self):
        y_range=self.ycor()+20#the yaxis is set above by 20 places w.r.t its current position
        self.goto(self.xcor(),y_range)#now the turtle is moved to the respective x and y axis
    def move_down(self):
        y_range=self.ycor()-20#the y_axis is set below 20 places w.r.t its current position now
        self.goto(self.xcor(),y_range)#now the turtle is moved to the respective x and y axis
