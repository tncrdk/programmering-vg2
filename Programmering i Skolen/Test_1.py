# Test Programmering i Skolen

# print((0.1 + 0.2)*3)

# print((1E-1 + 2E-1)*3)

# konstant = 4

# def f(x):
#     global konstant
#     konstant += 2
#     kvadrat = x**2
#     return kvadrat - konstant

# print(f(2))
# print(konstant)

class polygon:
    def __init__(self, edges):
        self.edges = edges
        if self.edges < 3:
            raise Exception("Too few edges to make a two-dimensional figure")
    
    def anglesum(self):
        anglesum = (self.edges-2)*180
        return anglesum
    
p1 = polygon(6)

class square(polygon):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.edges = 4
        super().anglesum()

    def area(self):
        area = self.height * self.width
        return area

sq = square(4, 2)

print(sq.anglesum())
print(sq.area())

class triangle(polygon):
    def __init__(self, height, width):
        super().anglesum
        self.width = width
        self.height = height
        self.edges = 3
    
    def area(self):
        return self.width * self.height * 0.5
    
tr = triangle(4,3)
print(tr.anglesum())
print(tr.area())



