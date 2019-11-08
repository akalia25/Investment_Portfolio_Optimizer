#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:08:14 2019

@author: adityakalia
"""
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


def Portfolio_Type(risk) : 
    print(type(risk))




risk = risk_Level()
budget = user_Budget()
print("The risk is " + risk)

Portfolio_Type(risk_Level)


