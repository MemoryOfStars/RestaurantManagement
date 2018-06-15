# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 16:43:08 2018

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

class dishWindowThread(threading.Thread):
    
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        root = tk.Tk(className='dishWindow')     
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