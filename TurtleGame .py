#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import turtle 
import time as t
from turtle import Turtle
import random
from random import randint

#window front end scene
widwo= turtle.Screen()
widwo.title("2D Race Game")
turtle.bgcolor("black")
turtle.color("yellow")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,210)
turtle.write("2D Racing Game", font = ("Arial" , 22 ,"bold"))
turtle.penup()

 #underground setup
turtle.setpos(-400,-180)
turtle.color("forestgreen")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#finshing point for players
stamp_sze=20
square_sze=15
finish_lne=200
turtle.color("violet")
turtle.shape("square")
turtle.shapesize(square_sze / stamp_sze)
turtle.penup()

for i in range(12):
                   turtle.setpos(finish_lne,(175 -(i * square_sze * 2)))
                   turtle.stamp()
turtle.hideturtle()

#there are three turtles in this program
   #turtlei
turtlei=Turtle()
turtlei.speed(0)
turtlei.color("orange")
turtlei.shape("turtle")
turtlei.penup()
turtlei.goto(-250,150)
turtlei.pendown()

   #turtlej
turtlej=Turtle()
turtlej.speed(0)
turtlej.color("red")
turtlej.shape("turtle")
turtlej.penup()
turtlej.goto(-250,120)
turtlej.pendown()

  #turtlek
turtlek=Turtle()
turtlek.speed(0)
turtlek.shape("turtle")
turtlek.color("purple")
turtlek.penup()
turtlek.goto(-250,90)
turtlek.pendown()

t.sleep(1)
for i in range(142):
    turtlei.forward(randint(1,5))
    turtlej.forward(randint(1,5))
    turtlek.forward(randint(1,5))
    turtlei_pos_x = turtlei.position()[0];
    turtlej_pos_x = turtlej.position()[0];
    turtlek_pos_x = turtlek.position()[0];
#     print(turtlei_pos_x, turtlej_pos_x, turtlek_pos_x);
    if turtlei_pos_x > 180:
        turtle.setpos(-140,-80)
        turtle.write("Turtle i won", font = ("Arial" , 28 ,"bold"))
        break
    elif turtlej_pos_x > 180:
        turtle.setpos(-140,-80)
        turtle.write("Turtle j won", font = ("Arial" , 28 ,"bold"))
        break
    elif turtlek_pos_x > 180:
        turtle.setpos(-140,-80)
        turtle.write("Turtle k won", font = ("Arial" , 28 ,"bold"))
        break;

turtle.exitonclick()


# In[ ]:




