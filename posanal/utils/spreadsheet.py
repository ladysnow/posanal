'''
Created on 22 Mar 2013

@author: malin
'''
import sys
sys.path.append('/usr/local/lib/python3.3/dist-packages')

class SpreadSheet:
    def __init__(self,oDoc):
        self.oDoc = oDoc

    def setValue(self,value):
        print ("setValue " + str(value))

    def setString(self,value):
        print ("setString " + value)
        
    def setFormula(self,value):
        print ("setFormula " + str(value))

    def setCellBackColor(self,color):
        print ("setCellBackColor " + str(color))

    def setHoriJustify(self,j):
        print ("HoriJustify " + j)

    def setCharWeight(self, w):
        print("setWeight " +w )

    def setFormat(self, format):
        print("setFormat " + str(format))

    def getFormatKey(self,format):
        return 1
    
    def setCell(self,x,y):
        print("setCell " + str(x) +" " + str(y))

def test():
    print("test")
