'''
Created on 24 Jul 2020

@author: Lilian
'''

import turtle
import math
my_turtle = turtle.Turtle()
my_turtle.showturtle()

####################      WRITE YOUR CODE BELOW      #########################


def draw_triangle():
    for i in 10:
        for j in range(3):
            my_turtle.forward(i * 100)
            my_turtle.right(60)


draw_triangle()

#################### WRITE YOUR CODE ABOVE THIS LINE #########################
####################        IGNORE CODE BELOW        #########################

## Must be the last line of code
my_turtle.screen.exitonclick()
