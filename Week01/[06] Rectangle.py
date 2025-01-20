class Rectangle:
  def __init__(self, height, width):
    self.height = height
    self.width = width

  def calculate_area(self):
    return self.width * self.height

  def calculate_perimeter(self):
    return 2*self.width + 2*self.height

rectangle = Rectangle(float(input()), float(input()))

condition = input()
if condition == "area":
  result = rectangle.calculate_area()
else:
  result = rectangle.calculate_perimeter()
print(f"{result:.2f}")
