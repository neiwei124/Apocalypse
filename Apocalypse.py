#######################################################################
# Title: Apocalypse                                                   #
# Programmer: Neien Wei                                               #
# Last Modified: May 15, 2015                                         #
# Description: As you watch this animation, you will be mesmerized by #
#              the beauty of this animation.                          #
#######################################################################

from tkinter import *
from random import *
from time import *
from math import *
myInterface = Tk()
screen = Canvas(myInterface, width=1000, height=800, background="SkyBlue")
screen.pack()

#background
screen.create_rectangle(0, 500, 1000, 800, fill="forestgreen")
house = screen.create_rectangle(775, 525, 900, 600, fill="beige")
roof = screen.create_polygon(775, 525, 840, 475, 900, 525, fill="blue")
window = screen.create_rectangle(835, 535, 880, 560, fill="cyan", outline="yellow", width=5)
mountain = screen.create_polygon(200, 500, 800, 500, 650, 275, 350, 275, fill="SaddleBrown", outline="black")
door = screen.create_rectangle(785, 550, 825, 600, fill="purple")

#mountain rumbling
x=400
y=200
x1=x+200
for f in range(200, 216):
    yM = f + 20*sin(10*f)
    Mtop = screen.create_polygon(x, yM, x1, yM, 650, 275, 350, 275, fill="white")
    screen.update()
    sleep(0.05)
    screen.delete(Mtop)

#smoke creating
smoke=[]
for f in range(0, 80):
    screen.create_polygon(x, y, x1, y, 650, 275, 350, 275, fill="white")
    x2 = 405 + 15*sin(0.3*f)               
    y1 = 195 + -4*f 
    x3 = x2 + 185
    y2 = y1 + 10
    smoke.append(screen.create_oval(x2, y1, x3, y2, fill="grey", outline="grey"))
    screen.update()
    sleep(0.05)

for f in range(0, 175):
#cloud 1
    x=5*f+(-1300)
    y=0
    x1=x+1300
    y1=y+50
    cloud=screen.create_oval(x, y, x1, y1, fill="DimGray")
#cloud 2
    x2=5*f+(-1200)
    y2=50
    x3=x2+1100
    y3=y2+40
    cloud1=screen.create_oval(x2, y2, x3, y3, fill="DimGray")
#cloud 3
    x4=-5*f+1200
    y4=0
    x5=x4+1100
    y5=y4+75
    cloud2=screen.create_oval(x4, y4, x5, y5, fill="DimGray")
#cloud 4
    x6=-5*f+1000
    y6=75
    x7=x6+1100
    y7=y6+35
    cloud3=screen.create_oval(x6, y6, x7, y7, fill="DimGray")
    screen.update()
    sleep(0.05)
    screen.delete(cloud, cloud1, cloud2, cloud3)

screen.create_oval(x, y, x1, y1, fill="DimGray")
screen.create_oval(x2, y2, x3, y3, fill="DimGray")
screen.create_oval(x4, y4, x5, y5, fill="DimGray")
screen.create_oval(x6, y6, x7, y7, fill="DimGray")
sleep(0.75)

#stickman
for f in range(0, 50):
    #face
    x=-3*f+790
    y=550
    x1=x+25
    y1=y+25
    #body
    x2=x+12.5
    y2=y1+15
    #arm
    y3=y+30
    #foot
    y4=y2+10

    face=screen.create_oval(x,y,x1,y1, fill="black")
    body=screen.create_line(x2, y1, x2, y2)
    arm=screen.create_line(x, y3, x1, y3)
    foot=screen.create_line(x, y4, x2, y2, x1, y4)

    screen.update()
    sleep(0.05)
    screen.delete(face, body, arm, foot)

face=screen.create_oval(x,y,x1,y1, fill="black")
body=screen.create_line(x2, y1, x2, y2)
arm=screen.create_line(x, y3, x1, y3)
foot=screen.create_line(x, y4, x2, y2, x1, y4)

#question mark
for f in range(0, 15):
    #wiggly part
    a=-25*f+1000
    b= 508
    a1=a+15
    b1=b+10
    a2=a+7.5
    b2=b+25
    #circle part
    c=a+7
    d=b+30
    c1=a+8
    d1=b+35
    wp=screen.create_line(a,b,a1,b,a1,b1,a2,b1,a2,b2, width=3)
    circle=screen.create_oval(c,d,c1,d1,fill="black")
    screen.update()
    sleep(0.05)
    screen.delete(wp, circle)        

wp=screen.create_line(a,b,a1,b,a1,b1,a2,b1,a2,b2, width=3)
circle=screen.create_oval(c,d,c1,d1,fill="black")
screen.delete(wp, circle)

#delete smoke
for f in range(0,80):
    screen.delete(smoke[f])
sleep(3)

