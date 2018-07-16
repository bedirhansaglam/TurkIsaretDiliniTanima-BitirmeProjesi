# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:18:38 2017

@author: Bedirhan
"""

import mysql.connector
from mysql.connector import errorcode

def connect(username,password,host,databasename):
    config = {
    'user': username,
    'password': password,
    'host': host,
    'database': databasename,
    'raise_on_warnings': True }
    
    try:
        cnx=mysql.connector.connect(**config)
        print("Veritabanina basariyla baglanildi")
    except mysql.connector.Error as err:
        if err.errno==errorcode.ER_ACCESS_DENIED_ERROR:
            print("Kullanici adi veya parola hatali")
        elif err.errno ==errorcode.ER_BAD_DB_ERROR:
            print ("Database adi hatali veya yanlis yazilmis")
        else:
            print(err)
    
    return cnx
    
def text_seperate(tablerow):
    t_row=""
    for i,row in enumerate (tablerow):
        if i!=len(tablerow)-1:
            t_row+=str(row)+", "
        else:
            t_row+=str(row)
    return t_row

def addTable(cursor,tablename,tablerow,tabledata):
    crs=cursor
    t_row=text_seperate(tablerow)
    data=text_seperate(tabledata)
    query=("INSERT INTO "+str(tablename)+" ("+t_row+") VALUES ("+data+")")
    crs.execute(query)
#    crs.close()
   
def selectTable(cursor):
    crs=cursor
    query=("SELECT * FROM new_data")
    crs.execute(query)
    for i in crs:
        print(str(len(i)))
        break
    return crs
    




