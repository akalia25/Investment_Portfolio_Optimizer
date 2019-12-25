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


def PortfolioAnalysis(risk):
    risk = int(risk)
    if risk == 1:
        print('\n The graph shows how the portfolio would compare against ' +
              'the market with normalized prices'
              )
        stocksDict = {'XEF.TO': 0.25, 'XIC.TO': 0.25,
                      'ZAG.TO': 0.35, 'ZFL.TO': 0.15}
        stocks = [key for key in stocksDict]
        allocation = list(stocksDict.values())
        # Hypotheical amount of $10,000 to show performance of portfolio \
        # against performance of market
        investedAmount = 10000
        df = pd.DataFrame()
        # Retrieving historical data from stocks using yfinance
        for x in stocks:
            stock = yf.Ticker(x)
            tempdf = stock.history(period='1y')
            tempdf.loc[:, 'StockName'] = x
            df = df.append(tempdf, sort='False')
        stockDF = df.loc[:, ['StockName', 'Close']]
        stockDF = stockDF.pivot(index=stockDF.index, columns='StockName')
        norm = stockDF/stockDF.iloc[0]
        portfolioNorm = norm * allocation
        dollarPortfolioVal = portfolioNorm * investedAmount
        dailyReturn = dollarPortfolioVal.sum(axis=1)
        dailyNormReturn = dailyReturn / dailyReturn.iloc[0]
        marketVal = yf.Ticker('SPY')
        df1 = marketVal.history(period='1y')
        marketDF = df1.loc[:, ['Close']]
        marketDF = marketDF.rename(columns={'Close': 'SPY Market'})
        normPlotDF = marketDF/marketDF.iloc[0]
        normPlotDF['Normalized Portfolio'] = dailyNormReturn
        ax = normPlotDF.plot(legend=True, grid=True,
                             title='Portfolio Performance VS. Market(SPY)')
        ax.set_ylabel('Normalized Price')
        ax.set_xlabel('Date')
        plt.show()


def main():
    risk = risk_Level()
    budget = user_Budget()
    Portfolio_Type(risk, budget)
    PortfolioAnalysis(risk)

if __name__ == '__main__':
    main()
