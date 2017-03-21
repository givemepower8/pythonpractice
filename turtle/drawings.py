"""
basic drawing
https://docs.python.org/3/library/turtle.html
"""
import turtle


def draw_star():
    """
    draw a five pointed star
    """
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.right(144) # 144 - 5 pointed, 120 - 3
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()


def draw_star2():
    """
    draw a star
    """
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()

draw_star()
draw_star2()
