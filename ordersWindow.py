# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 19:59:00 2018

@author: gmx
"""

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


                          O  R  D  E  R  S       W  I  N  D  O  W



Discription:Main Window And other Windows
Thread ID:       3
########################################

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import dish,dishes,order,table,DishList,createOrderWindow
import tkinter as tk
import mysql.connector as mc
import threading

def clickOnCreateNewOrder():
    #Open a new Window
    newOrderWindow = createOrderWindow.createOrderWindow(3,"CreateNewOrder")
    newOrderWindow.start()
    
    
def clickOnListAllOrder():
    #Open a List of All Orders
    #Not Create Source Files Yet
    orderListWin = orderList.orderList(10,"ListofAllOrders")
    orderListWin.start()
    
    

class ordersWindowThread(threading.Thread):
    
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    

    def run(self):
        dishWindow = tk.Tk(className='dishWindow')   
        dishWindow.geometry("300x300")
        #还未加事件响应函数
        newOrderButton   = tk.Button(dishWindow,anchor='c',width = 30,height = 4,text='New Order',fg='blue',bg='red',command=clickOnCreateNewOrder).place(x = 50,y = 20)
        #还未加事件响应函数
        orderChangeButton = tk.Button(dishWindow,anchor='c',width = 30,height = 4,text='Order Change',fg='red',bg='blue').place(x = 50,y = 200)

        dishWindow.mainloop()                 # 进入消息循环