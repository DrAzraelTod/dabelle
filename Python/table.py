import line

class Table(object):
  lines = []

  def __init__(self,read_func):
    i = 0
    for l in read_func():
      print(l)
      self.lines.append(line.Line(l, i))
      i += 1
    print(self.to_plaintext())

  def to_plaintext(self):
    ret = []
    widths = {}
    for l in self.lines:
      y = 0
      for c in l.cells:
        v = len(c.get_value())
        if len(widths) > y:
          if widths[y] < v:
            widths[y] = v
        else:
          widths[y] = v
        y += 1
    for l in self.lines:
      values = []
      y = 0
      for c in l.cells:
        values.append(" %s" % c.get_value().ljust(widths[y]))
        y += 1
      ret.append("| %s |" % "|".join(values))
    return ("\n".join(ret))+"\n"
