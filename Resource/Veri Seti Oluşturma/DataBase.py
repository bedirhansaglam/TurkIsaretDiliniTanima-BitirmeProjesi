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

def addTable(cursor,tabledata):
    tablerow="pp_x_0","pp_y_0","pp_z_0","pitch_0","roll_0","yaw_0","arm_d_x_0","arm_d_y_0","arm_d_z_0","wr_p_x_0","wr_p_y_0","wr_p_z_0",\
    "elb_p_x_0","elb_p_y_0","elb_p_z_0","m_s_x_00","m_s_y_00","m_s_z_00","m_e_x_00","m_e_y_00","m_e_z_00","m_d_x_00","m_d_y_00","m_d_z_00", \
    "p_s_x_00","p_s_y_00","p_s_z_00","p_e_x_00","p_e_y_00","p_e_z_00","p_d_x_00","p_d_y_00","p_d_z_00","i_s_x_00",\
    "i_s_y_00","i_s_z_00","i_e_x_00","i_e_y_00","i_e_z_00","i_d_x_00","i_d_y_00","i_d_z_00","d_s_x_00","d_s_y_00",\
    "d_s_z_00","d_e_x_00","d_e_y_00","d_e_z_00","d_d_x_00","d_d_y_00","d_d_z_00","m_s_x_01","m_s_y_01","m_s_z_01",\
    "m_e_x_01","m_e_y_01","m_e_z_01","m_d_x_01","m_d_y_01","m_d_z_01","p_s_x_01","p_s_y_01","p_s_z_01","p_e_x_01",\
    "p_e_y_01","p_e_z_01","p_d_x_01","p_d_y_01","p_d_z_01","i_s_x_01","i_s_y_01","i_s_z_01","i_e_x_01","i_e_y_01",\
    "i_e_z_01","i_d_x_01","i_d_y_01","i_d_z_01","d_s_x_01","d_s_y_01","d_s_z_01","d_e_x_01","d_e_y_01","d_e_z_01",\
    "d_d_x_01","d_d_y_01","d_d_z_01","m_s_x_02","m_s_y_02","m_s_z_02","m_e_x_02","m_e_y_02","m_e_z_02","m_d_x_02",\
    "m_d_y_02","m_d_z_02","p_s_x_02","p_s_y_02","p_s_z_02","p_e_x_02","p_e_y_02","p_e_z_02","p_d_x_02","p_d_y_02",\
    "p_d_z_02","i_s_x_02","i_s_y_02","i_s_z_02","i_e_x_02","i_e_y_02","i_e_z_02","i_d_x_02","i_d_y_02","i_d_z_02",\
    "d_s_x_02","d_s_y_02","d_s_z_02","d_e_x_02","d_e_y_02","d_e_z_02","d_d_x_02","d_d_y_02","d_d_z_02","m_s_x_03",\
    "m_s_y_03","m_s_z_03","m_e_x_03","m_e_y_03","m_e_z_03","m_d_x_03","m_d_y_03","m_d_z_03","p_s_x_03","p_s_y_03",\
    "p_s_z_03","p_e_x_03","p_e_y_03","p_e_z_03","p_d_x_03","p_d_y_03","p_d_z_03","i_s_x_03","i_s_y_03","i_s_z_03",\
    "i_e_x_03","i_e_y_03","i_e_z_03","i_d_x_03","i_d_y_03","i_d_z_03","d_s_x_03","d_s_y_03","d_s_z_03","d_e_x_03",\
    "d_e_y_03","d_e_z_03","d_d_x_03","d_d_y_03","d_d_z_03","m_s_x_04","m_s_y_04","m_s_z_04","m_e_x_04","m_e_y_04",\
    "m_e_z_04","m_d_x_04","m_d_y_04","m_d_z_04","p_s_x_04","p_s_y_04","p_s_z_04","p_e_x_04","p_e_y_04","p_e_z_04",\
    "p_d_x_04","p_d_y_04","p_d_z_04","i_s_x_04","i_s_y_04","i_s_z_04","i_e_x_04","i_e_y_04","i_e_z_04","i_d_x_04",\
    "i_d_y_04","i_d_z_04","d_s_x_04","d_s_y_04","d_s_z_04","d_e_x_04","d_e_y_04","d_e_z_04","d_d_x_04","d_d_y_04",\
    "d_d_z_04","pp_x_1","pp_y_1","pp_z_1","pitch_1","roll_1","yaw_1","arm_d_x_1","arm_d_y_1","arm_d_z_1","wr_p_x_1","wr_p_y_1","wr_p_z_1",\
    "elb_p_x_1","elb_p_y_1","elb_p_z_1","m_s_x_10","m_s_y_10","m_s_z_10","m_e_x_10","m_e_y_10","m_e_z_10","m_d_x_10","m_d_y_10","m_d_z_10",\
    "p_s_x_10","p_s_y_10","p_s_z_10","p_e_x_10","p_e_y_10","p_e_z_10","p_d_x_10","p_d_y_10","p_d_z_10","i_s_x_10",\
    "i_s_y_10","i_s_z_10","i_e_x_10","i_e_y_10","i_e_z_10","i_d_x_10","i_d_y_10","i_d_z_10","d_s_x_10","d_s_y_10",\
    "d_s_z_10","d_e_x_10","d_e_y_10","d_e_z_10","d_d_x_10","d_d_y_10","d_d_z_10","m_s_x_11","m_s_y_11","m_s_z_11",\
    "m_e_x_11","m_e_y_11","m_e_z_11","m_d_x_11","m_d_y_11","m_d_z_11","p_s_x_11","p_s_y_11","p_s_z_11","p_e_x_11",\
    "p_e_y_11","p_e_z_11","p_d_x_11","p_d_y_11","p_d_z_11","i_s_x_11","i_s_y_11","i_s_z_11","i_e_x_11","i_e_y_11",\
    "i_e_z_11","i_d_x_11","i_d_y_11","i_d_z_11","d_s_x_11","d_s_y_11","d_s_z_11","d_e_x_11","d_e_y_11","d_e_z_11",\
    "d_d_x_11","d_d_y_11","d_d_z_11","m_s_x_12","m_s_y_12","m_s_z_12","m_e_x_12","m_e_y_12","m_e_z_12","m_d_x_12",\
    "m_d_y_12","m_d_z_12","p_s_x_12","p_s_y_12","p_s_z_12","p_e_x_12","p_e_y_12","p_e_z_12","p_d_x_12","p_d_y_12",\
    "p_d_z_12","i_s_x_12","i_s_y_12","i_s_z_12","i_e_x_12","i_e_y_12","i_e_z_12","i_d_x_12","i_d_y_12","i_d_z_12",\
    "d_s_x_12","d_s_y_12","d_s_z_12","d_e_x_12","d_e_y_12","d_e_z_12","d_d_x_12","d_d_y_12","d_d_z_12","m_s_x_13",\
    "m_s_y_13","m_s_z_13","m_e_x_13","m_e_y_13","m_e_z_13","m_d_x_13","m_d_y_13","m_d_z_13","p_s_x_13","p_s_y_13",\
    "p_s_z_13","p_e_x_13","p_e_y_13","p_e_z_13","p_d_x_13","p_d_y_13","p_d_z_13","i_s_x_13","i_s_y_13","i_s_z_13",\
    "i_e_x_13","i_e_y_13","i_e_z_13","i_d_x_13","i_d_y_13","i_d_z_13","d_s_x_13","d_s_y_13","d_s_z_13","d_e_x_13",\
    "d_e_y_13","d_e_z_13","d_d_x_13","d_d_y_13","d_d_z_13","m_s_x_14","m_s_y_14","m_s_z_14","m_e_x_14","m_e_y_14",\
    "m_e_z_14","m_d_x_14","m_d_y_14","m_d_z_14","p_s_x_14","p_s_y_14","p_s_z_14","p_e_x_14","p_e_y_14","p_e_z_14",\
    "p_d_x_14","p_d_y_14","p_d_z_14","i_s_x_14","i_s_y_14","i_s_z_14","i_e_x_14","i_e_y_14","i_e_z_14","i_d_x_14",\
    "i_d_y_14","i_d_z_14","d_s_x_14","d_s_y_14","d_s_z_14","d_e_x_14","d_e_y_14","d_e_z_14","d_d_x_14","d_d_y_14",\
    "d_d_z_14","etiket"
    tablename="leap_data_test"
    crs=cursor
    t_row=text_seperate(tablerow)
    data=text_seperate(tabledata)
    query=("INSERT INTO "+str(tablename)+" ("+t_row+") VALUES ("+data+")")
    crs.execute(query)
#    crs.close()
   
def selectTable(cursor,tablename):
    crs=cursor
    query=("SELECT * FROM "+str(tablename))
    data=crs.execute(query)
    return data

    
    




