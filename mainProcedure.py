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
import dishWindow
#import mainProcedure

def windowDishRun():
    window = dishWindow.dishWindowThread(2,"dishWindow")
    window.start()
    
    
#def windowOrdersRun():

'''
def windowRun(window):
    new = window(2,"dishWindow")
    new.start()
'''

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

        buttonDishes = tk.Button(root,anchor = 'c',width = 30,height = 4,text='Dishes',fg='blue',bg='red',command=windowDishRun).place(x = 50,y = 20)
        buttonOrders = tk.Button(root,anchor = 'c',width = 30,height = 4,text='Orders',fg='blue',bg='red').place(x = 50,y = 200)
        
     
        root.mainloop()                 # 进入消息循环



    
    
mainWindow = mainWindowThread(1,"MainWindow")
#Main Window Starts
mainWindow.start()

mainWindow.join()

    

