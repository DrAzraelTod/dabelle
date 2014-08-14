#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, getopt, fileinput
import config
import table

debug = False
simple = True

class Dabelle(object):
    tables  = []

    def __init__(self, input):
      self.read_input(input)
      sys.exit(3)
    def read_input(self, input):
      fi = False
      if input==False:
         fi = fileinput.input
      else:
         fi = open(input,'r').xreadlines
      self.tables.append(table.Table(fi))

def usage():
    print("parameters:")
    print(" -h --help\t\t-> shows this help")
    print(" -d --debug\t\t-> enables debug-mode")
    print(" -s --simple\t\t-> no calculations (a-mode)")
    print(" -c --calculate\t\t-> enable calculation-parsing")
    print(" -f --file\t\t-> what file to parse? (else: stdin)")
    print(" -m --mode\t\t-> what config-mode to use")
    print("simple/calculate are opposites (combining makes no sense)")


if __name__ == '__main__':
    mode = 'default'
    source = False
    shortOptions = 'dcsf:m:h'
    longOptions = ['debug', 'calculate', 'simple', 'file=', 'mode=', 'help']
    try:
        opts, args = getopt.getopt(sys.argv[1:], shortOptions, longOptions)
    except getopt.GetoptError, err:
        print("[Parameter-Fehler]  %s" % err)
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("--debug", "-d"):
            print('[Status] Debugmodus aktiv')
            debug = True
        elif o in ("--help", "-h"):
            usage()
            sys.exit(0)
        elif o in ("--calculate", "-c"):
            simple = True;
        elif o in ("--file", "-f"):
            source=a
        elif o in ("--simple", "-s"):
            simple = false
        elif o in ("--mode", "-m"):
            mode = a
        else:
            print("[Fehler] Fehlerhafter Parameter")
            usage()
            sys.exit(2)
    Dabelle(source)