#lava
for f in range(0,30):
    #1
    x=410
    y=200
    x1=-2.5*f+x
    y1=5*f+y

    #2
    x2=440
    x3=-2*f+x2
    y2=7*f+y

    #3
    x4=470+8*sin(0.5*f) 
    y3=5*f+y
    x5=x4+5
    y4=y3+10

    #4
    x6=500
    x7=f+x6
    y5=3*f+y

    #5
    x8=530
    x9=1.5*f+x8
    y6=7*f+y

    #6
    x10=560+8*sin(0.5*f) 
    y7=8*f+y
    x11=x10+8
    y8=y7+15

    #7
    x12=590
    x13=2.5*f+x12
    y9=6*f+y

    lava=screen.create_line(x,y,x1,y1,fill="red", width=3)
    lava1=screen.create_line(x2,y,x3,y2,fill="red", width=3)
    lava2=screen.create_oval(x4,y3,x5,y4,fill="red", outline="red")
    lava3=screen.create_line(x6,y,x7,y5,fill="red", width=3)
    lava4=screen.create_line(x8,y,x9,y6,fill="red", width=3)
    lava5=screen.create_oval(x10,y7,x11,y8,fill="red", outline="red")
    lava6=screen.create_line(x12,y,x13,y9,fill="red", width=3)
    screen.update()
    sleep(0.05)

#booom
for f in range(0,75):
    #boom
    x=400
    y=-25
    x1=x+200
    y1=200

    #boom lines1
    for s in range(0,10):
        x2=randint(400, 600)
        y2=-3*s+randint(0, 200)
        y3=y2-10

    #boom lines2    
    for s in range(0,10):
        a=randint(400, 600)
        b=-3*s+randint(0, 200)
        c=y2-10

    #boom lines3
    for s in range(0,10):
        d=randint(400, 600)
        e=-3*s+randint(0, 200)
        f=y2-10

    colour=["red", "orange", "yellow"]
    co=choice(colour)
    kaboom=screen.create_rectangle(x,y,x1,y1,fill=co)
    line=screen.create_line(x2,y2,x2,y3)
    line1=screen.create_line(a,b,a,c)
    line2=screen.create_line(d,e,d,f)
    screen.update()
    sleep(0.05)
    screen.delete(kaboom, line, line1, line2)

#stickman running away
exclamation=screen.create_line(655, 530, 655, 510, width=8)
point=screen.create_oval(650, 535, 660, 543, fill="black")
screen.update()
sleep(1)
screen.delete(exclamation, point, face, body, arm, foot)
for f in range(0, 50):
    x=-50*f+643
    y=550
    x1=x+25
    y1=y+25
    #body
    x2=x+12.5
    y2=y1+15
    #arm
    y3=y+30
    #foot
    y4=y2+10

    face=screen.create_oval(x,y,x1,y1, fill="black")
    body=screen.create_line(x2, y1, x2, y2)
    arm=screen.create_line(x, y3, x1, y3)
    foot=screen.create_line(x, y4, x2, y2, x1, y4)

    screen.update()
    sleep(0.05)
    screen.delete(face, body, arm, foot)

#lava rain
numFlakes = 500
windSpeed = 1

flakes = []
xSpeeds = []
ySpeeds = []
xPos = []
yPos = []
xStart = []
yStart = []
sizes = []
t = []

for n in range(0,numFlakes):
    xPos.append(0)
    yPos.append(0)
    xSpeeds.append( windSpeed )
    ySpeeds.append( randint(2,4))
    xStart.append( randint(-200,1000))
    yStart.append( randint(-600, 0))
    sizes.append( randint(1,6) )
    flakes.append(0)
    t.append(0)
    
for frameCount in range(0,750):
    for n in range(0, numFlakes):
        xPos[n] = xSpeeds[n] * t[n] + xStart[n]
        yPos[n] = ySpeeds[n] * t[n] + yStart[n]
        flakes[n] = screen.create_line(xPos[n],yPos[n],xPos[n]+sizes[n],yPos[n]+sizes[n], fill="red", width=3)
        t[n] = t[n] + 1

    screen.update()
    sleep(0.005)

    for n in range(0, numFlakes):
        screen.delete( flakes[n])

#more volcano rocks
streak=[]
for f in range(0,25):
    #rock
    x=450
    y=-40*f+125
    x1=x+100
    y1=y+60

    #streak
    x2=460
    y2=y+40
    x3=540
    y3=200
    streak.append(screen.create_rectangle(x2,y2,x3,y3,fill="red", outline="red"))
    rock=screen.create_oval(x,y,x1,y1,fill="DimGray")
    screen.update()
    sleep(.05)
    screen.delete(rock)
    
for f in range(0,25):
    screen.delete(streak[f])
sleep(.5)

for f in range(0,26):
    #rock
    x=-3*f+200
    y=20*f+(-40)
    x1=x+40
    y1=y+40

    #streak
    x2=-3*f+220
    y2=y+20
    x3=210
    y3=-80
    streak=screen.create_line(x2,y2,x3,y3,fill="red", width=3)
    rock=screen.create_oval(x,y,x1,y1,fill="DimGray")
    screen.update()
    sleep(.05)
    screen.delete(rock, streak)

