# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:29:57 2018

@author: gmx
"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


                          D  I  S  H     W  I  N  D  O  W



Discription:Main Window And other Windows
########################################

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import dish,dishes,order,table,DishList
import tkinter as tk
import mysql.connector as mc
import threading

def clickOnList():
    #Open a new Window
    dishListWindow = DishList.dishList(4,"Dish List")
    dishListWindow.start()

class dishWindowThread(threading.Thread):
    
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    

        
    
    def run(self):
        dishWindow = tk.Tk(className='dishWindow')   
        dishWindow.geometry("300x300")
        listButton   = tk.Button(dishWindow,anchor='c',width = 30,height = 4,text='List',fg='blue',bg='red',command=clickOnList).place(x = 50,y = 20)
        #还未加事件响应函数
        changeButton = tk.Button(dishWindow,anchor='c',width = 30,height = 4,text='Change',fg='red',bg='blue').place(x = 50,y = 200)

        dishWindow.mainloop()                 # 进入消息循环