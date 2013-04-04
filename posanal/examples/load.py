'''
Created on 22 Mar 2013

@author: malin
'''

import sys
#sys.path.append("/usr/lib/python3/dist-packages")
sys.path.append("/home/malin/work/posanal")

from posanal.utils.helper import FrameworkHelper, TableDef
from posanal.utils.column import DecimalColumn as DEC
from posanal.utils.column import MoneyColumn as MON
from posanal.utils.column import TextColumn as TXT
from posanal.utils.column import FormulaColumn as FOR
from posanal.utils.column import DateColumn as DAT
from posanal.utils.spreadsheet import SpreadSheet 
from posanal.utils.log import info, warning, error, log, debug


from com.sun.star.script.provider import XScriptContext 

class FundPositionsTable(TableDef):

        def query(self):
            
                return """SELECT p.depoinsurance, p.symbol, f.name, p.startDate, f.valueDate, p.startValue, f.value, p.position, f.std \
                      FROM funds AS f, positions AS p \
                      WHERE p.symbol = f.symbol AND f.valueDate = (SELECT MAX(ff.valueDate) FROM funds AS ff  where ff.symbol = p.symbol)"""    
   
        def columns(self):
            
                return ( TXT("Symbol",     "symbol",     ""),\
                        DEC("Andel",      "position",    ""),\
                        DAT("Startdag",   "startDate",   ""),\
                        DAT("Kursdag",    "valueDate",   ""),\
                        DEC("Startkurs",  "startValue",  ""),\
                        DEC("Dagskurs",   "value",       ""),\
                        FOR("Startvärde", "{1,@}*{4,@}", ""),\
                        FOR("Dagsvärde",  "{1,@}*{5,@}", ""),\
                        FOR("Förändring", "{7,@}-{6,@}", "")\
                     )            

        def sums(self):
            
            return [("Dagsvärde"),("Startvärde"),("Förändring")]                                                



class CashPositionsTable(TableDef):

        def query(self):
        
            return  """SELECT p.description, v.valueDate, v.value from positions AS p, valuation AS v where p.security = 'Likvid' \
                       AND p.id = v.positionId """
               
               
        def columns(self):
        
            return  ( TXT("Beskrivning",    "description",      ""),\
                      TXT("","",""), \
                      TXT("","",""), \
                      DAT("Värdedag",      "valueDate",    ""),\
                      TXT("","",""), \
                      TXT("","",""), \
                      TXT("","",""), \
                      MON("Värde",          "value",   "") \
                    )            

        def sums(self):
            
            return [("Värde")]                                                

class LifePositionsTable(TableDef):

        def query(self):
        
            return  """SELECT p.description, p.position, p.startDate, v.valueDate, p.coupon, p.frequency, v.value from positions AS p, valuation AS v where p.security = 'Liv' \
                       AND p.id = v.positionId """
               
               
        def columns(self):
        
            return  ( TXT("Beskrivning",    "description",      ""), \
                      DEC("Andel",          "position",         ""), \
                      DAT("Startdag",       "startDate",        ""), \
                      DAT("Kursdag",        "valueDate",        ""), \
                      MON("Värde",          "value",            ""), \
                      MON("Utbetalas",      "coupon",           ""), \
                      TXT("Frekvens",       "frequency",        "") \
  
                    )            

        def sums(self):
            
            return [("Värde")]      


def writePositions(n):    
    
    info.active = True
    debug.active = True
    warning.active = True
    log.stdout = True
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
    
    x=0
    y0=1
    y1 = FundPositionsTable().execute(fwh, sheet, x, y0)
    y2 = CashPositionsTable().execute(fwh, sheet, x, y1 + 3) + y1
    y3 = LifePositionsTable().execute(fwh, sheet, x, y2 + 5) + y2
    
    info("Rows: " + str(y3))
    
    return None


writePositions(False)




