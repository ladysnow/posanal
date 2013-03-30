'''
Created on 22 Mar 2013

@author: malin
'''

from abc import ABCMeta, abstractmethod 
from .formula import spreadSheetFormula
from .formula import Coordinates

class TableManagerException(BaseException):
    def __init__(self,arg):
        self.arg = arg
        self.message = "TableMangerException " + arg

class Column(object):
    def __init__(self,label,key, fmt):
        self.coords = 0
        self.fmt = fmt
        self.key = key
        self.label = label
        self.nHeadings =0
        self.nFootings =0

    def initialize(self,sheet,coords):
        self.coords = coords
        self.sheet = sheet

    def getTotalRows(self):
        return self.nHeadings + self.coords.primY + self.nFootings

    @abstractmethod
    def writeCell(self,cell, coords, key):
        pass

    def getX(self):
            return self.coords.tableX + self.coords.X + self.coords.primX
    def getY(self):
            return self.coords.tableY + self.coords.Y + self.coords.primY
    def setCell(self,sheet):
            sheet.setCell(self.getX(),self.getY())
    def setCellAdjusted(self,sheet,x,y):
            sheet.setCell(self.getX()+x,self.getY()+y)

    def write(self,row, sheet):
        self.setCell(sheet)
        if (len(self.fmt) > 0):
            sheet.setFormat(self.fmt) 
       
        if (self.key in row): 
            self.writeCell(sheet, self.coords, row[self.key])
        else:
            self.writeCell(sheet, self.coords, self.key)
        self.coords.primY += 1
               
        return None

    def writeHeading(self,sheet):
        self.setCell(sheet)
        sheet.setCharWeight("BOLD")
        sheet.setHoriJustify("CENTER")
        sheet.setCellBackColor(13625333)
        sheet.setString(self.label)
        self.coords.Y += 1
        self.nHeadings += 1

    def writeSum(self,sheet):
        formula = "SUM(" + self.coords.getRange() + ")"
        self.setCellAdjusted(sheet,1,0)
        sheet.setCharWeight("BOLD")
        sheet.setFormula("=" + spreadSheetFormula(Coordinates(0,0,0,0), formula))
        self.nFootings +=1
  
class DecimalColumn(Column):
    def __init__(self,label,dbColName,fmt):
        super(DecimalColumn,self).__init__(label,dbColName,fmt)

    def writeCell(self,sheet, cords, value):        
        sheet.setValue(float(value))
        return True

class MoneyColumn(Column):
    def __init__(self,label,dbColName,fmt):
        if (len(fmt) == 0):
            fmt = "#,###,###"
        super(MoneyColumn,self).__init__(label,dbColName,fmt)

    def writeCell(self,sheet, cords, value):        
        sheet.setValue(float(value))
        return True

class DateColumn(Column):
    def __init__(self,label, dbColName, fmt):
        super(DateColumn,self).__init__(label,dbColName,fmt)

    def writeCell(self,sheet, cords, value):            
        sheet.setHoriJustify("RIGHT")
        sheet.setValue(int(value))
        return True

class TextColumn(Column):
    def __init__(self, label, dbColName, fmt):
        super(TextColumn,self).__init__(label,dbColName,fmt)

    def writeCell(self,sheet, cords, value):        
        sheet.setHoriJustify("LEFT")
        sheet.setString(value)
        return True

class FormulaColumn(Column):
    def __init__(self, label, formula, fmt):
        if (len(fmt) == 0):
            fmt = "#,###,###"
        super(FormulaColumn,self).__init__(label,formula,fmt)

    def writeCell(self,sheet, coords, formula):
        sheet.setHoriJustify("LEFT")
        sheet.setFormula("="+ spreadSheetFormula(coords, str(formula)))
        return None

def test():
    print("hej")
