'''
Created on 22 Mar 2013

@author: malin
'''

import sys
sys.path.append('/usr/local/lib/python3.3/dist-packages')
from posanal.utils.helper import FrameworkHelper
from posanal.utils.table import TableManager
from posanal.utils.column import DecimalColumn as DEC
from posanal.utils.column import MoneyColumn as MON
from posanal.utils.column import TextColumn as TXT
from posanal.utils.column import FormulaColumn as FOR
from posanal.utils.column import DateColumn as DAT
from posanal.utils.spreadsheet import SpreadSheet 


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

    if (v == True):    
        from posanal.libreoffice.spreadsheet import LibreSpreadSheet 
        sheet = LibreSpreadSheet(XSCRIPTCONTEXT.getDocument())
    else:
        sheet = SpreadSheet("")
    fwh = FrameworkHelper()
    fwh.connect("malin","katten3","192.168.1.2","mydb")    
    r = writePositionsWitRealValues(3,2,fwh,sheet)
    
    return None





