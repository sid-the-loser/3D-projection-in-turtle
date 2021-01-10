"""
Code written by: Sid The Loser
Refrences from:
    https://en.wikipedia.org/wiki/3D_projection
    https://en.wikipedia.org/wiki/Rotation_matrix
Description from the developer:
    This code took me 2 hours to finish and the whole code was done in a rush...so...I'm sorry if you are having a hard time reading it.
"""

import turtle # This just imports turtle library
import math # This just imports math library

screen = turtle.Screen()
screen.title("")
screen.tracer(0)
screen.bgcolor("black")

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.speed(0)

def draw_point(x, y): # This is a defenition made just to draw a point on the screen...
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.pensize(5)
    pen.forward(1)
    pen.backward(1)
    pen.pensize(1)
    pen.penup()

def draw_line(coord, coord1): # This is a defenition made just to draw a line on the screen...
    pen.penup()
    pen.goto(coord)
    pen.pendown()
    pen.goto(coord1)
    pen.penup()

class CustomError(Exception): # This class is for me to show custom errors
    pass

def rotateX(angle, coords): # This defention does the math to rotate X axis in the 3D coordinates that we pass in...
    X = [

        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]

        ]

    """
    The X on the top there just defines this:
        [ 1,    0,    0]
        [ 0, cosθ, sinθ]
        [ 0, sinθ, cosθ]
    """

    if len(coords) == 3:
        result = []

        for i in range(len(X)): # This part of the code does the multiplication...
            result.append((X[i][0]*coords[0])+(X[i][1]*coords[1])+(X[i][2]*coords[2]))

        return result # Returns the result that we get from the rotation matrix...

    else:
        raise CustomError("'rotateX', function only works with 3D coordinates") # This just raises an error if the length of coord list is not equal to 3...

def rotateY(angle, coords): # This defention does the math to rotate Y axis in the 3D coordinates that we pass in...
    X = [

        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]

        ]

    """
    The X on the top there just defines this:
        [ cosθ, 0, sinθ]
        [    0, 1,    0]
        [-sinθ, 0, cosθ]
    """

    if len(coords) == 3:
        result = []

        for i in range(len(X)): # This part of the code does the multiplication...
            result.append((X[i][0]*coords[0])+(X[i][1]*coords[1])+(X[i][2]*coords[2]))

        return result # Returns the result that we get from the rotation matrix...

    else:
        raise CustomError("'rotateY', function only works with 3D coordinates") # This just raises an error if the length of coord list is not equal to 3...

def rotateZ(angle, coords): # This defention does the math to rotate Z axis in the 3D coordinates that we pass in...
    X = [

        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]

        ]

    """
    The X on the top there just defines this:
        [ cosθ, -sinθ, 0]
        [ sinθ,  cosθ, 0]
        [    0,     0, 1]
    """

    if len(coords) == 3:
        result = []

        for i in range(len(X)): # This part of the code does the multiplication...
            result.append((X[i][0]*coords[0])+(X[i][1]*coords[1])+(X[i][2]*coords[2]))

        return result # Returns the result that we get from the rotation matrix...

    else:
        raise CustomError("'rotateZ', function only works with 3D coordinates") # This just raises an error if the length of coord list is not equal to 3...

def conv_coords(coords): # This defenition is to covert 3D coordinates to 2D coordinates...
    if len(coords) == 3:
        return coords[0], coords[1]
        """This does the same thing as projection matrix but easier:
            Projection Matrix:
                [1, 0, 0]
                [0, 1, 0] * [12, 30, 15] = [12, 30]
                [0, 0, 0]
            My code:
                conv_coords([12, 30, 15]) --> Haha just return the X and Y coordinates --> [12, 30]
        """

    else:
        raise CustomError("'conv_coords', function only works with 3D coordinates") # This just raises an error if the length of coord list is not equal to 3...

verts = ( # This list contains all the 3D coordinates for the verts of the cube...
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = ( # This is the list that stores which all verts to connect to form the edges of the cube...
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

zoom = 50 # This is some lazy way to englarge the cube's size...this will be changes soon...

angle = [0, 0, 0] # This is the angle of the cube...

while True:
    try:
        screen.update()

        pen.clear() # This clears what the pen drew before...

        vert_list = [] # This is to store the 2D coordiates of the cube verts for the edges code to refrence off of...

        for vert in verts:
            x, y = conv_coords(rotateX(angle[0], rotateY(angle[1], rotateZ(angle[2], vert)))) #This line of code rotates the cube vert coordinates and converts them to 2D coordinates for the turtle to display them...
            draw_point(x*zoom, y*zoom) # This just draws a point on the screen using the X and Y coordinates from the complex code given above...
            vert_list.append([x*zoom, y*zoom]) # This is for the edges code given below to reference the 2D coordinates that we get from the cube verts...

        for i in range(len(edges)):
            draw_line(vert_list[edges[i][0]], vert_list[edges[i][1]]) # This is the code that we use to connect all the edges of the cube...

    except Exception as e: # This type of canvas update error managment was taken from my other repository: https://github.com/sid-the-loser/turtle-common-update-error/ ...
        print(e)
        break

quit()

"""
If there is any problem with my code pls report it in the issues tab...or at me on twitter @sid_loser...or DM me on instagram on @sid_the_loser...
"""
