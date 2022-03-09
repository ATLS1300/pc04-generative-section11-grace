#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:22:51 2021

@author: LaurenPark
"""

import turtle, math
import turtle, random

turtle.speed(550)

panel=turtle.Screen() #panel set up
w=600
h=600
panel.setup(width=w, height=h)

#pseudocode initially indicated a while loop of circles, though after consideration I decided to use the larger portion of my PCO3 spirograph as the center of my piece and then added another for loop to incorporate a circle design around the other spirograph 

t=turtle.Turtle() #2 turtles

t2=turtle.Turtle()

colors= turtle.color()

colors=["#B24C63", "#5438DC", "#357DED", "#56EEF4", "#32E875", "#F28123", "#FFF072"]
#HEX colors
t2.up()
t.up()

size = 75 #PC03 addition
sides = 8
angle = 360/sides

inc = 10 
numIt = int(360/inc) 
innerCirc = 20 

t2.goto(0,130)  #Spirograph used from PCO3. Color and position changed
                #random.choice used to create rainbow spiro
t2.speed(500)
for i in range(numIt):
    turtle.down()
    for i in range(sides):
        t2.down()
        t2.color(random.choice(colors))
        t2.forward(size)
        t2.right(angle)
    t2.up()
    t2.forward(innerCirc)
    t2.right(inc)

t.goto(0,0)
size=15
t.width(5)
angle=360/sides
inc=10
numIt= int(360/inc)
innerCirc = 6


t.up()    
t.goto(-5,60)
t.down()         #Second For Loop / Random integration
t.speed(300)
for i in range(7):
    t.color(colors[i])
    random.choice(colors)
    t.width(3)
    t.forward(25)
    size += 1
    print(size)
    t.circle(65)
    t.forward(size)
    t.right(angle)
    t.forward(innerCirc)
    t.right(inc)
    
t.up()      #3rd loop from PCO3 spirograph
size = 30
sides = 4 
angle = 180/sides

inc = 10 
numIt = int(360/inc)
innerCirc = 20 
t.goto(15,-145) 

t.down()   #Also pulled from PCO3. Random.choice used for random color
for i in range(numIt):
    turtle.down()
    for i in range(sides):
        t.color(random.choice(colors))
        t.width(1)
        t.forward(size)
        t.right(angle)
    t.forward(innerCirc)
    t.right(inc)

size = 25    #Last For loop (PCO3) 
sides = 4 
angle = 180/sides

inc = 10 
numIt = int(360/inc)
innerCirc = 20 
t2.up()
t2.goto(0,230) 

for i in range(numIt):
    t2.down()
    for i in range(sides):
        t2.color(random.choice(colors))
        t2.width(1)
        t2.forward(size)
        t2.right(angle)
    t2.forward(innerCirc)
    t2.right(inc)
#all done
    
    
    
    
