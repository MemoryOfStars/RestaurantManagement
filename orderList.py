# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 22:14:17 2018

@author: gmx
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:21:59 2018

@author: gmx
"""

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


                               O  R  D  E  R     L  I  S  T



Discription:Compeled by 'List' button in the Dish Window.List All Dishes by loading the Database
ThreadID:      10        
########################################

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import dish,dishes,order,table
import tkinter as tk
import mysql.connector as mc
import threading

class listOfAllOrders(threading.Thread):
    
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        orderListWin = tk.Tk(className='ListOfAllOrders')
        orderListWin.geometry("600x600")
        orderListBox1 = tk.Listbox(orderListWin,height = 30)
        orderListBox2 = tk.Listbox(orderListWin,height = 30)
        orderListBox3 = tk.Listbox(orderListWin,height = 30)
        orderListBox4 = tk.Listbox(orderListWin,height = 30)
        orderListBox5 = tk.Listbox(orderListWin,height = 30)
        
        db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="restaurant")
        cursor = db.cursor()
        #currentDishes = dishes.dishes()
        #dishesList = currentDishes.ListAllDishes();
        #sql = "SELECT * FROM DISH"
        #cursor.execute(sql)
        #dishesList = cursor.fetchall()
        listOrders = []
               
        sql = "SELECT * FROM ORDERS"
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(results)
        for row in results:
            oneOrder = order(row[0],row[1],row[2],row[3],row[4])
            listOrders.append(oneOrder)
            
        index=0
        while index < len(listOrders):
            #显示每一条菜品在列表控件上
            #print(dishesList[index])
            tup = listOrders[index]
            orderListBox1.insert(tk.END,tup.GetTableID())
            orderListBox2.insert(tk.END,tup.GetName())
            orderListBox3.insert(tk.END,tup.GetQuantity())
            orderListBox4.insert(tk.END,tup.GetCRT())
            orderListBox5.insert(tk.END,tup.GetState())

            index = index + 1
        orderListBox1.place(x=50,y=50)
        orderListBox2.place(x=200,y=50)
        orderListBox3.place(x=350,y=50)
        orderListBox4.place(x=500,y=50)
        orderListBox5.place(x=650,y=50)

        orderListWin.mainloop()                 # 进入消息循环