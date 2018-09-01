"""
basic drawing
https://docs.python.org/3/library/turtle.html
"""
import turtle


def draw_star():
    """
    draw a five pointed star
    """
    _turtle = turtle.Turtle()
    _turtle.color('red', 'yellow')
    _turtle.begin_fill()
    while True:
        _turtle.forward(200)
        _turtle.right(144)  # 144 - 5 pointed, 120 - 3
        if abs(_turtle.pos()) < 1:
            break
    _turtle.end_fill()
    turtle.done()


def draw_star2():
    """
    draw a star
    """
    _turtle = turtle.Turtle()
    _turtle.color('red', 'yellow')
    _turtle.begin_fill()
    while True:
        _turtle.forward(200)
        _turtle.left(170)
        if abs(_turtle.pos()) < 1:
            break
    _turtle.end_fill()
    turtle.done()


# draw_star()
draw_star2()
