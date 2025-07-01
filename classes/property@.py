class rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height 
    @property
    def height(self):
            return f"{self._height:.1f} cm"
    
    @property
    def width(self):
            return f"{self._width:.1f} cm"
    @width.setter
    def width(self, new_width):
          if new_width> 0:
                self._width = new_width
          else:
                print("Width has to be greater than 0")    
    
rectangle1 = rectangle(3,4)

print(rectangle1.width)
print(rectangle1.height)
