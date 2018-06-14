# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:50:45 2018

@author: gmx
"""

import tkinter as tk
import mysql.connector as mc


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Class Name:dish
Discription:Dish Displayed on the Menu,in the Main Procedure,load dishes from MySQL
########################################
Element:
        1.Name(string)
        2.Price(integer)
        3.cate(string)
Functions:
        1.GetName():return Name
        2.GetPrice():return Price
        3.SetName(Name)
        4.SetPrice(Name)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class dish:
    
    def __init__(self,Name = '',Price = 0,Cate = 1):
        self.Name = Name
        self.Price = Price
        self.Cate = Cate
    
    def GetName(self):
        return self.Name
        
    def GetPrice(self):
        return self.Price
        
    def SetName(self,Name):
        self.Name = Name
        
    def SetPrice(self,Price):
        self.Price = Price
        