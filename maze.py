import turtle
#pointer
p=turtle.Turtle()
sp=turtle.Turtle()
sp.penup()
sp.goto(-100,230)
p.speed(1000) #speed of movements
#screen
s=turtle.Screen()
#adding background
s.bgpic("d:/pygame/mazegame/big.png")

#customising spaceman
s.addshape("d:/pygame/mazegame/a1.gif")
sp.shape("d:/pygame/mazegame/a1.gif")

#customising pointer(works better with gif)
s.addshape("d:/pygame/mazegame/r.gif")
p.shape("d:/pygame/mazegame/r.gif")

p.penup()
p.goto(180,-250)
#up func
def up():
    p.setheading(90)
    p.forward(10)
    p.setheading(0)
#down func
def down():
    p.setheading(270)
    p.forward(10)
    p.setheading(0)
#right func
def right():
   p.forward(10)
#left func    
def left():
    p.setheading(180)
    p.forward(10)
    p.setheading(0)


#movements
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
turtle.listen()

#accomplishment
while True:      
    s.update()  #updating screen 
    if p.distance(sp)<10:
        s.bgpic("d:/pygame/mazegame/end.png")


turtle.done()
