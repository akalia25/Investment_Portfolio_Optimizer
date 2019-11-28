# Investment_Portfolio_Optimizer
Stock Portfolio Analyzer

The purpose of this script is to provide users with an optimized portfolio based on their risk and budget to invest in ETF's. This advice should be taken at user's own caution.

The program works by requesting the users risk level from a scale of 1(low risk) to 3(high risk). After this input has been fufilled the program asks for the users budget (how much money they would like to invest). When these inputs are completed, the program outputs a tailored Portfolio consisting of ETFs and the dollar amount the user should invest in each ETF. The program visualizes the investments and percentage invested in an efficent pie chart (see below for sample).
![alt text](https://github.com/akalia25/Investment_Portfolio_Optimizer/blob/master/screenshots/Portfolio_breakdown.png)


To run this program simply download the .py file, and run it using terminal or any IDE.
The output should be like the screenshot below: 
![alt text](https://github.com/akalia25/Investment_Portfolio_Optimizer/blob/master/screenshots/Sample_Test.png)


This program also has the functionality to show how the Optimal Portfolio would perform against the market (SPY) over a dynamic 1 year time frame. 

![alt text](https://github.com/akalia25/Investment_Portfolio_Optimizer/blob/master/screenshots/PortfolioVisualization.png)

The program calculates the portfolios performance by first gathering the allocation percentage of each stock in the portfolio, and then multiplying that with that the normalized stock prices. After this calculation is done, the program takes the sum of across the row, and calculates the portfolios daily return. The portfolios daily return is then normalized and compared against the markets daily return for a one year timeframe, as shown above. 


