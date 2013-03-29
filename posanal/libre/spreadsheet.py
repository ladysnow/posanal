import sys
sys.path.append('/usr/local/lib/python3.3/dist-packages')

from  ..utils.spreadsheet import SpreadSheet 

import uno
import unohelper
from com.sun.star.script.provider import XScriptProviderFactory
from com.sun.star.script.provider import XScriptProvider
from com.sun.star.script.provider import XScriptContext 
from com.sun.star.lang import Locale as sLocale

class LibreSpreadSheet(SpreadSheet):
    def __init__(self,oDoc):
        self.oDoc = oDoc
        self.libreSheet = self.oDoc.CurrentController.getActiveSheet()
        self.cell = 0

    def setCell(self,x,y):
        self.cell = self.libresheet.getCellByPosition(x,y)

    def setFloat(self,value):
        self.cell.setValue(float(value))

    def setInt(self,value):
        self.cell.setValue(int(value))                             

    def setValue(self,value):
        self.cell.setValue(value)

    def setString(self,value):
        self.setString(value)
        
    def setFormula(self,value):
        self.cell.setFormula(value)

    def setCellBackColor(self,color):
        self.cell.CellBackColor = color 

    def setHoriJustify(self,j):
        self.cell.HoriJustify = uno.getConstantByName("com.sun.star.awt.TextAlign." + j)

    def setFontWeight(self, w):
        self.cell.CharWeight = uno.getConstantByName("com.sun.star.awt.FontWeight." + w )

    def setFormat(self,format):
        self.cell.NumberFormat = self.getFormatKey(format)

    def getFormatKey(self,format):
        NumForms = self.oDoc.getNumberFormats()
        key = NumForms.queryKey(format, sLocale() , True)
        if (key == -1):
            return self.oDoc.NumberFormats.addNew(format,sLocale())
        return key    


