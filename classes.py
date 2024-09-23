class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield {'Length': self.length}
        yield {'Width': self.width}


rect = Rectangle(10, 20)

for dimension in rect:
    print(dimension)