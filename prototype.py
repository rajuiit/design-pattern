import copy

class Shape:
    def __init__(self, color):
        self.color = color

    def clone(self):
        return copy.deepcopy(self)

    def draw(self):
        pass
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        print(f"Drawing a {self.color} circle with radius {self.radius}.")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    def draw(self):
        print(f"Drawing a {self.color} rectangle with width {self.width} and height {self.height}.")
class ShapeRegistry:
    def __init__(self):
        self.shapes = {}

    def register_shape(self, name, shape):
        self.shapes[name] = shape

    def get_shape(self, name):
        return self.shapes[name].clone()
if __name__ == "__main__":
    # Create a shape registry
    registry = ShapeRegistry()

    # Register prototypes
    registry.register_shape("small_circle", Circle("red", 5))
    registry.register_shape("large_rectangle", Rectangle("blue", 20, 15))

    # Clone and use shapes
    shape1 = registry.get_shape("small_circle")
    shape1.draw()

    shape2 = registry.get_shape("large_rectangle")
    shape2.draw()

    # Modify a cloned shape
    shape3 = registry.get_shape("small_circle")
    shape3.color = "green"
    shape3.draw()
