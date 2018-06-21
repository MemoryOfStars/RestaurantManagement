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
Discription:Show orders from all tables.Load from Database
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
        5.SetQuantity(newQuantity)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class order:
    
    def __init__(self,tableID,newDish,quantity,crt=time.time(),state=1):
        self.createTime = crt
        self.tableID = tableID
        self.dish = newDish
        self.quantity = quantity
        self.state = state
        
    def GetTime(self):
        return time.time() - self.createTime

    def GetState(self):
        return self.state

    def GetDishInfo(self):
        return self.dish
        
    def GetQuantity(self):
        return self.quantity
        
    def SetQuantity(self,newQuantity):
        self.quantity = newQuantity
        
    def GetCRT(self):
        return self.createTime
        
    def GetName(self):
        return self.dish.GetName()
        
    
        