import sys

from  ..utils.spreadsheet import SpreadSheet 
from  ..utils.log import debug

import uno
import unohelper
from com.sun.star.script.provider import XScriptProviderFactory
from com.sun.star.script.provider import XScriptProvider
from com.sun.star.script.provider import XScriptContext 
from com.sun.star.lang import Locale as sLocale


class LibreSpreadSheet(SpreadSheet):
    def __init__(self,oDoc):
        self.oDoc = oDoc
        self.sheet = self.oDoc.CurrentController.getActiveSheet()
        self.cell = 0

    def setCell(self,x,y):
        debug("setCell x %s y %s" % (x,y))
        self.cell = self.sheet.getCellByPosition(x,y)

    def setFloat(self,value):
        self.cell.setValue(float(value))
 
    def setInt(self,value):
        self.cell.setValue(int(value))                             

    def setValue(self,value):
        debug("setValue %s" % (value))
        self.cell.setValue(value)

    def setString(self,value):
        debug("setString %s" % (value))
        self.cell.setString(value)
        
    def setFormula(self,value):
        debug("setFormula %s" % (value))
        self.cell.setFormula(value)

    def setCellBackColor(self,color):
        debug("setBackColor %s" % ( str(color)))
        self.cell.CellBackColor = color 

    def setHoriJustify(self,j):
        debug("setHoriJustify %s" % (j))
        self.cell.HoriJustify = uno.getConstantByName("com.sun.star.awt.TextAlign." + j)

    def setCharWeight(self, w):
        debug("setFontWeight %s" % (w))
        self.cell.CharWeight = uno.getConstantByName("com.sun.star.awt.FontWeight." + w )

    def setFormat(self,format):
        debug("setFormat %s" % (str(format)))
        self.cell.NumberFormat = self.getFormatKey(format)

    def getFormatKey(self,format):
        NumForms = self.oDoc.getNumberFormats()
        key = NumForms.queryKey(format, sLocale() , True)
        if (key == -1):
            debug("setting new format %s" %(str(format)))
            return self.oDoc.NumberFormats.addNew(format,sLocale())
        return key    


