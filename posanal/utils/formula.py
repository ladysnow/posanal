'''
Created on 22 Mar 2013

@author: malin
'''
import re
import os
import sys
import string

class Coordinates:
    def __init__(self,tx,ty,x,y):
        self.tableX = tx
        self.tableY = ty
        self.X = x
        self.Y = y
        self.primX = 0
        self.primY = 0
    def getRange(self):
        X = self.X + self.tableX 
        Y = self.Y + self.tableY 
        primX = X + self.primX 
        primY = Y + self.primY
        return ("{%s,%s}:{%s,%s}" % (X,Y,primX,primY))


def getChar(v):
    return str(chr(ord('A') + int(v)))

def getAddressOf(x,y):
    return str(getChar(x) + str(y))

def spreadSheetFormula(coords,formula):
    f=formula.replace(" ","")
    addrs = re.findall("\{[0-9]+\,[0-9]+\}|\{@\,[0-9]+\}|\{[0-9]+\,@\}",f)
    fnames = []
    for a in addrs:
        sa = a.replace("{","").replace("}","").split(",")
        x = int(sa[0].replace("@",str(coords.X))) + int(coords.tableX + coords.primX)
        y = int(sa[1].replace("@",str(coords.Y))) + int(coords.tableY + coords.primY)
        fnames.append(str(getChar(x)) + str(y))
    i=0
    for fn in fnames:
        f = f.replace(addrs[i],fn)
        i=i+1       
    return f


def test():    

    expected = "C11/Z0*45-3*(C3-X0)"
    formula = " { @,11 }/ { 25,@ }* 45 -3*({@,3}-{23,0})"
    resultat = spreadSheetFormula(Coordinates(0,0,0,0),formula)
    print(resultat)

version = '0.1'


test()