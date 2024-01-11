# Python: object oriented programming
class Point :
    x = 0
    y = 0

def demo1() -> None:
    p1 = Point()
    p2 = Point()
    print(p1.x, p2.x, Point.x)
    Point.x = 10
    print(p1.x, p2.x, Point.x)
    p1.x = 20
    print(p1.x, p2.x, Point.x)
    Point.x = 30
    print(p1.x, p2.x, Point.x)
    del p1.x
    print(p1.x, p2.x, Point.x)


class Vector :
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:                  # representation - for developers, debug, etc.
        return f"<Vector>({self.x}, {self.y})"
    
    def __add__(self, other) :
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise ValueError("Vector can be added only to Vector")
    
    def __mul__(self, other) :
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise ValueError("Vector can be multiplied only to Vector")
    
    def magnitude(self) -> float:
        if isinstance(self, Vector):
            return (self.x*self.x + self.y*self.y)**0.5
    
    def translate(self, dx: float, dy: float) -> None:
        if isinstance(self, Vector):
            self.x += dx
            self.y += dy


def demo2() -> None:
    v1 = Vector()
    v2 = Vector(1)
    v3 = Vector(1, -1)
    v4 = Vector(y=-1)
    print(v1, v2, v3, v4)
    print(repr(v1), repr(v2), repr(v3), repr(v4))
    print("v1+v2", v1 + v2)
    print("Magnit: ", v3.magnitude())
    v4.translate(10, 10)
    print("Trans: ", v4)
    v5 = Vector(10, 5)
    print(v5)
    print("Multiply:", v5 * 10)
    print(v3)
    print("v3*v5", v3 * v5)

def main() -> None:
    demo2()

if __name__ == "__main__": main()
