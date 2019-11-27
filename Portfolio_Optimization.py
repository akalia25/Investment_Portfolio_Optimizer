#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:08:14 2019

@author: adityakalia
"""


import pprint
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd


def risk_Level():
    """
    Getting the user's risk level
    """
    while True:
        try:
            risk = input("Please enter the risk level from 1 (Low Risk) " +
                         "or 2 (Med Risk) or 3 (High Risk) " +
                         "you would like to take on from your portfolio : ")
            if int(risk) > 0 and int(risk) <= 3:
                break
        except ValueError:
            pass
        print("Incorrect input please enter risk level between 1-3")
    return risk


def user_Budget():
    """
    Getting the user's budget for the portfolio
    """
    while True:
        try:
            budget = input("Please enter how much you would like to invest " +
                           "in this portfolio : ")
            if int(budget) > 0:
                break
        except:
            pass
        print("Incorrect input please your budget")
    return budget


def Portfolio_Type(risk, budget):
    """
    Using the users's specified risk and budget to create an optimal portfolio
    """
    risk = int(risk)
    budget = int(budget)
    if risk == 1:
        print("\nThe user should invest more into fixed-income investments " +
              "and less equity holdings\n")
        print()
        stocksDict = {'EEMV': 0.10, 'ACWV': 0.10, 'XEF.TO': 0.075, 'VTI': 0.05,
                      'XIC.TO': 0.025, 'ZAG.TO': 0.35,
                      'ZFL.TO': 0.20, 'QTIP.NE': 0.10}
        stocks = [key for key in stocksDict]
        df = pd.DataFrame()
        for x in stocks:
            stock = yf.Ticker(x)
            tempdf = stock.history(period='1mo')
            tempdf.loc[:, 'StockName'] = x
            df = df.append(tempdf, sort='False')
            df.loc[:, 'ROI'] = df['Close'].pct_change()
        plotdf = df.loc[:, ['StockName', 'ROI']]
        plotdf = plotdf.fillna(0)
        plotdf = plotdf.drop(plotdf.index[0])
        plotdf = plotdf.pivot(index=plotdf.index, columns='StockName')
        plotdf.plot(ylim=(-1, 1))
        stocksDict = {key: value*budget for key, value in stocksDict.items()}
        print('The following stock allocation should be used ')
        pprint.pprint(stocksDict)
        labels = stocksDict.keys()
        vals = stocksDict.values()
        labels = list(labels)
        vals = list(vals)
        plt.pie(vals, labels=labels, autopct='%1.1f%%')
        plt.show()

    if risk == 2:
        print()
        print("The user should invest equually in fixed-income investments " +
              "and equity holdings \n")
        stocksDict = {'VTI': 0.15, 'EEMV': 0.15, 'XEF.TO': 0.15, 'ACWV': 0.10,
                      'XIC.TO': 0.075, 'VUS': 0.025,
                      'ZFL.TO': 0.175, 'QTIP.NE': 0.10, 'ZAG.TO': 0.075}
        stocksDict = {key: value*budget for key, value in stocksDict.items()}
        print('The following stock allocation should be used ')
        pprint.pprint(stocksDict)
        labels = stocksDict.keys()
        vals = stocksDict.values()
        labels = list(labels)
        vals = list(vals)
        plt.pie(vals, labels=labels, autopct='%1.1f%%')
        plt.show()

    if risk == 3:
        print()
        print("The user should invest more into equity holdings and " +
              "less fixed-income investments")
        print()
        stocksDict = {'VTI': 0.20, 'XEF.TO': 0.20, 'EEMV': 0.15, 'ACWV': 0.10,
                      'VUS': 0.05, 'ZFL.TO': 0.15,
                      'QTIP.NE': 0.05}
        stocksDict = {key: value*budget for key, value in stocksDict.items()}
        print('The following stock allocation should be used ')
        pprint.pprint(stocksDict)
        labels = stocksDict.keys()
        vals = stocksDict.values()
        labels = list(labels)
        vals = list(vals)
        plt.pie(vals, labels=labels, autopct='%1.1f%%')
        plt.show()


def main():
    risk = risk_Level()
    budget = user_Budget()
    Portfolio_Type(risk, budget)

if __name__ == '__main__':
    main()
