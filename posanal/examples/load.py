'''
Created on 22 Mar 2013

@author: malin
'''

import sys
#sys.path.append("/usr/lib/python3/dist-packages")
sys.path.append("/home/malin/work/posanal")

from posanal.utils.helper import FrameworkHelper
from posanal.utils.table import TableManager
from posanal.utils.column import DecimalColumn as DEC
from posanal.utils.column import MoneyColumn as MON
from posanal.utils.column import TextColumn as TXT
from posanal.utils.column import FormulaColumn as FOR
from posanal.utils.column import DateColumn as DAT
from posanal.utils.spreadsheet import SpreadSheet 
from posanal.utils.log import info, warning, error, log, debug

#from com.sun.star.script.provider import XScriptProviderFactory
#rom com.sun.star.script.provider import XScriptProvider
#from com.sun.star.script.provider import XScriptContext 


def writePositionsWitRealValues(x,y,fwh,sheet):

    query = """SELECT p.depoinsurance, p.symbol, f.name, p.startDate, f.valueDate, p.startValue, f.value, p.position, f.std \
               FROM funds AS f, positions AS p \
               WHERE p.symbol = f.symbol AND f.valueDate = (SELECT MAX(ff.valueDate) FROM funds AS ff  where ff.symbol = p.symbol)"""    
   
    colDefs = ( TXT("Symbol",     "symbol",      ""),\
                DEC("Andel",      "position",    ""),\
                DAT("Startdag",   "startDate",   ""),\
                DAT("Kursdag",    "valueDate",   ""),\
                DEC("Startkurs",  "startValue",  ""),\
                DEC("Dagskurs",   "value",       ""),\
                FOR("Startvärde", "{1,@}*{4,@}", ""),\
                FOR("Dagsvärde",  "{1,@}*{5,@}", ""),\
                FOR("Förändring", "{7,@}-{6,@}", "")\
              )            

    sums = [("Dagsvärde"),("Startvärde"),("Förändring")]                                                

    tm = TableManager(x,y,sheet)
    info("initialize")
    tm.initialize(colDefs)
    info("writeHeading")    
    tm.writeHeading()
    info("exccuteData")
    fwh.executeData(query,tm)
    info("writeSums")
    tm.writeSums(sums)

    return tm.rowCount() 

def writePositions(x):    
    
    info.active = True
    warning.active = True
    log.file = True
    log.file = "/home/malin/log/posanal"
    
    sheet=0
    
    if (1):
        info("import")   
        from posanal.libre.spreadsheet import LibreSpreadSheet
        info("XSCRIPT")   
        sheet = LibreSpreadSheet(XSCRIPTCONTEXT.getDocument())
        info("done")   
    else:
        sheet = SpreadSheet("")
        
    fwh = FrameworkHelper()
    info("Connect")
    fwh.connect("malin","katten3","192.168.1.2","mydb")
    info("fill positions")    
    r = writePositionsWitRealValues(1,1,fwh,sheet)
    
    info("done")
    
    return None


writePositions(False)




