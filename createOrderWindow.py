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
import tkinter as tk
import mysql.connector as mc
import threading



def clickOnApply():
    ##How to Solve????????????????????????????????????????????????????
    TableID = orderEntry_TableID.get()
    #clear the Entry Box after Clicking on the Button
    orderEntry_TableID.delete(0,END)
    DishName = orderEntry_DishName.get()
    orderEntry_DishName.delete(0,END)
    Quantity = orderEntry_Quantity.get()
    orderEntry_Quantity.delete(0,END)
    db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="restaurant")
    cursor = db.cursor()
    sql = "INSERT INTO ORDERS \
            (TableID,Name,Quantity,CreateTime,State) \
            ('%d','%s','%d','%s','%d')" % \
            ('','','','','','')
    cursor.execute(sql)
    



class createOrderWindow(threading.Thread):
    
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        createOrderWin = tk.Tk(className='Create New Order')
        createOrderWin.geometry("600x600")
        orderLabel_TableID = tk.Label(createOrderWin,text='Table ID:',bg='green')
        orderLabel_TableID.place(x=20,y=30)
        orderEntry_TableID = tk.Entry(createOrderWin)
        orderEntry_TableID.place(x=20,y=60)
        orderLabel_DishName = tk.Listbox(createOrderWin,text='Dish Name:',bg='blue')
        orderLabel_DishName.place(x=40,y=30)
        orderEntry_DishName = tk.Entry(createOrderWin)
        orderEntry_DishName.place(x=40,y=60)
        orderLabel_Quantity = tk.Listbox(createOrderWin,text='Dish Name:',bg='blue')
        orderLabel_Quantity.place(x=40,y=30)
        orderEntry_Quantity = tk.Entry(createOrderWin)
        orderEntry_Quantity.place(x=40,y=60)
        dishButton_Apply = tk.Listbox(createOrderWin,text='Apply',command=clickOnApply)
        dishButton_Apply.pack(anchor='s')
        
        db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="restaurant")
        cursor = db.cursor()
        #currentDishes = dishes.dishes()
        #dishesList = currentDishes.ListAllDishes();
        #sql = "SELECT * FROM DISH"
        #cursor.execute(sql)
        #dishesList = cursor.fetchall()
        listDishes = dishes.dishes()
        dishesList = listDishes.ListAllDishes()
        #print('dishesList')
        i = 0
        while i < len(dishesList):
            print(dishesList[i].GetPrice(),dishesList[i].GetName(),dishesList[i].Cate)
            i = i + 1

        #Get Category Information
        
        sql = "SELECT * FROM CATEGORY"
        cursor.execute(sql)
        results = cursor.fetchall()
        #print(results)
        dishCate = []
        for row in results:
            dishCate.append(row[1])
        db.close()
        
        index=0
        while index < len(dishesList):
            #显示每一条菜品在列表控件上
            #print(dishesList[index])
            tup = dishesList[index]
            dishListBox1.insert(tk.END,tup.GetName())
            dishListBox2.insert(tk.END,tup.GetPrice())
            dishListBox3.insert(tk.END,dishCate[int(tup.Cate) - 1])

            index = index + 1
        dishListBox1.place(x=50,y=50)
        dishListBox2.place(x=200,y=50)
        dishListBox3.place(x=350,y=50)

        dishListWin.mainloop()                 # 进入消息循环