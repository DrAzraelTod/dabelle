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
      if temp == substr:
        break
      substr = temp
    self.value = substr
    print("cell %i %i - %s" % (self.x, self.y, self.value))

  def search_property(self,substr):
    r = re.compile(r"^([^a-zA-Z0-9])(.*)(\1)")
    res = r.split(substr)
    if len(res) > 3:
      # "_multiply with_!titles" becomes:
      # ['', '_', 'multiply with', '_', '!titles']
      self.found_property(res[1],res[2])
      return res[-1]
    else:
      return substr

  def found_property(self,name,value):
    print("property %s found: %s" %(name, value))
    pass
