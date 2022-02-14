"""
main geometry app
"""
from random import randint
import turtle
from modules import Point, Rectangle, GuiRectangle

# Create rectangle object
rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
              Point(randint(10, 19), randint(10, 19)))


# Draw rectangle object
gui_rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)),
              Point(randint(10, 400), randint(10, 400)))

myturtle = turtle.Turtle()
gui_rectangle.draw(canvas=myturtle)
turtle.done()

# Print rectangle coordinates
# print("Rectangle Coordinates: ",
#       rectangle.point1.x, ",",
#       rectangle.point1.y, "and",
#       rectangle.point2.x, ",",
#       rectangle.point2.y)
#
# # Get point and area from user
# user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
# user_area = float(input("Guess rectangle area: "))
#
# # Print out the game result
# print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
# print("Your area was off by: ", rectangle.area() - user_area)
