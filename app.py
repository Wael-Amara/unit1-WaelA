""" import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.forward(0)

def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)

def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200)

def right(x):
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right(0)

def rectangle(x):
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
rectangle(0)

def equal():
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
    t.forward(90)
equal()

def message(input):
    print(input)
message("Hello Class")


turtle.done() """

import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(100000)
for i in range(3):
    print(i)

for i in range (0):
    def equal():
        t.forward(90)
        t.left(120)
        t.forward(90)
        t.left(120)
        t.forward(90)
    equal()

def square():
    for i in range(60):
        for i in range(4):
            t.forward(200)
            t.left(90)
        t.left(5)
square()




turtle.done()
