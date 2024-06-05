import unittest
import math
from main import Square, Rectangle, Circle, Triangle, parse_input


class TestShapes(unittest.TestCase):
    def test_parse_input_square(self):
        input_line = "Square TopRight 2 2 Bottomleft 1 1"
        shape = parse_input(input_line)
        self.assertIsInstance(shape, Square)
        self.assertAlmostEqual(shape.perimeter(), 4)
        self.assertAlmostEqual(shape.area(), 1)

    def test_parse_input_square2(self):
        input_line = "Square Side 2 TopRight 2 2"
        shape = parse_input(input_line)
        self.assertIsInstance(shape, Square)
        self.assertAlmostEqual(shape.perimeter(), 8)
        self.assertAlmostEqual(shape.area(), 4)

    def test_parse_input_square_negative(self):
        input_line = "Square TopRight 2 2 Bottomleft -1 -1"
        shape = parse_input(input_line)
        self.assertIsInstance(shape, Square)
        self.assertAlmostEqual(shape.perimeter(), 12)
        self.assertAlmostEqual(shape.area(), 9)

    def test_parse_input_rectangle(self):
        input_line = "Rectangle TopRight 2 2 BottomLeft 1 1"
        shape = parse_input(input_line)
        self.assertIsInstance(shape, Rectangle)
        self.assertAlmostEqual(shape.perimeter(), 4)
        self.assertAlmostEqual(shape.area(), 1)

    def test_parse_input_circle(self):
        input_line = "Circle Center 1 1 Radius 2"
        shape = parse_input(input_line)
        self.assertIsInstance(shape, Circle)
        self.assertAlmostEqual(shape.perimeter(), 2 * math.pi * 2, places=2)
        self.assertAlmostEqual(shape.area(), math.pi * 2**2, places=2)

    def test_parse_input_triangle(self):
        input_line = "Triangle Point1 0 0 Point2 0 3 Point3 4 0"
        shape = parse_input(input_line)
        self.assertIsInstance(shape, Triangle)
        self.assertAlmostEqual(shape.perimeter(), 12)
        self.assertAlmostEqual(shape.area(), 6)


if __name__ == "__main__":
    unittest.main()
