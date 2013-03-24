'''
Created on 22 Mar 2013

@author: malin
'''

import sys
sys.path.append('/usr/local/lib/python3.3/dist-packages')


from .utils.spreadsheet import SpreadSheet
from .utils.helper import FrameworkHelper
from .utils.table import TableManager
from .utils.column import DecimalColumn as DEC
from .utils.column import MoneyColumn as MON
from .utils.column import TextColumn as TXT
from .utils.column import FormulaColumn as FOR
from .utils.column import DateColumn as DAT

def writePositionsWitRealValues(x,y,fwh,sheet):

    query = """SELECT p.depoinsurance, p.symbol, f.name, p.startDate, f.valueDate, p.startValue, f.value, p.position, f.std \
               FROM funds AS f, positions AS p \
               WHERE p.symbol = f.symbol AND f.valueDate = (SELECT MAX(ff.valueDate) FROM funds AS ff  where ff.symbol = p.symbol)"""    
   
    colDefs = ( TXT("Symbol",     "symbol",      ""),\
                DEC("Andel",      "position",    ""),\
                DAT("Startdag",   "startDate",   ""),\
                DAT("Kursdag",    "valueDate",   ""),\
                MON("Startkurs",  "startValue",  ""),\
                MON("Dagskurs",   "value",       ""),\
                FOR("Startvärde", "{1,@}*{4,@}", ""),\
                FOR("Dagsvärde",  "{1,@}*{5,@}", ""),\
                FOR("Förändring", "{7,@}-{6,@}", "")\
              )            

    sums = [("Dagsvärde"),("Startvärde"),("Förändring")]                                                

    tm = TableManager(x,y,sheet)
    tm.initialize(colDefs)    
    tm.writeHeading()
    fwh.executeData(query,tm)
    tm.writeSums(sums)

    return tm.rowCount() 

def writePositions(v):    
    
    #oDoc = XSCRIPTCONTEXT.getDocument()

    sheet = SpreadSheet("")
    fwh = FrameworkHelper()
    fwh.connect("malin","katten3","192.168.1.2","mydb")    
    r = writePositionsWitRealValues(3,2,fwh,sheet)
    
    return None

writePositions(1)




