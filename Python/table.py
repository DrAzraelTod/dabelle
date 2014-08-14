import line

class Table(object):
  lines = []

  def __init__(self,read_func):
    i = 0
    for l in read_func():
      print(l)
      self.lines.append(line.Line(l, i))
      i += 1
