#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:08:14 2019

@author: adityakalia
"""

"""
Getting the user's risk level
"""
import yfinance as yf
import matplotlib.pyplot as plt
import pprint
def risk_Level() :
    while True :
        try : 
            risk =  input("Please enter the risk level from 1 (Low Risk) or 2 (Med Risk) or 3 (High Risk) you would like to take on from your portfolio : ")
            if int(risk) > 0 and int(risk) <=3 :
                break
        except :
            pass
        print("Incorrect input please enter risk level between 1-3")
    
    return risk
        
"""
Getting the user's budget for the portfolio
"""
def user_Budget():
    while True :
        try : 
            budget =  input("Please enter how much you would like to invest in this portfolio : ")
            if int(budget) > 0 :
                break
        except :
            pass
        print("Incorrect input please your budget")
        
    return budget

"""
Using the users's specified risk and budget to create an optimal portfolio
"""

def Portfolio_Type(risk, budget) : 
    risk = int(risk)
    budget = int(budget)
    if risk == 1 :
        print()
        print("The user should invest more into fixed-income investments and less equity holdings")
        print()
        stocksDict = {'EEMV': 0.10, 'ACWV' : 0.10, 'XEF': 0.075 , 'VTI' : 0.05, 'XIC' : 0.025 , 'ZAG': 0.35 ,
                      'ZFL' : 0.20 , 'QTIP' : 0.10}
        stocksDict = {key:value*budget for key, value in stocksDict.items()}
        print('The following stock allocation should be used ')
        pprint.pprint(stocksDict)
        labels = stocksDict.keys()
        vals = stocksDict.values()
        labels = list(labels)
        vals = list(vals)
        plt.pie(vals, labels = labels, autopct='%1.1f%%')  
        plt.show()

    if risk == 2 :
        print()
        print("The user should invest equually in fixed-income investments and equity holdings")
        print()
        stocksDict = {'VTI': 0.15, 'EEMV' : 0.15, 'XEF': 0.15 , 'ACWV' : 0.10, 'XIC' : 0.075 , 'VUS': 0.025 ,
                      'ZFL' : 0.175 , 'QTIP' : 0.10 , 'ZAG' : 0.075}
        stocksDict = {key:value*budget for key, value in stocksDict.items()}
        print('The following stock allocation should be used ')
        pprint.pprint(stocksDict)
        labels = stocksDict.keys()
        vals = stocksDict.values()
        labels = list(labels)
        vals = list(vals)
        plt.pie(vals, labels = labels, autopct='%1.1f%%')  
        plt.show()
  
    if risk == 3 :
        print()
        print("The user should invest more into equity holdings and less fixed-income investments")
        print()
        stocksDict = {'VTI': 0.20, 'XEF' : 0.20, 'EEMV': 0.15 , 'ACWV' : 0.10, 'VUS' : 0.05 , 'ZFL': 0.15 ,
                      'QTIP' : 0.05}
        stocksDict = {key:value*budget for key, value in stocksDict.items()}
        print('The following stock allocation should be used ')
        pprint.pprint(stocksDict)
        labels = stocksDict.keys()
        vals = stocksDict.values()
        labels = list(labels)
        vals = list(vals)
        plt.pie(vals, labels = labels, autopct='%1.1f%%')  
        plt.show()
      
    

def main():
    risk = risk_Level()
    budget = user_Budget()
    Portfolio_Type(risk, budget)

    
    
if __name__ == '__main__':
    main()



