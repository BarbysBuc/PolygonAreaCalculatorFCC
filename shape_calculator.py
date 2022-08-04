class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self, width):
    self.width = width
    

  def set_height(self, height):
    self.height = height
    

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    picture = ''
    if self.width >= 50 or self.height >= 50:
      return 'Too big for picture.'
    else:
      for line in range(0, self.height):
        for col in range(0, self.width):
          picture += '*'
        picture += '\n'  
      return picture  

#  def get_amount_inside(self, another_shape):
#    aux = self.height
#    amount = 0
#    if self.height >= another_shape.height and self.width >= another_shape.width:
#      while aux >= another_shape.height:
#        amount += self.width // another_shape.width
#        aux = self.height - another_shape.height
#    return amount  
  def get_amount_inside(self,shape):
    fieldWidth = self.width
    fieldHeight = self.height
    shapeWidth = shape.width
    shapeHeight = shape.height
    countWidth = 0
    countHeight = 0
    if fieldHeight > shapeHeight:
      countHeight = fieldHeight // sectHeight
    if fieldWidth > shapeWidth:
      countWidth = fieldWidth // sectWidth
    return countWidth * countHeight

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side,side)
    self.side = side

  def __repr__(self):
    return f'Square(side={self.width})'

  def set_side(self, side):
    super().__init__(side,side)
    self.side = side

  def set_width(self,side):
    self.set_side(side) 
  
  def set_height(self,side):
    self.set_side(side) 

