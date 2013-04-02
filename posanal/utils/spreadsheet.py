'''
Created on 22 Mar 2013

The purpose of the abstract class is to be able to test outside libreoffice

@author: malin
'''
from .log import debug

from abc import abstractmethod 
import sys

class SpreadSheet(object):
    def __init__(self,oDoc):
        self.oDoc = oDoc

    @abstractmethod
    def setValue(self,value):
        debug("setValue " + str(value))
        pass
        
    @abstractmethod
    def setString(self,value):
        debug("setString " + value)
        pass
      
    @abstractmethod
    def setFormula(self,value):
        debug("setFormula " + str(value))
        pass

    @abstractmethod
    def setCellBackColor(self,color):
        debug ("setCellBackColor " + str(color))
        pass
    
    @abstractmethod
    def setHoriJustify(self,j):
        debug ("HoriJustify " + j)
        pass
    
    @abstractmethod
    def setCharWeight(self, w):
        debug("setWeight " + w)
        pass
    
    @abstractmethod
    def setFormat(self, format):
        debug("setFormat " + str(format))
        pass
 
    @abstractmethod
    def getFormatKey(self,format):
        return 1
        pass

    @abstractmethod    
    def setCell(self,x,y):
        debug("setCell " + str(x) +" " + str(y))
        pass
    
def test():
    print("test")
