# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 20:13:54 2018

@author: gmx
"""

# -*- coding: utf-8 -*-

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



                         C R E A T E    O R D E R    W I N D O W


                         
Discription:Compeled by 'New Order' button in the Orders Window.Add New orders by writing to the Database
ThreadID:      4        
########################################

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import dish,dishes,order,table
import time
import tkinter as tk
import mysql.connector as mc
import threading




def clickOnApply(createOrderWin):

    TableID = createOrderWin.orderEntry_TableID.get()
    #clear the Entry Box after Clicking on the Button
    createOrderWin.orderEntry_TableID.delete(0,tk.END)
    DishName = createOrderWin.orderEntry_DishName.get()
    createOrderWin.orderEntry_DishName.delete(0,tk.END)
    Quantity = createOrderWin.orderEntry_Quantity.get()
    createOrderWin.orderEntry_Quantity.delete(0,tk.END)
    #Calculate the Time
    timeStamp = time.time()
    timeStruct = time.localtime(timeStamp)
    timeStr = time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)
    
    db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="restaurant")
    cursor = db.cursor()
    print(TableID)
    print(DishName)
    print(Quantity)
    print(timeStr)
    print(int(1))
    sql = "INSERT INTO ORDERS \
            (TableID,Name,Quantity,CreateTime,State) \
            ('%d','%s','%d','%s','%d')" % \
            (TableID,DishName,Quantity,timeStr,1)
    cursor.execute(sql)
    



class createOrderWindow(threading.Thread):
    
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        self.createOrderWin = tk.Tk(className='Create New Order')
        self.createOrderWin.geometry("600x600")
        self.orderLabel_TableID = tk.Label(self.createOrderWin,text='Table ID:',bg='green')
        self.orderLabel_TableID.place(x=20,y=30)
        self.orderEntry_TableID = tk.Entry(self.createOrderWin)
        self.orderEntry_TableID.place(x=20,y=60)
        self.orderLabel_DishName = tk.Label(self.createOrderWin,text='Dish Name:',bg='blue')
        self.orderLabel_DishName.place(x=40,y=30)
        self.orderEntry_DishName = tk.Entry(self.createOrderWin)
        self.orderEntry_DishName.place(x=40,y=60)
        self.orderLabel_Quantity = tk.Label(self.createOrderWin,text='Quantity:',bg='blue')
        self.orderLabel_Quantity.place(x=40,y=30)
        self.orderEntry_Quantity = tk.Entry(self.createOrderWin)
        self.orderEntry_Quantity.place(x=40,y=60)
        self.orderButton_Apply = tk.Listbox(self.createOrderWin,text='Apply',command=clickOnApply(self))
        self.orderButton_Apply.pack(anchor='s')
        
        
        self.createOrderWin.mainloop()                 # 进入消息循环
        
        
        