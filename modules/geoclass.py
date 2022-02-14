"""
classes for geometry app
"""
class Point:
    """
    This is a Point Class
    """
    def __init__(self, x, y):
        self.x = x  #pylint .....
        self.y = y

    def falls_in_rectangle(self, rectangle):
        """
        This method takes a rectangle object as the argument and returns
        True or False if the Point object falls inside the Rectangle object
        :param rectangle: Rectangle object with lower left and upper left Point objects
        :type rectangle: Rectangle
        :return: True or False
        :rtype: Boolean
        """
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        return False

    def dummy_method(self):
        """
        this is a dummy method
        :return:
        """


class Rectangle:
    """
    This is a rectangle class
    """
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        """
        This method calculates the area of the rectangle object and returns a float
        :param self: rectangle object consisting of two point objects
        :type self: Rectangle
        :return: float calculation of area of rectangle
        :rtype: float
        """
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)

    def dummy_method(self):
        """
        this is a dummy method
        :return:
        """

class GuiRectangle(Rectangle):
    """
    This method takes a guirectangle object as the argument and returns
    True or False if the Point object falls inside the Rectangle object
    :param rectangle: Rectangle object with lower left and upper left Point objects
    :type rectangle: GuiRectangle
    :return: True or False
    :rtype: Boolean
    """
    def draw(self, canvas):
        """
        This is a draw method
        :param canvas:
        :return: turtle
        """
        # do not write to screen
        canvas.penup()

        # move pen to the point coordinates
        canvas.goto(self.point1.x, self.point1.y)

        # start writing to screen
        canvas.pendown()

        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
