import re

class Cell(object):
  value = False
  x = 0
  y = 0
  hheading = ""
  vheading = ""
  manual_id = False
  merged = 0
  calculation = False

  def set_hheading(self,text):
    self.hheading = text
  def set_vheading(self,text):
    self.vheading = text
  def set_id(self,text):
    self.manual_id = text
  def set_merged(self,count):
    self.merged = int(count)
  def set_calculation(self,text):
    self.calculation = text

  def get_id(self):
    if self.manual_id != False:
      return self.manual_id
    return "Cell_%i_%i" % (self.x, self.y)

  def get_value(self):
    #TODO: check for calculation
    return self.value

  props = {
   "_": set_hheading,
   "!": set_vheading,
   "#": set_id,
   "&": set_merged,
   "=": set_calculation,
  }

  def __init__(self,substr,x,y):
    self.x = x
    self.y = y
    while True:
      temp = self.search_property(substr)
      if len(temp) >= len(substr):
        break
      substr = temp
    self.value = substr
    print("%s (%i;%i)  %s" % (self.get_id(), self.x, self.y, self.value))

  def search_property(self,substr):
    props = self.props.keys()
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
    self.props[name](self,value)
