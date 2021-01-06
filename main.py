"""
Code written by: Sidharth S
Refrences from:
    https://en.wikipedia.org/wiki/3D_projection#:~:text=A%203D%20projection%20(or%20graphical,capability%20on%20a%20simpler%20plane.
    https://en.wikipedia.org/wiki/Rotation_matrix
"""

import turtle
import math

def projection_matrix(coords):
    return coords[0], coords[1]

screen = turtle.Screen()
screen.title("")
screen.tracer(0)
screen.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.speed(0)

def draw_point(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.pensize(5)
    pen.forward(1)
    pen.backward(1)
    pen.pensize(1)
    pen.penup()

def draw_line(coord, coord1):
    pen.penup()
    pen.goto(coord)
    pen.pendown()
    pen.goto(coord1)
    pen.penup()

class CustomError(Exception):
    pass

def rotateX(angle, coords):
    coords = list(coords)
    X = [

        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]

        ]
    if len(coords) == 3:
        result = []

        for i in range(len(X)):
            result.append((X[i][0]*coords[0])+(X[i][1]*coords[1])+(X[i][2]*coords[2]))

        return result

    else:
        raise CustomError("'rotateX', function only works with 3D coordinates")

def rotateY(angle, coords):
    coords = list(coords)
    X = [

        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]

        ]
    if len(coords) == 3:
        result = []

        for i in range(len(X)):
            result.append((X[i][0]*coords[0])+(X[i][1]*coords[1])+(X[i][2]*coords[2]))

        return result

    else:
        raise CustomError("'rotateY', function only works with 3D coordinates")

def rotateZ(angle, coords):
    coords = list(coords)
    X = [

        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]

        ]
    if len(coords) == 3:
        result = []

        for i in range(len(X)):
            result.append((X[i][0]*coords[0])+(X[i][1]*coords[1])+(X[i][2]*coords[2]))

        return result

    else:
        raise CustomError("'rotateZ', function only works with 3D coordinates")

def conv_coords(coords):
    if len(coords) == 3:
        return coords[0], coords[1]

    else:
        raise CustomError("'conv_coords', function only works with 3D coordinates")

zoom = 50

verts = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

angle = 0

while True:
    try:
        screen.update()

        pen.clear()

        vert_list = []

        for vert in verts:
            x, y = conv_coords(rotateX(angle, rotateY(angle, rotateZ(angle, vert))))
            draw_point(x*zoom, y*zoom)
            vert_list.append([x*zoom, y*zoom])

        for i in range(len(edges)):
            draw_line(vert_list[edges[i][0]], vert_list[edges[i][1]])

        angle += 0.001

    except:
        break

quit()
