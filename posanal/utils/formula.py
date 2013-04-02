'''
Created on 22 Mar 2013

@author: malin
'''
import re

ADJ = 1  # The coordinate system is based on (0,0) as a base, but on the spreadsheet the base is (A,1), thus y = +1

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
        return ("{%s,%s}:{%s,%s}" % (X,Y+ADJ,primX,primY))


def getChar(v):
    res=""
    delta = ord('Z') - ord('A') 
    lent = int (v / ( delta ))
    for i in range(0,lent):
        res = res + "A"
    res = res + chr( ord('A') + v - lent * delta)
    return str(res)

def getAddressOf(x,y):
    return str(getChar(x) + str(y))

def spreadSheetFormula(coords,formula):
    f=formula.replace(" ","")
    addrs = re.findall("\{[0-9]+\,[0-9]+\}|\{@\,[0-9]+\}|\{[0-9]+\,@\}",f)
    fnames = []
    for a in addrs:
        sa = a.replace("{","").replace("}","").split(",")
        x = int(sa[0].replace("@",str(coords.X))) + int(coords.tableX + coords.primX)
        y = int(sa[1].replace("@",str(coords.Y+ADJ))) + int(coords.tableY + coords.primY)
        fnames.append(str(getChar(x)) + str(y))
    i=0
    for fn in fnames:
        f = f.replace(addrs[i],fn)
        i=i+1       
    return f

def test():    

    expected = "C11/Z0*45-3*(C3-X0)"
    formula = " { @,11 }/{ 25,@ }* 45 -3*({@,3}-{0,0})"
    resultat = spreadSheetFormula(Coordinates(0,0,0,0),formula)
    print(resultat)

test()


version = '0.1'

