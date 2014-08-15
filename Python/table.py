import line

class Table(object):
  lines = []

  def __init__(self,read_func):
    self.lines = []
    i = 0
    for l in read_func():
      if "\n" in l:
        for p in l.split("\n"):
          self.create_line(p)
      else:
        self.create_line(l)
    print(self.to_plaintext())

  def create_line(self,text):
    if len(text) <1:
      return
    i = len(self.lines)+1
    self.lines.append(line.Line(text, i))

  def to_plaintext(self):
    ret = "\n"
    widths = {}
    for l in self.lines:
      for c in l.cells:
        y = c.y
        v = len(c.get_value())
        if y in widths:
          if widths[y] < v:
            widths[y] = v
        else:
          widths[y] = v
    print(widths)
    for l in self.lines:
      print(len(l.cells))
      line = []
      for c in l.cells:
        line.append(c.get_value().ljust(widths[c.y]))
      ret += "\n| %s |" % (" | ".join(line))
    return ret