for f in range(0,20):
    colour=["red","blue", "yellow", "orange"]
    c=choice(colour)
    boom=screen.create_polygon(50, 500, 35, 425,65, 450,100, 350, 125, 400, 185, 375, 175, 500, fill=c, outline="black", width=2)
    screen.update()
    sleep(.05)
    screen.delete(boom)

streak=[]
for f in range(0,25):
    #rock
    x=450
    y=-40*f+125
    x1=x+100
    y1=y+60

    #streak
    x2=460
    y2=y+40
    x3=540
    y3=200
    streak.append(screen.create_rectangle(x2,y2,x3,y3,fill="red", outline="red"))
    rock=screen.create_oval(x,y,x1,y1,fill="DimGray")
    screen.update()
    sleep(.05)
    screen.delete(rock)
    
for f in range(0,25):
    screen.delete(streak[f])
sleep(.5)

for f in range(0,30):
    #rock
    x=3*f+675
    y=20*f+(-40)
    x1=x+80
    y1=y+80

    #streak
    x2=3*f+705
    y2=y+20
    x3=685
    y3=-80
    streak=screen.create_line(x2,y2,x3,y3,fill="red", width=10)
    rock=screen.create_oval(x,y,x1,y1,fill="DimGray")
    screen.update()
    sleep(.05)
    screen.delete(rock, streak)
    
for f in range(0,20):
    colour=["red","blue", "yellow", "orange"]
    c=choice(colour)
    boom=screen.create_polygon(750, 625, 775, 585, 750, 550, 775, 525, 750, 475, 775, 450, 825, 465, 875, 450, 925, 500, 900, 550, 925, 600, 885, 625, 825, 615, fill=c, outline="black", width=5)
    screen.update()
    sleep(.05)
    screen.delete(boom, house, roof, door, window)

debris=screen.create_polygon(775, 600, 775, 550, 800, 590, 825, 565, 850, 575, 875, 570, 885, 575, 900, 550, 900, 600, fill="black")
screen.update()
sleep(1)

streak=[]
for f in range(0,25):
    #rock
    x=450
    y=-40*f+125
    x1=x+100
    y1=y+60

    #streak
    x2=460
    y2=y+40
    x3=540
    y3=200
    streak.append(screen.create_rectangle(x2,y2,x3,y3,fill="red", outline="red"))
    rock=screen.create_oval(x,y,x1,y1,fill="DimGray")
    screen.update()
    sleep(.05)
    screen.delete(rock)
    
for f in range(0,25):
    screen.delete(streak[f])
sleep(0.5)    

for f in range(0,80):
    #rock
    x=-100
    y=100*f+(-800)
    x1=1100
    y1=y+1000

    #streak
    x2=100
    y2=y+300
    x3=900
    y3=y2-3000
    streak=screen.create_rectangle(x2,y2,x3,y3,fill="red", outline="red")
    rock=screen.create_oval(x,y,x1,y1,fill="DimGray")
    screen.update()
    sleep(.05)
    screen.delete(rock, streak)

for f in range(0,20):
    colour=["red","blue", "yellow", "orange"]
    c=choice(colour)
    boom=screen.create_polygon(0, 900, -50, 700, 100, 750, 250, 700, 400, 725, 550, 650, 700, 725, 850, 675, 950, 750, 1025, 700, 1000, 900, fill=c, outline="black", width=5)
    screen.update()
    sleep(.05)
    screen.delete(boom)

#UFO
r=-100
position=250
for f in range(0,100):
    #glass part
    x=15*f+(r-50)
    y=0.05*f**2-4*f+(position-50)
    x1=x+100
    y1=y+100

    #rest of the ufo parts
    x2=15*f+(r+100)
    x3=15*f+(r-100)
    y2=y+50
    y3=0.05*f**2-4*f+(position+55)

    #beam
    x4=15*f+(r-34.5)
    y4=200
    x5=x+75
    y5=y4+500
    colour=["red","blue", "yellow", "orange", "green", "SaddleBrown", "black", "blanchedAlmond"]
    c=choice(colour)

    #random damaged terrain lines
    for f in range(0,30):
        xrange=int(x4-15)
        yrange=int(y5-20)
        xrange1=int(x5+15)
        yrange1=int(y5+20)
        x6=randint(xrange, xrange1)
        y6=randint(yrange, yrange1)
        x7=randint(xrange, xrange1)
        y7=randint(yrange, yrange1)
        screen.create_line(x6,y6,x7,y7, fill="black")
        
    beam=screen.create_rectangle(x4,y4,x5,y5, fill=c)
    glass=screen.create_oval(x,y,x1,y1, fill="cyan")
    rest=screen.create_polygon(x,y2,x1,y2,x2,y3,x3,y3,fill="purple")
    screen.update()
    sleep(.05)
    screen.delete(glass,rest, beam)
sleep(2)

screen.create_rectangle(0,0,1000,800,fill="black")
screen.create_text(500,400, text="Then the earth blew up and everyone died. The End.", font="ComicSansMS 40", fill="red")
screen.update()
