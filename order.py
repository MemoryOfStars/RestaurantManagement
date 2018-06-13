# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 21:21:25 2018

@author: gmx
"""

import tkinter as tk
import mysql.connector as mc
import time
import dish


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Class Name:order
Discription:Dish Displayed on the Menu,in the Main Procedure,load dishes from MySQL
########################################
Element:
        1.createTime(int)
        2.tableID(int)
        3.dish(dish)
        4.quantity(int)
        5.state(int)
Functions:
        1.GetTime()//CurrentTime - CreateTime---return time(int)
        2.GetState()//return State(int)
        3.GetDishInfo()//return dish
        4.GetQuantity()//return Quantity
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class order:
    
    def __init__(self,tableID,newDish,quantity):
        self.createTime = time.time()
        self.tableID = tableID
        self.dish = newDish
        self.quantity = quantity
        self.state = 1
        
    def GetTime(self):
        return time.time() - self.createTime

    def GetState(self):
        return state

    def GetDishInfo(self):
        return dish
        
    def GetQuantity(self):
        return self.quantity
        