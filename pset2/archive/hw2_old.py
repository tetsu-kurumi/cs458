"""
You will use the Yahoo finance api: yahooquery, which is installed as a Python module on the zoo. 
See yquery.html for more information and a demonstration.

Your program will be similar to your blackjack program. 
When it gets a ticker, it will use yahooquery to get information about the stock and then use that 
information to index a table of results. Here are some sample indices:

beta beta: a measure of the stocks volatility relative to the market as a whole.
market cap whether the stock is a large cap (> $10 billion), mid cap (< $10 billion and > $2 billion) 
or small cap (> $250 million and < $2 billion)
growth vs value growth e.g., no or low dividend and volatile vs value e.g., dividend and stable.
ESG Companies are graded on ESG: environment, social, and corporate governance. 
That is, companies that fight climate change and promote diversity get high ESG scores. 
The question is: are they more profitable than the nasty old companies.
Earnings surprise Did their recent earnings report exceed expectations or disappoint?
sector In what sector does the company operate? e.g., energy, technology, materials.
yahooquery provides you these data (and a boatload more) for most US companies. 
For this assignment, that is your world. All companies should be US and report in US dollars.
You should gather data on dozens of companies and determine which of these indices can predict performance. 
To do so, you need to look at a stock's performance for the past 10 years or so. 
A stock is good if it outperformed the S and P 500 index during that period, and bad if it did worse than the S and P. 
The ticker for the S and P is "^GSPC".

Your analysis does not need to be one size fits all. You may evaluate companies differently 
depending on their size, sector, or ESG scores. For example, you could have one metric 
for technology companies and another for banks.

Explanation
Your procedure needs to provide an explanation that justifies your recommendation. Your process may be either quantitative or qualitative. You might use a machine learning classification based on the Merrill Lynch model portfolios or you might come up with your own set of rules. The explanation should be qualitative. I don't want to see R2's or p-values.
We will not evaluate the accuracy of your recommendation. We are more interested in the coherency of your explanation. Does it make sense? Is it a good story? Even the best Wall Street analyst is not going to be right all the time.
"""
import yahooquery as yq
import pandas as pd
import numpy as np

"""
which will take a stock ticker symbol as its argument and return one of three values: 
buy, sell, or hold. It will also provide an explanation for its recommendation. 
The optional client parameter can be one of: income, growth, or esg, 
in which case the procedure will evaluate the stock for inclusion in an 
income portfolio, growth portfolio, or environment, social, and governance portfolio.


Your explanation should be readily understandable to someone who does not have a background in finance.  
Also, your explanations for different decisions should be consistent with each other.  
That doesn't necessarily mean that you need to keep a record of the queries that the client has made so 
far that you consult every time you make a new decision, but your recommendation procedure shouldn't 
contradict itself in obvious ways.

demo
you should pick a collection of example inputs (however many it takes to show off all of the important 
functionality of your implementation; you'll probably need more than one stock if you want to show off 
buy, sell, and hold cases) and show the outputs that your implementation gives for them.

Yes, you should demonstrate all four client cases.
"""

SP_LIST = list(pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'])

class DefaultStrategy():
    None

class IncomeStrategy():
    None

class GrowthStrategy():
    def __init__(self):
        None
    
    def get_price 

class ESGStrategy():
    None

class Decisions():
    def __init__(self, stock):
        try:
            # Attempt to fetch data
            self.Ticker = yq.Ticker(stock)
        except ValueError as e:
            # Handle the error
            ValueError(f"Ticker does not exist. {e}")

        self.current_price = self.Ticker.financial_data[stock]['currentPrice']
        self.beta = self.Ticker.key_stats[stock]['beta']
        self. = self.Ticker.summary_detail[stock]

    def default(self) -> str:
        return decision

    def income(self) -> str:
        return decision

    def growth(self) -> str:
        return decision
    
    def esg(self) -> str:
        # Check score & trajectory and score (acceptable or not?)
        return decision
    
    def print_explanation(self, decision):
        None

def invest(ticker, client=False):
    # Initialize a simulation model sector by sector for growth using S&P stocks (predict them) and also set S&P predictions (set baseline to compare to)
    WarrenBuffet = Decisions(ticker)
    match client:
        case 'income':
            decision = WarrenBuffet.income()
        case 'growth':
            decision = WarrenBuffet.growth()
        case 'esg':
            decision = WarrenBuffet.esg()
        case False:
            decision = WarrenBuffet.default()
        case _:
            ValueError(f"Client type {client} is not supported")
    WarrenBuffet.print_explanation(decision)


def main():
    # Initialize the prediction models
    print("Initializing prediction model. This may take a few minutes.")


    ticker = input("Enter stock ticker: ")
    client = input("Enter client (return if default): ")
    if client == '':
        invest(ticker)
    else:
        invest(ticker, client)
    

if __name__ == "__main__":
    main()

"""
- Hold
not doing better than S&P but will potentially
- Sell
will not do better than S&P (value will go down)
- Buy
will do better than S&P (value will go up)

growth
- beta = confidence level (a measure of the stocks volatility relative to the market as a whole.)



growth vs value growth e.g., no or low dividend and volatile vs value e.g., dividend and stable.
ESG Companies are graded on ESG: environment, social, and corporate governance. That is, companies that fight climate change and promote diversity get high ESG scores. The question is: are they more profitable than the nasty old companies.
Earnings surprise Did their recent earnings report exceed expectations or disappoint?
Sector In what sector does the company operate? e.g., energy, technology, materials.

Growth objective:
produce long-term excess returns versus the benchmark over a full market cycle (at least 5 years) 
correct for inflation (or don't and use it if calculating the ratio to S&P)

growth features (quarter by quarter for training)
Earnings Per Share (EPS)
Price to Earnings Ratio (P/E ratio)
Price to Book Ratio (P/B ratio)
Dividend Yield
Revenue Growth Rate
Profit Margin
Debt-to-Equity Ratio
Book Value
Market Capitalization

return on equity (ROE)
return on invested capital (ROIC)
projected three-to-five year sales and EPS growth rates

past year data points of growth 

Industry-specific Variables
Supply and demand dynamics
Industry-specific regulations and policies
Competitive landscape
Technological innovations and disruptions

market indicators
Interest rates (e.g., Federal Reserve rates)
Inflation rates
GDP growth rates
Unemployment rates
Consumer sentiment indices
Volatility indices (e.g., VIX)
Bond yields

income (metric should be Dividend Yield)
- protection of principal (will the stock grow downwards?)
- income should not be on a downward trend (that it will cut under S&P)

Income objective:
to obtain an above average and ongoing secure income stream
from dependable sources, with some emphasis on protection of principal. Equity focus is
not just on the current dividend yield, but also on the potential for dividend growth as an
offset against inflation.


For this assignment, that is your world. All companies should be US and report in US dollars.


You should gather data on dozens of companies and determine which of these indices can predict performance. 
To do so, you need to look at a stock's performance for the past 10 years or so. 
A stock is good if it outperformed the S and P 500 index during that period, and bad if it did worse than the S and P. 
The ticker for the S and P is "^GSPC".
"""