# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:58:59 2018

@author: gmx
"""

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


                          M A I N    P R O C E D U R E



Discription:Main Window And other Windows
########################################

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import dish,dishes,order,table
import tkinter as tk
import mysql.connector as mc
import threading

class mainWindowThread (threading.Thread):
    
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
    def run(self):
        root = tk.Tk()                     # 创建窗口对象的背景色
        root.title("Restaurant Management")
        root.geometry("300x300")
                                    # 创建两个列表
        #li     = ['C','python','php','html','SQL','java']
        #movie  = ['CSS','jQuery','Bootstrap']
        #listb  = tk.Listbox(root)          #  创建两个列表组件
        #listb2 = tk.Listbox(root)
        #for item in li:                 # 第一个小部件插入数据
        #    listb.insert(0,item)
        #for item in movie:              # 第二个小部件插入数据
        #    listb2.insert(0,item)
        
        #listb.pack()                    # 将小部件放置到主窗口中
        #listb2.pack()
        app = tk.Frame(root)
        app.grid()
        
        
        buttonDishes = tk.Button(app,text = "Dishes")
        buttonDishes.place()
        buttonOrders = tk.Button(app,text = "Orders")
        
        buttonDishes.grid()
        buttonOrders.grid()
        
        
        root.mainloop()                 # 进入消息循环


class subWindowThread(threading.Thread):
    
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        root = tk.Tk(className='subWindow')     
        li     = ['C','python','php','html','SQL','java']
        movie  = ['CSS','jQuery','Bootstrap']
        listb  = tk.Listbox(root)          #  创建两个列表组件
        listb2 = tk.Listbox(root)
        for item in li:                 # 第一个小部件插入数据
            listb.insert(0,item)
        for item in movie:              # 第二个小部件插入数据
            listb2.insert(0,item)
        
        listb.pack()                    # 将小部件放置到主窗口中
        listb2.pack()
        root.mainloop()                 # 进入消息循环
    
    
mainWindow = mainWindowThread(1,"MainWindow")
subWindow = subWindowThread(2,"subWindow")

mainWindow.start()
subWindow.start()

mainWindow.join()
subWindow.join()
    

