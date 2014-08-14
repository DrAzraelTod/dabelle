class Cell(object):
  value = False
  fieldid = False
  x = 0
  y = 0

  def __init__(self,substr,x,y):
    self.x = x
    self.y = y
    self.value = substr
    print("cell %i %i - %s" % (self.x, self.y, self.value))
