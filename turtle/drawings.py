"""
basic drawing
https://docs.python.org/3/library/turtle.html
"""

from turtle import * 

def draw_star():
    """
    draw a five pointed star
    """      
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        right(144) # 144 - 5 pointed, 120 - 3
        if abs(pos()) < 1:
            break
    end_fill()
    done()

def draw_star2():
    """
    draw a star
    """      
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

draw_star()