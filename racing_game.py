import turtle
import random
w=1000
h=1000
win=turtle.Screen()
win.setup(w,h)
win.bgcolor("black")

def createTurtle(shape,color,size,x,y):
  t=turtle.Turtle()
  t.shape(shape)
  t.color(color)
  t.shapesize(size,size,size)
  t.penup()
  t.goto(x,y)
  t.speed(0)
  return t
Giraffe=createTurtle("turtle","white",2,-350,300)
Giraffe.pendown()
Giraffe.goto(-350,-300)
Giraffe.penup()
Giraffe.goto(350,300)
Giraffe.pendown()
Giraffe.goto(350,-300)
Giraffe.penup()
bird= createTurtle("turtle","green",2,-400,100)
turt1e_jr= createTurtle("turtle", "green",2,-400,-100) 
turt1e_jr.pendown()
bird.pendown()
colors=["green","grey","white","blue","red","orange","brown"]
speeds=[0,1,10,23,25,68,-5,30,45,-8,-7,-1,21,13,19,59]
racelength=750
birddistance=0
turt1e_jrdistance=0

while turt1e_jrdistance<=racelength and birddistance<=racelength:
    birdspeed=random.choice(speeds)
    turt1e_jrspeed=random.choice(speeds)
    bird.forward(birdspeed)
    turt1e_jr.forward(turt1e_jrspeed)
    bird.color(random.choice(colors))
    turt1e_jr.color(random.choice(colors))
    birddistance+=birdspeed
    turt1e_jrdistance+=turt1e_jrspeed
Giraffe.goto(-100,0)
Giraffe.hideturtle()
MYFONT=("ariel",15,"normal")
if birddistance > turt1e_jrdistance:
    Giraffe.write("congradulations BIRD!!!!!!!!!!!!",font=MYFONT)
    Giraffe.goto(-75,-25)
    Giraffe.write("distance:"+str(birddistance),font=MYFONT)
else:
    Giraffe.write("congradulations turt1e jr!!!!!!!!!!",font=MYFONT)
    Giraffe.goto(-75,-25)
    Giraffe.write("distance:"+str(turt1e_jrdistance),font=MYFONT)

turtle.mainloop()
