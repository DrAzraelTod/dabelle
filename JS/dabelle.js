var dabelle = function(source) {
  dabelle.table = [];
  dabelle.cells = {};
  dabelle.debug = true;

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
        }
        dabelle.error("")

      }
    }
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
  dabelle.parseData = function(data) {

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
