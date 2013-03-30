'''
Created on 22 Mar 2013

@author: malin
'''
import sys
sys.path.append("/usr/local/lib/python3.3/dist-packages")
import mysql.connector

class FrameworkHelper:
    def __init__(self):
        self.stuff =1
        self.conn =0

    def executeData(self,query,tm):
        cursor = self.conn.cursor()
        cursor.execute(query)
        rowNames = cursor._description
        for row in cursor.fetchall():
            i=0
            rowDict = {}
            for value in row:
                rowDict[rowNames[i][0]] = value              
                i+=1
            tm.writeRow(rowDict)

    def connect(self,n,p,h,db):
        try:   
            self.conn = mysql.connector.connect(user=n, password=p, host=h, database=db)
        except mysql.connector.Error as err:
            print("Exception " + str(err))
            sys.exit(0)

def test(self):
    print("test")
