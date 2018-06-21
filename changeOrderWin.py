# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:36:28 2018

@author: gmx
"""

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



                         C H A N G E    O R D E R    W I N D O W


                         
Discription:Compeled by 'New Order' button in the Orders Window.Add New orders by writing to the Database
ThreadID:      8        
########################################

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import dish,dishes,order,table
import time
import tkinter as tk
import mysql.connector as mc
import threading




def clickOnApply(changeOrderWin):

    TableID = changeOrderWin.orderEntry_TableID.get()
    #clear the Entry Box after Clicking on the Button
    changeOrderWin.orderEntry_TableID.delete(0,tk.END)
    DishName = changeOrderWin.orderEntry_DishName.get()
    changeOrderWin.orderEntry_DishName.delete(0,tk.END)
    Quantity = changeOrderWin.orderEntry_Quantity.get()
    changeOrderWin.orderEntry_Quantity.delete(0,tk.END)
    #Calculate the Time
    timeStamp = time.time()
    timeStruct = time.localtime(timeStamp)
    timeStr = time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)
    
    db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="restaurant")
    cursor = db.cursor()
    
    sql = "UPDATE ORDERS \
            SET QUANTITY = %d \
            WHERE (TABLEID,NAME) = (%d,%s)" % \
            (TableID,DishName)
    cursor.execute(sql)
    

def clickOnCancel(changeOrderWin):
    db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="restaurant")
    cursor = db.cursor()
    tarTableID = changeOrderWin.orderEntry_TableID.get()
    tarDishName = changeOrderWin.orderEntry_DishName.get()
    sql = "DELETE FROM ORDERS \
            WHERE (TABLEID,NAME) =  \
            ('%d','%s')" % \
            (tarTableID,tarDishName)
    cursor.execute(sql)
    


class changeOrderWindow(threading.Thread):
    
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        self.changeOrderWindow = tk.Tk(className='Create New Order')
        self.changeOrderWindow.geometry("600x600")
        self.orderLabel_TableID = tk.Label(self.changeOrderWindow,text='Table ID:',bg='green')
        self.orderLabel_TableID.place(x=20,y=30)
        self.orderEntry_TableID = tk.Entry(self.changeOrderWindow)
        self.orderEntry_TableID.place(x=20,y=60)
        self.orderLabel_DishName = tk.Label(self.changeOrderWindow,text='Dish Name:',bg='blue')
        self.orderLabel_DishName.place(x=40,y=30)
        self.orderEntry_DishName = tk.Entry(self.changeOrderWindow)
        self.orderEntry_DishName.place(x=40,y=60)
        self.orderLabel_Quantity = tk.Label(self.changeOrderWindow,text='Quantity:',bg='blue')
        self.orderLabel_Quantity.place(x=40,y=30)
        self.orderEntry_Quantity = tk.Entry(self.changeOrderWindow)
        self.orderEntry_Quantity.place(x=40,y=60)
        self.orderButton_Apply = tk.Listbox(self.changeOrderWindow,text='Change',command=clickOnApply(self))
        self.orderButton_Apply.pack(anchor='s')
        
        self.orderButton_Cancel = tk.Button(self.changeOrderWindow,text='Change',command=clickOnCancel(self))
        self.orderButton_Cancel.pack(anchor='s')
        
        
        self.createOrderWin.mainloop()                 # 进入消息循环
        
        
        