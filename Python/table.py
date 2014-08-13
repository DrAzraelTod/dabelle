import line

class Table(object):
  lines = []

  def __init__(self,read_func):
    for l in read_func():
      print(l)
      self.lines += line.Line(l)
