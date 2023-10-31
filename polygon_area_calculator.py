class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height
    
    def get_perimeter(self) -> int:
        return (self.width + self.height) * 2
    
    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            full_str = ""
            for i in range(self.height):
                full_str += self.width * "*" + "\n"
            return full_str
    
    def get_amount_inside(self, obj: object) -> int:
        horizontal =  self.width // obj.width
        vertical = self.height // obj.height
        return horizontal * vertical


class Square(Rectangle):
    def __init__(self, side: int) -> None:
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f"Square(side={self.width})"
    
    def set_side(self, side: int) -> None:
        self.width = side
        self.height = side
    
    def set_width(self, side: int) -> None:
        self.set_side(side)

    def set_height(self, side: int) -> None:
        self.set_side(side)
    

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))