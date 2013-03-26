'''
Created on 22 Mar 2013

The purpose of the abstract class is to be able to test outside libreoffice

@author: malin
'''
from abc import abstractmethod 
import sys

sys.path.append('/usr/local/lib/python3.3/dist-packages')

class SpreadSheet(object):
    def __init__(self,oDoc):
        self.oDoc = oDoc

    @abstractmethod
    def setValue(self,value):
        print ("setValue " + str(value))
        pass
        
    @abstractmethod
    def setString(self,value):
        print ("setString " + value)
        pass
      
    @abstractmethod
    def setFormula(self,value):
        print ("setFormula " + str(value))
        pass

    @abstractmethod
    def setCellBackColor(self,color):
        print ("setCellBackColor " + str(color))
        pass
    
    @abstractmethod
    def setHoriJustify(self,j):
        print ("HoriJustify " + j)
        pass
    
    @abstractmethod
    def setCharWeight(self, w):
        print("setWeight " + w)
        pass
    
    @abstractmethod
    def setFormat(self, format):
        print("setFormat " + str(format))
        pass
 
    @abstractmethod
    def getFormatKey(self,format):
        return 1
        pass

    @abstractmethod    
    def setCell(self,x,y):
        print("setCell " + str(x) +" " + str(y))
        pass
    
def test():
    print("test")
