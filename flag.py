import math
import time
import sys
import turtle

# To move the origin towards bottom left corner
__x, __y = -360, -390


def drawSun(width):
    sides = 12
    coordinates = []
    b_w = round(0.043038961 * width)
    __h, __k = round(width/4, 0), round(width*(1/(2*math.sqrt(2))), 0)
    x, y = __h+__x, __k+__y
    inside_radius = (5-2*math.sqrt(2))/16*width
    outside_radius = (23-9*math.sqrt(2))/48*width
    angle = 360//sides
    for i in range(sides):
        coordinates.append(
            (int(math.sin(math.radians(i*angle))*inside_radius)+x,
             int(math.cos(math.radians(i*angle))*inside_radius)+y)
        )
        coordinates.append(
            (int(math.sin(math.radians(i*angle+15))*(outside_radius))+x,
             int(math.cos(math.radians(i*angle+15))*(outside_radius))+y)
        )
    return coordinates


def flagBorder(width, t):
    cordinates = []
    b_w = 0
    x, y = __x, __y
    cordinates.append((x, 0+y))
    cordinates.append((b_w+x, round(4 * width / 3.0)+y))
    cordinates.append((width + b_w+x, round(width / math.sqrt(2))+y))
    cordinates.append((round(width - (width / math.sqrt(2))) +
                      b_w+x, round(width / math.sqrt(2)) + y))
    cordinates.append((width + b_w+x, 0+y))
    return cordinates


def blueBorder(width, t):
    cordinates = []
    b_w = round(0.043038961 * width)
    x, y = __x, __y
    cordinates.append((0+x-b_w, 0+y-b_w))
    cordinates.append((0+x-b_w,
                       round(4 * width / 3.0)+y +
                       b_w/math.tan(math.radians(57.94)) +
                       b_w/math.sin(math.radians(57.94))
                       ))
    cordinates.append((width + x +
                       b_w/math.tan(math.radians(32.06)) +
                       b_w/math.sin(math.radians(32.06)),
                       round(width / math.sqrt(2))+y-b_w
                       ))
    cordinates.append((round(width - (width / math.sqrt(2))) + x +
                       b_w*math.sqrt(2)+b_w,
                       round(width / math.sqrt(2)) + y - b_w
                       ))
    cordinates.append((width + x +
                       b_w/math.tan(math.radians(45)) +
                       b_w/math.sin(math.radians(45)),
                       y-b_w
                       ))
    return cordinates


def drawArc(start_angle, end_angle, h, k, radius, screen, begin_fill):
    screen.tracer(0)
    increment = 0.4
    iterate = round((end_angle-start_angle)/increment)
    x, y = 0, 0
    coordinates = []
    for i in range(iterate):
        x = radius*math.cos(math.radians(start_angle))+h
        y = radius*math.sin(math.radians(start_angle))+k
        coordinates.append((x, y))
        start_angle += increment
        t.penup()
        t.goto(x, y)
        t.dot(1)
        if begin_fill:
            t.begin_fill()
            begin_fill = False
        screen.update()
    screen.tracer(1)
    t.penup()
    return (x, y)


def drawSpikes(width):
    sides = 16
    coordinates = []
    __h, __k = round(width/4, 0), round(width*0.84925739539, 0)
    x, y = __h+__x, __k+__y
    inside_radius = round(0.09268434285*width, 0)
    outside_radius = round(0.12871854062*width, 0)
    angle = 360/sides
    for i in range(-6, sides-10):
        coordinates.append(
            (int(math.sin(math.radians(i*angle))*inside_radius)+x,
             int(math.cos(math.radians(i*angle))*inside_radius)+y)
        )
        coordinates.append(
            (int(math.sin(math.radians(i*angle+11.25))*(outside_radius))+x,
             int(math.cos(math.radians(i*angle+11.25))*(outside_radius))+y)
        )
    return coordinates


def drawMoon(width, t):
    # Moon's upper facing upper arc
    b_w = 0
    __h, __k = round(width/4, 0), round(1.0202200572*width, 0)
    x, y = __x+b_w+__h, __y+b_w + __k
    __radius = round(0.2140016237*width, 0)
    end_x, end_y = drawArc(201.4559, 338.5441,
                           x, y,
                           __radius, screen, True)
    # Moon's upper facing lower arc
    __h, __k = round(width/4, 0), round(0.94194173824*width, 0)
    x, y = __x+b_w+__h, __y+b_w + __k
    __radius = round(0.199171282*width, 0,)
    drawArc(180, 360,
            x, y,
            __radius, screen, False)
    # Moon's down facing
    t.goto(end_x, end_y)
    t.dot(1)
    t.end_fill()


turtle.setup(width=800, height=1000)
t = turtle.Turtle()
t.width(2)
t.shape("arrow")
t.shapesize(0.5, 0.5)
turtle.bgcolor("black")
screen = turtle.Screen()
time.sleep(2)
flag_widht = 600

# Draw the outline
vertices_outline = flagBorder(flag_widht, t)
t.penup()
t.color(220/255, 20/255, 60/255)
t.goto(vertices_outline[0])
t.pendown()
t.fillcolor(220/255, 20/255, 60/255)
t.begin_fill()  # Begin the fill
for vertex in vertices_outline[1:]:
    t.goto(vertex)
t.goto(vertices_outline[0])
t.end_fill()  # End the fill

vertices_outline_1 = blueBorder(flag_widht, t)
t.penup()
t.color(0, 0, 145/255)
t.goto(vertices_outline[0])
t.pendown()
t.fillcolor(0, 0, 145/255)
t.begin_fill()  # Begin the fill
for vertex in vertices_outline_1[:]:
    t.goto(vertex)
t.goto(vertices_outline_1[0])
t.speed(10)
for vertex in vertices_outline:
    t.goto(vertex)
t.goto(vertices_outline[0])
t.end_fill()  # End the fill
t.speed(3)

# Draw the sun
vertices_sun = drawSun(flag_widht)
t.penup()
t.color("white")
t.goto(vertices_sun[0])
t.pendown()
t.fillcolor("white")
t.begin_fill()
for vertex in vertices_sun[1:]:
    t.goto(vertex)
t.goto(vertices_sun[0])
t.end_fill()
t.penup()

drawMoon(flag_widht, t)
vertices_spikes = drawSpikes(flag_widht)
t.penup()
t.color("white")
t.goto(vertices_spikes[0])
t.pendown()
t.begin_fill()
for vertex in vertices_spikes[1:]:
    t.goto(vertex)
t.goto(vertices_spikes[0])
t.end_fill()
t.penup()
t.penup()
t.hideturtle()
# Close the Turtle window when clicked
turtle.exitonclick()
