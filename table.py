# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:07:46 2018

@author: gmx
"""

import tkinter as tk
import mysql.connector as mc
import dish
import order


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Class Name:table
Discription:
########################################
elements:
		1.ordersOfSelf(list[order])
         2.
functions:
		1.AddOrder(string dishName,int quantity)
		2.ChangeOrderState(string dishName,int operation,newQuantity) :return boolean//Costomer is willing to cancel an order or sth.
              OperationsI. ==1 -------> Cancel  
                        II.==2 -------> ChangeQuantity
  
  
		3.GetTotalConsumption():return Total Consumption by Adding Price
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

class table:
    def __init__(self,tableID):
        self.orderOfSelf = {}
        self.tableID = tableID
    def addOrder(self,dishName,quantity):
        #Connect Database
        #Refresh Data in the Database
        db = mc.connect("localhost", "root", "zaq1XSW2cde3", "restaurant", charset='utf8' )
        cursor = db.cursor()
        #Load Price and Category
        newDish = dish(dishName,Price,cate)
        #Get the New Ordered Dish
        newOrder = order(self.tableID,newDish,quantity)
        self.orderOfSelf.append(newOrder) 
        #Refresh Data in the Database
        db.close()
        
    def changeOrderState(self,dishName,operation,newQuantity):
        if operation == 1:
            #Cancel the Indicated Order
            #Connect Database and Refresh
            db = mc.connect("localhost", "root", "zaq1XSW2cde3", "restaurant", charset='utf8' )
            cursor = db.cursor()
            db.close()
        else:
            for temp in self.orderOfSelf:
                if order.GetDishInfo().GetName() == dishName:
                    tarOrder = temp
                    break
            tarOrder.SetQuantity(newQuantity)
            
    def GetTotalConsumption(self):
         #Connect Database and Refresh
        db = mc.connect("localhost", "root", "zaq1XSW2cde3", "restaurant", charset='utf8' )
        cursor = db.cursor()
        total = 0
        for temp in self.ordersOfSelf:
            total = total + temp.GetDishInfo().GetPrice()*temp.GetQuantity()
        
        db.close()
        return total
        
            
        
        