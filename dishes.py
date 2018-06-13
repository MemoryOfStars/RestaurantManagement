# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:57:02 2018

@author: gmx
"""

import tkinter as tk
import mysql.connector as mc
import dish

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Class Name:dishes
Discription:Dish Displayed on the Menu,in the Main Procedure,load dishes from MySQL
########################################
Element:
        1.dishList(list[dish])
Functions:
        1.ListAllDishes()
        2.AddNewDishes(string newName,int Price,int Kind)
        3.DeleteDishes(string Name)
        4.SetDishesName(string Name,string newName)
        5.SetDishesPrice(string,integer)
        6.GetDishesPrice(Name)
        7.ListAllDishesWithAscendingPrice()
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class dishes:
    
    def __init__(self):
        self.dishList = {}
        self.dish = dish() #A Proceeding element for Functions

    def ListAllDishes(self):
        #Initialize a new Window
        #Load and Display dishes from Database
        db = mc.connect("localhost", "root", "zaq1XSW2cde3", "restaurant", charset='utf8' )
        cursor = db.cursor()
        db.close()
        
    def AddNewDishes(self,newDish,newPrice,newKind):
        
        #Connect Database
        #Refresh Data in the Database
        db = mc.connect("localhost", "root", "zaq1XSW2cde3", "restaurant", charset='utf8' )
        cursor = db.cursor()
        db.close()
        
    def DeleteDishes(self,tarDishName):
        #Connect Database
        #Refresh Data in the Database
        db = mc.connect("localhost", "root", "zaq1XSW2cde3", "restaurant", charset='utf8' )
        cursor = db.cursor()
        db.close()
        
    def SetDishesName(self,Name,newName):
        #Connect Database
        #Refresh Data in the Database
        db = mc.connect("localhost", "root", "zaq1XSW2cde3", "restaurant", charset='utf8' )
        cursor = db.cursor()
        db.close()
        
    def GetDishesPrice(self,Name):
        #Connect Database
        db = mc.connect("localhost", "root", "zaq1XSW2cde3", "restaurant", charset='utf8' )
        cursor = db.cursor()
        db.close()
        #Price = returnValue
        return Price
    
    def ListAllDishesWithAscendingPrice(self):
        #Connect Database
        db = mc.connect("localhost", "root", "zaq1XSW2cde3", "restaurant", charset='utf8' )
        cursor = db.cursor()
        db.close()
        #Display dishes with Ascending Price in a window
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        