import re

class Cell(object):
  value = False
  fieldid = False
  x = 0
  y = 0

  def __init__(self,substr,x,y):
    self.x = x
    self.y = y
    while True:
      temp = self.search_property(substr)
      if len(temp) >= len(substr):
        break
      substr = temp
    self.value = substr
    print("cell %i %i - %s" % (self.x, self.y, self.value))

  def search_property(self,substr):
    props = "_!#&="
    print("search %s" % substr)
    r = re.compile(r"^([^a-zA-Z0-9])(.*)(\1)")
    res = r.split(substr)
    if len(res) > 3:
      # "_multiply with_!titles" becomes:
      # ['', '_', 'multiply with', '_', '!titles']
      if res[1] in props:
        self.found_property(res[1],res[2])
      return res[-1]
    else:
      if substr[0] in props:
        self.found_property(substr[0],substr[1:])
        return substr[1:]
      return substr

  def found_property(self,name,value):
    print("property %s found: %s" %(name, value))
    pass
