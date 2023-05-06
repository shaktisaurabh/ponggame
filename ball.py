from turtle import Turtle#now Turtle class from turtle module is imported
class ball1(Turtle):#Turtle is the super class of ball1 class
    def __init__(self):
       super().__init__()#all the attributes and methods of Turtle class are imported here
       self.shape("circle")#the shape method of Turtle class gets imported here
       self.color("blue")#the color Method of Turtle class gets imported here
       self.penup()#pen is held up so that lines dont get drawn on screen
       self.xmove=10
       self.ymove=10
       self.move_ahead()
       
    def move_ahead(self):
        x_range=self.xcor()+self.xmove#new x_range is initialized by adding the current xcoordinate of the ball with xmove attribute of the class
        y_range=self.ycor()+self.ymove#new y_range is initialized by adding the current ycoordinate of the ball object with ymove attribute of the class
        self.goto(x_range,y_range)#now the object can be sent to the respective coordinates on the x and y axis
    def y_bounce(self):
        self.ymove*=-1#now ymove starts becoming negative the moment it hits the top of screen or bottom of screen
    def x_bounce(self):
        self.xmove*=-1#xmove starts becoming negative when it hits either of the paddles
    def reset_again(self):
        self.goto(0,0)#the position of ball changes to centre the moment it goes out of bound or hits either of the edges
        self.xmove*=-1#and then xmove starts becoming negetaive when it has hit the right-most boundary and starts becoming positive when it has hit the leftmost boundary
        
