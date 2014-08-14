import cell

class Line(object):
  cells = []
  x = 0

  def __init__(self,filepart,x):
    self.x = x
    y = 0
    for l in filepart.split("|"):
      self.cells.append(cell.Cell(l,x,y))
      y += 1
