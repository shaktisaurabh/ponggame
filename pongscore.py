from turtle import Turtle
class score(Turtle):
    def __init__(self):
        super().__init__()#all the methods and attributes of Turtle class can now be accessed by the score class
        self.color("white")#the color of this Turtle/class object would be white as set by using color method
        self.penup()#the pen is put up so as to not draw lines while this turtle is moved
        self.hideturtle()#then the turtle is hidden
        self.lscore=0#lscore and rscore is set to zero and turtle is updated to initial scores
        self.rscore=0
        self.update_score()
    def update_score(self):
        self.goto(-100,200)
        self.write(self.lscore,align="center",font=("Arial", 16, "normal"))
        self.goto(100,200)
        self.write(self.rscore,align="center",font=("Arial", 16, "normal"))
    def update_left(self):
        self.clear()#before update,the score object is cleared up each time before getting updated else it becomes very confusing
        self.lscore+=1
        self.update_score()
    def update_right(self):
        self.clear()
        self.rscore+=1
        self.update_score()