var dabelle = function(source) {
  dabelle.table = [];
  dabelle.cells = {};
  dabelle.debug = true;
  dabelle.props = "_!&#=";

  dabelle.init = function(source) {
    if (source.search("\n") >= 0) {
      dabelle.parseData(source);
    } else {
      var s = document.getElementById(source)
      if (s) {
        dabelle.parseData(dabelle.getData(s));
      } else {
        if ($) {
          dabelle.parseData(dabelle.getData($(source)));
        } else {
          dabelle.error("no idea how to get input-data! you fail!")
          dabelle = null;
          return;
        }
      }
    }
    // Now we have data! \o/
  }

  dabelle.to_plaintext = function() {
    return dabelle.cells;
  }

  dabelle.error = function(output) {
    if (console && console.error) {
      console.error(output);
    } else {
      alert(output);
    }
  }
  
  dabelle.parseProp = function(ident, val) {
    if (dabelle.props.search(ident) >= 0) {
      return val;
    }
    return false;
  }

  dabelle.parseCell = function(text, x, y) {
    temp = text;
    props = {}
    r = /^([^a-zA-Z0-9])(.*)(\1)/;
    while (r.exec(temp)) {
      f = r.exec(temp);
      if (false !== dabelle.parseProp(f[1], f[2])) {
        props[f[1]] = f[2];
      }
      temp = temp.replace(r,""); // remove current property
    }
    if (false !== dabelle.parseProp(temp[0], temp.substr(1))) {
      props[temp[0]] = temp.substr(1);
      temp = temp.substr(1);
    }
    if (!dabelle.cells) {
      dabelle.cells = {}
    }
    if (!dabelle.cells[x]) {
      dabelle.cells[x] = {}
    }
    dabelle.cells[x][y] = [temp,props];
    return [temp, props];
  }
  dabelle.parseLine = function(text, x) {
    var cells = text.split("|");
    var y = -1;
//    cells.forEach(dabelle.parseCell)
    cells.forEach(function(c) {
      y++;
      return dabelle.parseCell(c,x,y);
    });
  }

  dabelle.parseData = function(data) {
    var lines = data.split("\n");
    lines.forEach(dabelle.parseLine);
  }
  dabelle.getData = function(element) {
    if (element.value == undefined) {
      return element.innerHTML;
    }
    return element.value;
  }
  dabelle.init(source);
  return dabelle;
}
