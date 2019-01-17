import sys
import getpass
import os
import random
import cx_Oracle
import datetime
from addperson import *


def driverLicenceRegistration(curs, connection):
    sin = str(input("please input user sin > "))
    search_str = 'SELECT name FROM people p WHERE p.sin =\''
    search_str += sin
    search_str += "\'"
    print(search_str)
    curs.execute(search_str)    
    result = curs.fetchall()
    print(result)
    if (len(result) == 0):
        n_own = 'y'
        #n_own = input("new sin entered, add new person? (y) or (n) or (e) > ")
        if (n_own == 'e'):
            pass
        else:  
            n_own = input("user found, add vehicle? (y)es or (n)o or (e)xit > ")
            if (n_own == 'e'):
                pass            
    licence_no = input("input licence number > ")
    Dclass = input("input licence class > ")
    photo = input("input (photoname).jpg > ")
    issuing_date = input("input issuing date > ")
    expiring_date = input("input expiration date > ")
    
    
    f_image  = open(photo,'rb')
    photo  = f_image.read()
    ddata =(licence_no, sin, Dclass, photo, issuing_date, expiring_date)
    #prepare memory for operation parameters
    curs.bindarraysize = 1
    curs.setinputsizes(30, 30, 10 , cx_Oracle.BLOB, cx_0racle.Date, cx_0racle.Date)
    curs.setinputsizes(photo = cx_Oracle.BLOB)
    cursInsert.executemany("INSERT INTO drive_license( licence_no, sin, class, photo, issuing_date, expiring_date)" 
                                       "VALUES (:1, :2, :3, :4, :5, :6)",ddata)    
    
    insert = """insert into drive_license( licence_no, sin, class, photo, issuing_date, expiring_date)
    values (:license_no, :sin, :class, :image, :issuing_date, expiring_date)"""
    curs.execute(insert,{'licence_no':licence_no, 'sin':sin,
                           'Dclass':Class, 'photo':image, 'issuing_date':issuing_date, 'expiring_date':expiring_date})
