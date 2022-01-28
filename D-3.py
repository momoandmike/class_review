class Square:
    def __int__(self, side):
        self.side = side

    def area(self):
        return (self.side ** 2)

    def diagonal(self):
        return ((self.side ** 2) ** 0.5)


square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
