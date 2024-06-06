import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass




class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

    def perimeter(self):
        return (self.side1 + self.side2)*2


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side1=side, side2=side)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p*(p - self.side1)*(p - self.side2)*(p - self.side3))


def parse_input(input_line):
    parts = input_line.split()
    parts = [part.lower() for part in parts]
    shape_type = parts[0]

    if shape_type == "square":
        if "side" in parts:
            side_index = parts.index("side") + 1
            side = float(parts[side_index])
            return Square(side)

        elif "topright" in parts and "bottomleft" in parts:
            tr_index = parts.index("topright") + 1
            bl_index = parts.index("bottomleft") + 1
            top_right_x, top_right_y = float(parts[tr_index]), float(parts[tr_index + 1])
            bottom_left_x, bottom_left_y = float(parts[bl_index]), float(parts[bl_index + 1])
            side = top_right_x - bottom_left_x
            return Square(side)
        elif "topleft" in parts and "bottomright" in parts:
            tl_index = parts.index("topleft") + 1
            br_index = parts.index("bottomright") + 1
            top_left_x, top_left_y = float(parts[tl_index]), float(parts[tl_index + 1])
            bottom_right_x, bottom_right_y = float(parts[br_index]), float(parts[br_index + 1])
            side = bottom_right_x - top_left_x
            return Square(side)

    elif shape_type == "rectangle":
        if "side1" and "side2" in parts:
            side1_index = parts.index("side1") + 1
            side1 = float(parts[side1_index])
            side2_index = parts.index("side2") + 1
            side2 = float(parts[side2_index])
            return Rectangle(side1, side2)

        elif "topright" in parts and "bottomleft" in parts:
            tr_index = parts.index("topright") + 1
            bl_index = parts.index("bottomleft") + 1
            top_right_x, top_right_y = float(parts[tr_index]), float(parts[tr_index + 1])
            bottom_left_x, bottom_left_y = float(parts[bl_index]), float(parts[bl_index + 1])
            side1 = top_right_x - bottom_left_x
            side2 = top_right_y - bottom_left_y
            return Rectangle(side1, side2)

    elif shape_type == "circle":
        if "radius" in parts:
            radius_index = parts.index("radius") + 1
            radius = float(parts[radius_index])
            return Circle(radius)
        elif "point" in parts and "center" in parts:
            point_index = parts.index("point") + 1
            center_index = parts.index("center") + 1
            center_x, center_y = float(parts[center_index]), float(parts[center_index + 1])
            point_x, point_y = float(parts[point_index]), float(parts[point_index + 1])
            radius = math.sqrt(
                (point_x - center_x) ** 2 + (point_y - center_y) ** 2)
            return Circle(radius)

    elif shape_type == "triangle":
        p1_index = parts.index("point1") + 1
        p2_index = parts.index("point2") + 1
        p3_index = parts.index("point3") + 1
        x1, y1 = float(parts[p1_index]), float(parts[p1_index + 1])
        x2, y2 = float(parts[p2_index]), float(parts[p2_index + 1])
        x3, y3 = float(parts[p3_index]), float(parts[p3_index + 1])
        side1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        side2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        side3 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
        return Triangle(side1, side2, side3)

    else:
        raise ValueError("Unknown shape type")


def main():
    with open('input.txt', 'r') as file:
        input_data = file.read().strip().split('\n')
    for line in input_data:
        try:
            shape = parse_input(line)
            if shape is not None:
                print(f"{line.split()[0].capitalize()} Perimeter {shape.perimeter():.2f} Area {shape.area():.2f}")
            else:
                print(f"Error processing line: {line}\nShape is None")
        except Exception as e:
            print(f"Error processing line: {line}\n{e}")


if __name__ == "__main__":
    main()
