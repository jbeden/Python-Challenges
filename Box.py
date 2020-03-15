# What's in the Box?
# Write a class that simulates a 2-dimensional box. You must be able to specify the dimensions, and it must have a method for 
# determining whether a given point lies inside or outside of the box.
# Bonus challenges:
# - Make it work for a 3-dimensional box
# - Make it work for an n-dimensional hyperrectangle

class Box:
  def __init__(self, dimensions, origin=None):
    self.dimensions = []
    self.origin = []
    self.set_dimensions(dimensions, origin)
  
  def set_dimensions(self, dimensions, origin=None):
    if len(dimensions) > 0 and all(i > 0 for i in dimensions):
      self.dimensions = dimensions
      self.set_origin(origin)

  def set_origin(self, origin):
    if origin != None:
      if len(origin) == len(self.dimensions):
        self.origin = origin
      else:
        self.origin = [0] * len(self.dimensions)
    else:
      if len(self.origin) != len(self.dimensions):
        self.origin = [0] * len(self.dimensions)

  def lies_inside(self, point):
    if len(point) == len(self.dimensions):
      inside = True
      for idx in range(len(point)):
        if point[idx] > (self.dimensions[idx] + self.origin[idx]) or point[idx] < self.origin[idx]:
          inside = False

      return inside
    else:
      print("Not a valid point in {0}-dimensional space".format(len(self.dimensions)))

      return False
