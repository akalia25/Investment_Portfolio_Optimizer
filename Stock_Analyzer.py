#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:08:14 2019

@author: adityakalia
"""
def Portfolio_Risk_Level() :
    while True :
        try : 
            risk_level =  input("Please enter the risk level from 1 (Low Risk) to 10 (High Risk) you would like to take on from your portfolio : ")
            if int(risk_level) > 0 and int(risk_level) <=10 :
                break
        except :
            pass
        print("Incorrect input please enter risk level between 1-10")
    
    return risk_level
        


print("Your risk level is " + Portfolio_Risk_Level())




