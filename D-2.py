class Rectangle:
    def __int__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return (self.height * self.width)

    def diagonal(self):
        return (((self.height ** 2) + (self.width ** 2)) ** 0.5)


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
