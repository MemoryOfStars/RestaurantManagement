# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 18:21:59 2018

@author: gmx
"""

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


                               D  I  S  H     L  I  S  T



Discription:Compeled by 'List' button in the Dish Window.List All Dishes by loading the Database
ThreadID:      4        
########################################

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import dish,dishes,order,table
import tkinter as tk
import mysql.connector as mc
import threading

class dishList(threading.Thread):
    
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        dishListWin = tk.Tk(className='DishList')
        dishListWin.geometry("300x600")
        dishListBox1 = tk.Listbox(dishListWin)
        dishListBox2 = tk.Listbox(dishListWin)
        dishListBox3 = tk.Listbox(dishListWin)
        
        db = mc.connect(host="localhost", user="root", password="zaq1XSW2cde3", database="restaurant")
        cursor = db.cursor()
        #currentDishes = dishes.dishes()
        #dishesList = currentDishes.ListAllDishes();
        sql = "SELECT * FROM DISH"
        cursor.execute(sql)
        dishesList = cursor.fetchall()
        print('dishesList')
        print(dishesList)

        #Get Category Information
        
        sql = "SELECT * FROM CATEGORY"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        dishCate = []
        for row in results:
            dishCate.append(row[1])
        db.close()
        
        index=0
        while index < len(dishesList):
            #显示每一条菜品在列表控件上
            print(dishesList[index])
            tup = dishesList[index]
            dishListBox1.insert(tk.END,tup[0])
            dishListBox2.insert(tk.END,tup[1])
            dishListBox3.insert(tk.END,dishCate[int(tup[2]) - 1])

            index = index + 1

        dishListBox1.place(x=50,y=50)
        dishListBox2.place(x=200,y=50)
        dishListBox3.place(x=350,y=50)

        dishListWin.mainloop()                 # 进入消息循环