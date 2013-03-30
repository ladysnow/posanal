'''
Created on 22 Mar 2013

@author: malin
'''
import sys

from .formula import Coordinates

class TableManager:
    def __init__(self,x,y, sheet):
        self.x = x
        self.y = y
        self.colDefs = 0
        self.sheet = sheet

    def initialize(self,colDefs):
        self.colDefs = colDefs
        ci=0
        for colDef in self.colDefs:
            coords = Coordinates(self.x,self.y,ci,0)
            colDef.coords = coords
            ci=ci+1
        return True

    def rowCount(self):
        maxRows=0
        for cd in self.colDefs:
            nRows = cd.getTotalRows() 
            if (nRows > maxRows):
                maxRows = nRows
            return max
        
    def columnCount(self):
            return (len(self.colDefs))

    def writeHeading(self):
        for colDef in self.colDefs:
            colDef.writeHeading(self.sheet)
        return None

    def writeRow(self,row):    
        for colDef in self.colDefs:
            colDef.write(row,self.sheet)
        return None

    def writeSums(self,sums):
        i=0
        for label in sums:
            i += 1
            for cd in self.colDefs:
                if (cd.label == label):
                    cd.writeSum(self.sheet)
        return None

def test():
    print("test")

