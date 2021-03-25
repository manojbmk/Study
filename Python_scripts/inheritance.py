class Polygon:
  
    def set_values(self,width,height):
        self.width = width
        self.height = height
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

class Rectangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height()

class Triangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width() / 2
    

rect = Rectangle()
rect.set_values(4,5)

tri = Triangle()
tri.set_values(4,5)

print(rect.area(),tri.area())