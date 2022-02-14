"""
pytests
"""
from random import randint
import pytest
from modules.geoclass import Point, Rectangle, GuiRectangle

def test_point1():
    """
    Basic test for Point Class
    :return: pass
    """
    pointx = Point(6, 19)
    assert pointx.x == 6
    assert pointx.y == 19

def test_point_type():
    """
    Basic test for Point Class Type
    :return: pass
    """
    assert isinstance(Point(6, 19), Point)

def test_rectangle():
    """
    Basic test for Rectangle Class
    :return: pass
    """
    rectanglex = Rectangle(Point(3, 4), Point(6, 9))
    assert rectanglex.point1.x == 3
    assert rectanglex.point1.y == 4
    assert rectanglex.point2.x == 6
    assert rectanglex.point2.y == 9

def test_rectangle_type():
    """
    Basic test for Rectangle Class Type
    :return: pass
    """
    assert isinstance(Rectangle(Point(3, 4), Point(6, 9)), Rectangle)

def test_guirectangle():
    """
    Basic test for GuiRectangle Class
    :return: pass
    """
    gui_rectangle = GuiRectangle(Point(randint(0, 400), randint(0, 400)), \
                                 Point(randint(10, 400), randint(10, 400)))
    assert isinstance(gui_rectangle, GuiRectangle)
    pytest.skip("skipping this test for now")
