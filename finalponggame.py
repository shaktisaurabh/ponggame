from turtle import Screen #Screen class is present in turtle module
from testpaddle1 import paddle#paddle class present in testpaddle1 module is first imported
from ball import ball1#ball1 class in ball module is imported
from pongscore import score#score class in pongscore module is imported
import time

s=Screen()#s is an object of Screen class
s.setup(width=800,height=600)#then the Screen object is set up to width of 800 and height of 600
s.title("pong_game")#then title of Screen is set to pong_game using the title method of Screen class
s.bgcolor("black")#the background color is set to black 
s.tracer(0)#the tracer is set to zero so that the movement of paddle from 0 to edge of x axis cannot be tracked,set to zero and updated after some time do thst movement of the ball can be tracked
l_pad=paddle((-350,0))#object of all respective classes are made noe
r_pad=paddle((350,0))
bs=ball1()
sc=score()
s.listen()#this is to help the screen listen and react to all the screen events
s.onkey(l_pad.move_up,"w")#now the respective methods are called for respective button presses
s.onkey(l_pad.move_down,"z")
s.onkey(r_pad.move_up,"Up")
s.onkey(r_pad.move_down,"Down")
is_on=True
while is_on:#everything put inside the while loop is going to get refreshed every 0.1 seconds
    time.sleep(0.1)#this is to provide a given time delay before the actual update is shown in the movement of ball
    s.update()#then the respective changes are updated everytime after the entire loop is run
    bs.move_ahead()#the ball is then moved ahead without this condition ball would remain stagnant
    if bs.ycor()>280 or bs.ycor()<-280:#when the ball moves either to the extreme north of y-axis or extreme south of y-axis,then ymove starts becoming negetaive
        bs.y_bounce()
    if l_pad.distance(bs)<54 and bs.xcor()<-320 or r_pad.distance(bs)<54 and bs.xcor()>320:#when the ball moves beyond a particular point(320) from the x-axis in either
        #of the directions or within a distance of 54 from the centre of the paddle (square root of 20^2+50^2) the x_direction starts becoming negative
        bs.x_bounce()
    if bs.xcor()>380:#when ball goes out of bound/beyond 380 point on x-axis then the position of ball is reset and the ball then starts travelling
        #along negative x-axis
        bs.reset_again()
        sc.update_left()
    if bs.xcor()<-380:#when ball goes out of bound beyond -380 along x-axis then the position of ball is reset to (0,0) and then the score gets reset
        #and then ball starts travelling on positive x-axis
        bs.reset_again()
        sc.update_right()
s.exitonclick()



