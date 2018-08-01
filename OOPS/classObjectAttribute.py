class Circle():
  # this is a Class Object Attribute. it is true at any instance of class!
  pi=3.14
  
  def __init__(self, radius=1):   # default parameter for radius
    self.radius=radius
    self.area=radius*radius*Circle.pi    # can use Circle.pi also as pi is a globally defined Class Object Attribute
    
  # this is a method!
  def circumference(self):
    return self.radius*self.pi*2    # can use Circle.pi also as pi is a globally defined Class Object Attribute
  
  
