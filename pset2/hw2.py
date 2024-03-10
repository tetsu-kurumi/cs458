# %% [markdown]
# ## Installing Dependencies
# - yahooquery
# - pandas
# - numpy
# - scikit-learn

# %%
from yahooquery import Ticker
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math
import sys
import warnings

# Suppress FutureWarnings
warnings.filterwarnings("ignore", category=FutureWarning)

# %% [markdown]
# ## Setting Global Variables

# %%
# GLOBAL VARIABLES

SP_LIST = ['MMM', 'AOS', 'ABT', 'ABBV', 'ACN', 'ADBE', 'AMD', 'AES', 'AFL', 'A', 'APD', 'ABNB', 'AKAM', 'ALB', 'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP', 'AIG', 'AMT', 'AWK', 'AMP', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'AON', 'APA', 'AAPL', 'AMAT', 'APTV', 'ACGL', 'ADM', 'ANET', 'AJG', 'AIZ', 'T', 'ATO', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'AXON', 'BKR', 'BALL', 'BAC', 'BK', 'BBWI', 'BAX', 'BDX', 'BRK-B', 'BBY', 'BIO', 'TECH', 'BIIB', 'BLK', 'BX', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR', 'BRO', 'BF-B', 'BLDR', 'BG', 'CDNS', 'CZR', 'CPT', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CTLT', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE', 'COR', 'CNC', 'CNP', 'CF', 'CHRW', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG', 'CLX', 'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'COP', 'ED', 'STZ', 'CEG', 'COO', 'CPRT', 'GLW', 'CTVA', 'CSGP', 'COST', 'CTRA', 'CCI', 'CSX', 'CMI', 'CVS', 'DHR', 'DRI', 'DVA', 'DAY', 'DE', 'DAL', 'XRAY', 'DVN', 'DXCM', 'FANG', 'DLR', 'DFS', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DHI', 'DTE', 'DUK', 'DD', 'EMN', 'ETN', 'EBAY', 'ECL', 'EIX', 'EW', 'EA', 'ELV', 'LLY', 'EMR', 'ENPH', 'ETR', 'EOG', 'EPAM', 'EQT', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ETSY', 'EG', 'EVRG', 'ES', 'EXC', 'EXPE', 'EXPD', 'EXR', 'XOM', 'FFIV', 'FDS', 'FICO', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FSLR', 'FE', 'FI', 'FLT', 'FMC', 'F', 'FTNT', 'FTV', 'FOXA', 'FOX', 'BEN', 'FCX', 'GRMN', 'IT', 'GEHC', 'GEN', 'GNRC', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GILD', 'GPN', 'GL', 'GS', 'HAL', 'HIG', 'HAS', 'HCA', 'DOC', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT', 'HOLX', 'HD', 'HON', 'HRL', 'HST', 'HWM', 'HPQ', 'HUBB', 'HUM', 'HBAN', 'HII', 'IBM', 'IEX', 'IDXX', 'ITW', 'ILMN', 'INCY', 'IR', 'PODD', 'INTC', 'ICE', 'IFF', 'IP', 'IPG', 'INTU', 'ISRG', 'IVZ', 'INVH', 'IQV', 'IRM', 'JBHT', 'JBL', 'JKHY', 'J', 'JNJ', 'JCI', 'JPM', 'JNPR', 'K', 'KVUE', 'KDP', 'KEY', 'KEYS', 'KMB', 'KIM', 'KMI', 'KLAC', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LDOS', 'LEN', 'LIN', 'LYV', 'LKQ', 'LMT', 'L', 'LOW', 'LULU', 'LYB', 'MTB', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MTCH', 'MKC', 'MCD', 'MCK', 'MDT', 'MRK', 'META', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MRNA', 'MHK', 'MOH', 'TAP', 'MDLZ', 'MPWR', 'MNST', 'MCO', 'MS', 'MOS', 'MSI', 'MSCI', 'NDAQ', 'NTAP', 'NFLX', 'NEM', 'NWSA', 'NWS', 'NEE', 'NKE', 'NI', 'NDSN', 'NSC', 'NTRS', 'NOC', 'NCLH', 'NRG', 'NUE', 'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 'OMC', 'ON', 'OKE', 'ORCL', 'OTIS', 'PCAR', 'PKG', 'PANW', 'PARA', 'PH', 'PAYX', 'PAYC', 'PYPL', 'PNR', 'PEP', 'PFE', 'PCG', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'POOL', 'PPG', 'PPL', 'PFG', 'PG', 'PGR', 'PLD', 'PRU', 'PEG', 'PTC', 'PSA', 'PHM', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', 'RTX', 'O', 'REG', 'REGN', 'RF', 'RSG', 'RMD', 'RVTY', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SRE', 'NOW', 'SHW', 'SPG', 'SWKS', 'SJM', 'SNA', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STLD', 'STE', 'SYK', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW', 'TTWO', 'TPR', 'TRGP', 'TGT', 'TEL', 'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TXT', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRV', 'TRMB', 'TFC', 'TYL', 'TSN', 'USB', 'UBER', 'UDR', 'ULTA', 'UNP', 'UAL', 'UPS', 'URI', 'UNH', 'UHS', 'VLO', 'VTR', 'VLTO', 'VRSN', 'VRSK', 'VZ', 'VRTX', 'VFC', 'VTRS', 'VICI', 'V', 'VMC', 'WRB', 'WAB', 'WBA', 'WMT', 'DIS', 'WBD', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST', 'WDC', 'WRK', 'WY', 'WHR', 'WMB', 'WTW', 'GWW', 'WYNN', 'XEL', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS']

# Ref: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/wacc.htm and https://www.linkedin.com/pulse/sp-500-sectors-roic-vs-wacc-through-1q21-david-trainer/
WACC_RATES = {
    'Technology': 0.092,
    'Healthcare': 0.1028,
    'Financial Services': 0.1,
    'Consumer Cyclical': 0.0786,
    'Consumer Defensive': 0.07,
    'Industrials': 0.0791,
    'Energy': 0.0867,
    'Utilities': 0.068,
    'Basic Materials': 0.08,
    'Real Estate': 0.0986,
    'Communication Services': 0.073,
}

SECTORS = list(WACC_RATES.keys())

MARKETCAPS = ['largecap', 'midcap', 'smallcap']

# (See Appendix A for source code to obtain data)
AVGPERATIOS = {'Technology': 49.23658881690141,
 'Healthcare': 56.14869727118644,
 'Financial Services': 19.586146538461545,
 'Consumer Cyclical': 24.644157226415093,
 'Consumer Defensive': 31.269938114285708,
 'Industrials': 30.180891085714283,
 'Energy': 13.010462826086957,
 'Utilities': 19.340905928571427,
 'Basic Materials': 26.606018799999998,
 'Real Estate': 50.20442143333334,
 'Communication Services': 30.231775736842103}

# Assumed average growth rate for entire market
GROWTH_RATE = 0.04

# Default variables if the user inputs stocks in sectors that were not expected
DEFAULT_WACC_RATE = 0.084
DEFAULT_PE_RATIO = 31.6

# (See Appendix B for source code to obtain data)
AVGUPSIDES = {'Technology': {'largecap': -0.46532794252636306, 'midcap': -0.21392046923820554, 'smallcap': -0.21392046923820554}, 'Healthcare': {'largecap': -0.43055560930173425, 'midcap': -0.5719170423212125, 'smallcap': -0.21392046923820554}, 'Financial Services': {'largecap': 0.3029707379229806, 'midcap': 0.6715045600325802, 'smallcap': -0.21392046923820554}, 'Consumer Cyclical': {'largecap': 0.08440235744354845, 'midcap': -0.4348427886408699, 'smallcap': -0.21392046923820554}, 'Consumer Defensive': {'largecap': -0.2158942523257203, 'midcap': -0.21392046923820554, 'smallcap': -0.21392046923820554}, 'Industrials': {'largecap': -0.19325612805530254, 'midcap': 0.8031396239132172, 'smallcap': -0.21392046923820554}, 'Energy': {'largecap': 0.510275576264435, 'midcap': 0.5326022958942742, 'smallcap': -0.21392046923820554}, 'Utilities': {'largecap': -2.544612808703413, 'midcap': -3.427366258394338, 'smallcap': -0.21392046923820554}, 'Basic Materials': {'largecap': -0.06398120906354324, 'midcap': -2.4225627087099912, 'smallcap': -0.21392046923820554}, 'Real Estate': {'largecap': -0.3261417740317038, 'midcap': 0.9050036015731132, 'smallcap': -0.21392046923820554}, 'Communication Services': {'largecap': 1.343112974529212, 'midcap': 0.4747008587111436, 'smallcap': -0.21392046923820554}}

STARTDATE_LIST = ['2014-01-01', '2015-01-01', '2016-01-01', '2017-01-01', '2018-01-01'
                  '2019-01-01', '2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01', '2024-01-01']

# Decision Tables
"""
The key to the decision table is (P/E Ratio, Upside, Predicted Growth Rate) with True as outperforming S&P500 and False as underperforming

We determine the decision of buy, sell, hold, through on how many metrics the stock outperforms its peers.
If the stock outperforms in no metrics, we recommend to sell, if the stock outperforms in one metric we recommend to hold, and if the stock outperforms
in two or more metrics we recommend to buy. This is because while each metric on its own may not perfectly predict the growth of the stock, the more 
metric the stock outperforms in, we can be more condfident in its growth potential. 
"""
GROWTH_DECISION_TABLE = {(False, False, False): 'sell',
                         (True, False, False): 'hold',
                         (False, True, False): 'hold',
                         (False, False, True): 'hold',
                         (False, True, True): 'buy',
                         (True, False, True): 'buy',
                         (True, True, False): 'buy',
                         (True, True, True): 'buy'}

"""
The key to the decision table is (Predicted Dividend Yield, Beta, Principle Protection) with True as outperforming S&P500 and False as underperforming

The primary metric that we consider is the predicted dividend yield. However, since beta is a good metric that reflects how stable the stock is, 
or in other words, how reliable the dividend payout is, we only recommend to buy if the stock outperforms the S&P500 in both predicted dividend yields 
and beta since it is liklely that the stock will achieve a large dividend yield. 
Thus, in other cases when only one of the metrics (between predicted dividend yields and beta) outperforms S&P500, we recommend to hold since there 
is a potential (but not certain) for the stock to achieve a decent dividend yield, and if neither of them are outperforming, we recommend to sell.
Additionally, in all cases, we recommend to sell if the stock is predicted to produce a net loss or we cannot perform analysis on principle protection 
due to insufficient data in the next 5 years through principle protection analysis.
"""
INCOME_DECISION_TABLE = {(True, False, True): 'hold',
                         (False, True, True): 'hold',
                         (False, False, True): 'sell',
                         (True, True, True): 'buy',
                         (True, False, False): 'sell',
                         (False, True, False): 'sell',
                         (False, False, False): 'sell',
                         (True, True, False): 'sell'}

"""
The key to the decision table is (Decision of Growth Analysis, Decision of Income Analysis) 

If growth analysis recommends to sell or both analysis recommends to sell, the default strategy will recommend to sell, 
since this means that the stock is likley to underperform S&P500 or produce a net loss.
If income analysis recommends to sell but growth analysis recommends to hold or buy, the default strategy will recommend to hold, 
since this means that the stock is likley to underperform S&P500 in terms of income, but there is potential growth in stock value.
If either analysis recommends to buy (and the analysis doesn't recommend to sell), the default strategy will recommend to buy, 
since this means that the stock is likely to outperform S&P500 and produce a net gain.
If both analysis recommends to hold, the default strategy will recommend to hold.
"""
DEFAULT_DECISION_TABLE = {('buy', 'buy'): 'buy',
                          ('buy', 'hold'): 'buy',
                          ('buy', 'sell'): 'hold',
                          ('hold', 'buy'): 'buy',
                          ('hold', 'hold'): 'hold',
                          ('hold', 'sell'): 'sell',
                          ('sell', 'buy'): 'sell',
                          ('sell', 'hold'): 'sell',
                          ('sell', 'sell'): 'sell'}

"""
The key to the decision table is (Decision of Default Strategy, ESG Risk Score) with True as outperforming S&P500 and False as underperforming

- Default Strategy
If growth analysis recommends to sell or both analysis recommends to sell, the default strategy will recommend to sell, 
since this means that the stock is likley to underperform S&P500 or produce a net loss.
If income analysis recommends to sell but growth analysis recommends to hold or buy, the default strategy will recommend to hold, 
since this means that the stock is likley to underperform S&P500 in terms of income, but there is potential growth in stock value.
If either analysis recommends to buy (and the analysis doesn't recommend to sell), the default strategy will recommend to buy, 
since this means that the stock is likely to outperform S&P500 and produce a net gain.
If both analysis recommends to hold, the default strategy will recommend to hold.

- Default Strategy to ESG Strategy
When the default strategy is to sell, we always recommend to sell, since holding this stock will result in a loss.
When the default strategy is to hold, we recommend to sell if the ESG risk score is higher relative to its peer stocks and to buy if the ESG risk score is lower, 
since we prefer to increase the number of stocks that are ESG friendly in the portfolio and to decrease the number of stocks that are not ESG friendly.
When the default strategy is to buy, we recommend to hold if the ESG risk score is higher relative to its peer stocks and to buy if the ESG risk score is lower,
since we prefer not to increase the number of stocks that are not ESG friendly in the portfolio and to increase the number of stocks that are ESG friendly.
"""
ESG_DECISION_TABLE = {('buy', True): 'buy',
                      ('buy', False): 'hold',
                      ('hold', True): 'buy',
                      ('hold', False): 'sell',
                      ('sell', True): 'sell',
                      ('sell', False): 'sell'}

# %% [markdown]
# ## class GetInfo
# This class accesses yahooquery and returns information 
# 
# When there is no information available, it returns nan so that subsequent calculations can be performed and the program can produce a decision

# %%
class GetInfo():
    def __init__(self, stock):
        self.stock = stock
        try:
            # Attempt to fetch data
            self.Ticker = Ticker(stock)
        except ValueError as e: # TODO: do more error handling
            # Handle the error
            raise ValueError(f"Ticker does not exist. {e}")
        
    def current_price(self):
        try:
            current_price = self.Ticker.financial_data[self.stock]['currentPrice']
        except:
            try:
                current_price = self.Ticker.summary_detail[self.stock]['previousClose']
            except:
                current_price = float('nan')
        return current_price
    
    def free_cashflow(self):
        try:
            fcf = self.Ticker.cash_flow(trailing=False)['FreeCashFlow'].iloc[-1]
        except:
            fcf = float('nan')
        return fcf
    
    def shares_outstanding(self):
        try:
            shares_outstanding = self.Ticker.key_stats[self.stock]['sharesOutstanding']
        except:
            shares_outstanding = float('nan')
        return shares_outstanding
    
    def peratio(self):
        try:
            peratio = self.Ticker.valuation_measures['PeRatio'].iloc[-2] # current P/E for the stock
        except:
            peratio = float('nan')
        return peratio
    
    def beta(self):
        try:
            beta = self.Ticker.key_stats[self.stock]['beta']
        except:
            beta = float('nan')
        return beta
    
    def sector(self):
        try:
            sector = str(self.Ticker.asset_profile[self.stock]['sector'])
        except:
            sector = 'undefined'
        if sector not in WACC_RATES:
            WACC_RATES[sector] = DEFAULT_WACC_RATE
        if sector not in AVGPERATIOS:
            AVGPERATIOS[sector] = DEFAULT_PE_RATIO
        return sector
    
    def marketcap(self):
        try:
            marketcap = self.Ticker.price[self.stock]['marketCap']
        except:
            marketcap = float('nan')
        return marketcap
    
    def marketcap_type(self, marketcap):
        if marketcap >= 10000000000:
            return 'largecap'
        if marketcap < 10000000000 and marketcap >= 2000000000:
            return 'midcap'
        if marketcap < 2000000000:
            return 'smallcap'
        if math.isnan(marketcap):
            return 'undefined'
        
    def dividend_yield(self):
        try:
            dividend_yield = self.Ticker.summary_detail[self.stock]['dividendYield']
        except:
            dividend_yield = float('nan')
        return dividend_yield
    
    """
    Returns the longest available history of dividends by year (as far back as 2014-01-01)
    If dividend history doesn't exist, returns None
    """
    def dividend_history(self):
        for start_date in STARTDATE_LIST:
            try:
                dividend = self.Ticker.dividend_history(start = start_date)
                if dividend.shape[0] != 0:
                    dividend_history = dividend['dividends']
                    dividend_history = pd.DataFrame(dividend_history.items(), columns=['date', 'dividends'])
                    dividend_history = dividend_history.explode('date').reset_index(drop=True)
                    dividend_history = dividend_history[dividend_history['date'] != self.stock]
                    dividend_history = dividend_history.reset_index(drop=True)

                    # Convert 'date' column to datetime
                    dividend_history['date'] = pd.to_datetime(dividend_history['date'])
                    # Group by year and sum up dividends
                    dividend_history = dividend_history.groupby(dividend_history['date'].dt.year)['dividends'].sum()
                    dividend_history = dividend_history.drop(dividend_history.index[-1])
                    dividend_history = dividend_history.rename_axis('year').reset_index(name='dividends')
                    return dividend_history['dividends']
            except Exception as e:
                pass
        return []

    """
    Returns the longest available history of price by interval specified (as far back as 2014-01-01)
    If price history doesn't exist, returns None
    """
    def price_history(self, interval):
        for start_date in STARTDATE_LIST:
            try:
                price_history = np.array(self.Ticker.history(start=start_date, interval=interval)['close'])
                if price_history.size != 0:
                    return price_history
            except Exception as e:
                pass
        return []
        
    
    """
    Returns dictionary with all esg scores info and peer esg scores info (dictionary with min, avg, max)
    Returns None if any of the information cannot be accessed
    """
    def esg_scores(self):
        try:
            esg_score_dict = self.Ticker.esg_scores[self.stock]
        except:
            esg_score_dict = None
        return esg_score_dict


# %% [markdown]
# ## class Analysis
# This class defines all the necessary analysis models for income and growth analyses
# - predict_growth
# 
#     This function creates a linear regression model using the scikit-learn library, and predicts the value for future time points, given a sequence of data from past time points.
# - compare_predictions
#     
#     This function compares two sequences of data and returns at how many time points the first sequence is greater than the second. 
#     
#     It is used to compare the predicted dividend yields for a stock against the S&P500 ETF.
# 
# - predict_fiveyr_price
# 
#     This function retrieves the history of stock prices and calls the predict_growth function to return a prediction of stock prices for the next 5 years.
# 
# - predict_fiveyr_dividend
# 
#     This function retrieves the history of dividends and calls the predict_growth function to return a prediction of dividends for the next 5 years.
# 
# - calculate_dcf_intrinsic_value
# 
#     This function calculates the intrinsic value of a stock, based on a DCF analysis. It retrieves data on free cash flow and calculates the discounted cash flow based on the wacc rates. Ref: https://www.investopedia.com/terms/i/intrinsicvalue.asp 
# 
# - calculate_upside
# 
#     This function calculates a stock's upside, given the intrinsic value.

# %%
class Analysis():
    def __init__(self, stock):
        self.stock = stock
        self.info = GetInfo(stock)
        self.sector = self.info.sector()
        self.current_price = self.info.current_price()

    # FOR GROWTH AND INCOME
    def predict_growth(self, data, time_points):
        X = np.arange(len(data)).reshape(-1, 1)
        y = data

        # Create and fit the linear regression model
        model = LinearRegression()
        model.fit(X, y)

        # Predict growth for the next time points
        future_time_points = np.arange(len(data), len(data) + time_points).reshape(-1, 1)
        predicted_growth = model.predict(future_time_points)

        return list(predicted_growth)
    
    def compare_predictions(self, stock_preds, sp_preds):
        stock = 0
        nan_count = 0
        total = len(stock_preds)
        for i in range(total):
            stock_pred= stock_preds[i]
            sp_pred = sp_preds[i]
            if (not math.isnan(stock_pred)) and (not math.isnan(sp_pred)):
                if stock_pred >= sp_pred:
                    stock += 1
            else:
                nan_count += 1
        if nan_count == total:
            return float('nan')
        return stock
    
    def predict_fiveyr_price(self):
        # Set pred num to 60 because we want to predict 5 years (60months) ahead
        price_history = self.info.price_history('1mo')
        if len(price_history) == 0:
            return []
        price_pred_fiveyrs = []
        price_pred = self.predict_growth(price_history, 60)
        index_list = [11, 23, 35, 47, 59]
        for index in index_list:
            price_pred_fiveyrs.append(price_pred[index])
        return price_pred_fiveyrs
    
    # FOR INCOME
    def predict_fiveyr_dividend(self):
        dividend_history = self.info.dividend_history()
        if len(dividend_history) == 0:
            return []
        return self.predict_growth(dividend_history, 5)

    # FOR GROWTH
    def calculate_dcf_intrinsic_value(self):
        # Assuming constant growth rate for simplicity
        growth_rate = GROWTH_RATE 
        # Discount rate
        discount_rate = WACC_RATES[self.sector]  
        # Get last year free cash flow
        fcf = self.info.free_cashflow()
        # Get the number of shares outstanding
        shares_outstanding = self.info.shares_outstanding()
        # Calculate terminal value using perpetual growth formula
        terminal_value = (fcf * (1 + growth_rate)) / (discount_rate - growth_rate)
        # Discount each year's cash flow
        discounted_cash_flows = [fcf / (1 + discount_rate) ** i for i in range(1, 6)]  # Discounting cash flows for 5 years
        # Add terminal value
        discounted_cash_flows.append(terminal_value / (1 + discount_rate) ** 5)
        # Calculate intrinsic value
        intrinsic_value = np.sum(discounted_cash_flows) / shares_outstanding

        return intrinsic_value
    
    def calculate_upside(self, intrinsic_value):
        return intrinsic_value/self.current_price - 1

# %% [markdown]
# ## class Decisions
# This class returns a decision or explanation for a given stock and client type
# - income
# 
#     The income analysis considers three metrics: predicted dividend yield, beta, and principle protection
# 
#     - Predicted dividend yield is derived through the predicted dividends and stock prices through linear regression, and is set to True if it outperforms the predicted dividend yield of S&P500 for more than 2 of the next 5 years.
# 
#     - Beta is obtained from yahooquery, and is set to True if it is less than or equal to 1.
# 
#     - Principle protection is derived as the sum of predicted stock price delta between now and 5 years from now and sum of predicted dividends over the next 5 years. It is set to True if it is above or equal to 0 (net gain). 
# 
#     - Given these 3 metrics, the analysis returns a decision based on the income decision table (description for decision is in global variables section).
# - growth
# 
#     The growth analysis considers three metrics: P/E ratio, upside, and predicted stock price growth
# 
#     - P/E ratio is obtained from yahooquery, and is set to True if it is greater than or equal to the average P/E ratio of the sector / market cap group the stock is in.
# 
#     - Upside is calculated through a DCF analysis of intrinsic value, and is set to True if it is greater than or equal to the average upside of the sector / market cap group the stock is in.
# 
#     - For both P/E ratio and upside, we compare it to the average of the sector / market cap group the stock is in, since they tend to vary a lot between sectors and market caps, and using the same threshold for all stocks will favor some sectors or market caps over others and hinder portfolio diversification.
# 
#     - Predicted stock price growth is derived through the predicted stock prices through linear regression, and is set to True if the 5 year growth rate outperforms the predicted stock price growth of S&P500.
# 
#     - Given these 3 metrics, the analysis returns a decision based on the growth decision table (description for decision is in global variables section).
# - default
#     
#     The default analysis makes a decision based on the combination of decisions that the income analysis and growth analysis returns.
#     Given these 2 decisions, the analysis returns a decision based on the default decision table (description for decision is in global variables section).
# - esg
# 
#     The esg analysis considers the ESG risk score and defaut analysis decison to make a decision.
#     The ESG risk score is obtained from yahooquery, and is set to True if it is smaller than or equal to the average ESG risk score of its peers.
#     Given the 2 metrics, the analysis returns a decision based on the ESG decision table (description for decision is in global variables section).
# - get_explanation
# 
#     Returns the descriptions of the metrics and decision processes that led to the decision.
# 

# %%
class Decisions():
    def __init__(self, stock):
        self.stock = stock
        self.info = GetInfo(self.stock)
        self.strategy = Analysis(self.stock)
        self.beta = self.info.beta()
        self.sector = self.info.sector()
        self.marketcap = self.info.marketcap()
        self.current_price = self.info.current_price()
        self.marketcap_type = self.info.marketcap_type(self.marketcap)

        # For default (income and growth)
        self.default_decision = None
        # Predict stock price for next 5 years
        # Set pred num to 60 because we want to predict 5 years (60months) ahead
        self.price_pred_fiveyrs = self.strategy.predict_fiveyr_price()
        # Predict stock price for next 5 years
        # Set pred num to 60 because we want to predict 5 years (60months) ahead
        self.sp_strategy = Analysis('SPY')
        self.sp_price_pred_fiveyrs = self.sp_strategy.predict_fiveyr_price()
        self.sp_info = GetInfo('SPY')
        self.sp_current_price = self.sp_info.current_price()
        self.fiveyr_delta = self.price_pred_fiveyrs[-1] - self.current_price
        self.sp_fiveyr_delta = self.sp_price_pred_fiveyrs[-1] - self.sp_current_price
        self.fiveyr_delta_rate = (self.price_pred_fiveyrs[-1] - self.current_price) / self.current_price
        self.sp_fiveyr_delta_rate = (self.sp_price_pred_fiveyrs[-1] - self.sp_current_price) / self.sp_current_price

        # For growth
        self.growth_decision = None
        self.peratio = None
        self.sector_peratio_average = None
        self.upside = None
        self.intrinsic_value = None
        self.sector_upside_average = None
        self.peratio_flag = False
        self.upside_flag = False
        self.fiveyr_growth_flag = False

        # For income
        self.income_decision = None
        self.dividend_pred_fiveyrs = None
        self.dividend_yield_pred_fiveyrs = None
        self.sp_dividend_pred_fiveyrs = None
        self.sp_dividend_yield_pred_fiveyrs = None
        self.dividend_yield_performance = None
        self.dividend_yield_flag = False
        self.beta_flag = False
        self.principle_protection_flag = False
        self.no_dividend_flag = False
        self.missing_principle_protection_flag = False

        # For ESG
        self.esg_decision = None
        self.esg_flag = False
        self.esg_risk_score = None
        self.peer_esg_risk_score = None
        self.no_esg_score_flag = False

    def default(self) -> str:
        # The default strategy combines the income and growth metrics to make a decision
        growth_decision = self.growth()
        income_decision = self.income()
        self.default_decision = DEFAULT_DECISION_TABLE[(growth_decision, income_decision)]
        return self.default_decision

    def income(self) -> str:
        dividend_history = self.info.dividend_history()
        if len(dividend_history) == 0:
            self.no_dividend_flag = True
            self.income_decision = 'sell'
            return self.income_decision
        # Predict dividend for next 5 years
        self.dividend_pred_fiveyrs = self.strategy.predict_growth(dividend_history, 5)
        # Perform element-wise division to calculate dividend yield for next 5 years
        self.dividend_yield_pred_fiveyrs = [a / b for a, b in zip(self.dividend_pred_fiveyrs, self.price_pred_fiveyrs)]
        
        # Calculate the predicted dividend yield for a S&P500 ETF to compare as baseline
        # Predict s&p dividend for next 5 years
        spy_dividend_history = self.sp_info.dividend_history()
        self.sp_dividend_pred_fiveyrs = self.sp_strategy.predict_growth(spy_dividend_history, 5)
        # Perform element-wise division to calculate dividend yield for next 5 years

        self.sp_dividend_yield_pred_fiveyrs = [a / b for a, b in zip(self.sp_dividend_pred_fiveyrs, self.sp_price_pred_fiveyrs)]

        # Make decision
        
        self.dividend_yield_performance = self.strategy.compare_predictions(self.dividend_yield_pred_fiveyrs, self.sp_dividend_yield_pred_fiveyrs)
        if self.dividend_yield_performance >= 3:
            self.dividend_yield_flag = True

        if self.beta <= 1:
            self.beta_flag = True

        if math.isnan(self.fiveyr_delta) or math.isnan(sum(self.dividend_pred_fiveyrs)):
            self.missing_principle_protection_flag = True
            self.income_decision = 'sell'
            return self.income_decision
        if self.fiveyr_delta + sum(self.dividend_pred_fiveyrs) >= 0:
            self.principle_protection_flag = True

        # Return decision based on decision table
        self.income_decision = INCOME_DECISION_TABLE[(self.dividend_yield_flag, self.beta_flag, self.principle_protection_flag)]
        return self.income_decision
    
    def growth(self) -> str:
        self.intrinsic_value = self.strategy.calculate_dcf_intrinsic_value()
        self.upside = self.strategy.calculate_upside(self.intrinsic_value)
        self.peratio = self.info.peratio()
        self.sector_peratio_average = AVGPERATIOS[self.sector]
        
        if self.marketcap_type != 'undefined':
            self.sector_upside_average = AVGUPSIDES[self.sector][self.marketcap_type]

        # Make decision
        if self.upside >= self.sector_upside_average:
            self.upside_flag = True

        if self.peratio >= self.sector_peratio_average:
            self.peratio_flag = True
        
        # Check if the predicted price change for next 5 years is greater than S&P500 or not are going down significantly
        if self.fiveyr_delta_rate >= self.sp_fiveyr_delta_rate:
            self.fiveyr_growth_flag = True

        self.growth_decision = GROWTH_DECISION_TABLE[(self.upside_flag, self.peratio_flag, self.fiveyr_growth_flag)]

        return self.growth_decision
    
    def esg(self) -> str:
        esg_risk_scores = self.info.esg_scores()
        
        if esg_risk_scores == None or isinstance(esg_risk_scores, str):
            self.no_esg_score_flag = True
            self.esg_decision = self.default()
            return self.esg_decision

        self.esg_risk_score = esg_risk_scores['totalEsg']
        self.peer_esg_risk_score = esg_risk_scores['peerEsgScorePerformance']['avg']

        if self.esg_risk_score <= self.peer_esg_risk_score:
            self.esg_flag = True
        
        self.esg_decision = ESG_DECISION_TABLE[(self.default(), self.esg_flag)]
        
        return self.esg_decision
    
    def get_explanation(self, type):
        match type:
            case 'income':
                explanation = self.income_explanation()
                
            case 'growth':
                explanation = self.growth_explanation()
   
            case 'esg':
                explanation = self.esg_explanation()

            case _:
                explanation = self.default_explanation()
        
        return explanation
    
    def performance(self, boolean):
        if boolean:
            return 'outperforms'
        else:
            return 'underperforms'
        
    def beta_performance(self, beta):
        if beta > 1:
            return 'larger'
        if beta <= 1:
            return 'equal to or smaller'
        
    def income_explanation(self):
        # Check if the stock has never paid dividends in the past 10 years
        if self.no_dividend_flag:
            explanation = f"""
According to the income analysis, we recommend to {self.income_decision} {self.stock}.
{self.stock} has never paid dividends to its share holders or there is no data available to determine the dividend pay in the past 10 years, 
and thus we believe that they will not pay dividends in the near future. 
Therefore, the Income Analysis yields a recommendation to {self.income_decision} {self.stock}."""
        else:
            explanation = f"""
[Introduction]
According to the income analysis, we recommend to {self.income_decision} {self.stock}. 
If the stock has historically paid dividends, this program analyzes the predicted future dividend yields of the stock and the beta of the stock, 
and considers principle protection to make a decision on income portfolio stocks.
We use S&P500 as the baseline, and analyze whether the stock will outperform S&P500 or not, and buy or hold if it will, and sell if it will not.

[Explanation of Analyses]
Analysis 1: Dividend yield prediction based on stock price prediction and dividend growth prediction through linear regression on historical data
Dividend yeild prediction using linear regression on historical data involves using past dividend growth data to create a linear model that predicts dividends, 
and combines this with a stock price prediction model which uses past price data to create a linear model that predicts future stock prices. 
Then, we divide the predicted dividends by the predicted stock prices in order to obtain the predicted dividend yields for the next 5 years.
In this program, we compare these predicted dividend yields of a given stock with the predicted dividend yields of the S&P500 ETF (SPY), 
and determine a stock to be outperforming S&P500 if the stock's predicted dividend yield is equal to or greater than that of the S&P500 ETF's 
majority of the years (>2years out of 5).

Analysis 2: Beta
Beta, a measure of a stock's volatility compared to the market, serves as a valuable tool when determining the suitability of a stock for an income portfolio. 
Stocks with beta values less than 1 typically exhibit lower volatility than the market, and these low beta stocks often belong to established companies 
in mature industries, known for their consistent earnings and dividend payments. By including such stocks in an income portfolio, 
investors can mitigate risk and ensure a smoother income stream. 
In this program, we determine a stock to be outperforming S&P500 in terms of it's stability if the stock has a beta equal to or smaller than one, 
and underperforming if greater than one.

Analysis 3: Principle protection
Although an income portfolio focuses on the dividend yields more than the growth, in order to prevent net losses by holding the stock, 
we also consider net gain of holding the stock. In other words, we add up the predicted dividend payouts per stock for the next 5 years 
and sum it with the predicted delta of stock price (predicted stock price in 5 years - current price).
If this sum is less than 0, we recommend to sell, since we predict that the stock will produce a net loss.

[Results of Analyses]
Analysis 1:
{'The analysis on predicted dividend yields could not be performed due to insufficient data.' if math.isnan(self.dividend_yield_performance) else f"""{self.stock} has predicted dividend yields of {["{:.4f}".format(num) for num in self.dividend_yield_pred_fiveyrs]} over the next 5 years,
and the predicted dividend yields for S&P500 is {["{:.4f}".format(num) for num in self.sp_dividend_yield_pred_fiveyrs]}.
Therefore, {self.stock} is predicted to have a higher dividend yield than S&P500 in {self.dividend_yield_performance} of the next 5 years, which means that
{self.stock} {self.performance(self.dividend_yield_flag)} S&P500 in predicted dividend yields."""}

Analysis 2:
{self.stock}'s beta is {'not available.' if math.isnan(self.beta) else f"""{self.beta:.2f}, which is {self.beta_performance(self.beta)} than one.
Therefore, {self.stock} {self.performance(self.beta_flag)} S&P500 in beta."""}

Analysis 3:
{'The analysis on principle protection could not be performed due to insufficient data.' if self.missing_principle_protection_flag else f"""The predicted sum of dividend payments of {self.stock} in the next 5 years is {sum(self.dividend_pred_fiveyrs):.2f},
and the predicted delta of the stock price between the current price and the predicted price in 5 years is {self.fiveyr_delta:.2f}.
Thus, the sum of the two is {(self.fiveyr_delta + sum(self.dividend_pred_fiveyrs)):.2f}, which is {'equal to or greater' if self.principle_protection_flag else 'smaller'} than 0, 
and therefore, {self.stock} will produce a net {'gain' if self.principle_protection_flag else 'loss'} in the next 5 years."""}

[Decision Process]
The primary metric that we consider is the predicted dividend yield. However, since beta is a good metric that reflects how stable the stock is, 
or in other words, how reliable the dividend payout is, we only recommend to buy if the stock outperforms the S&P500 in both predicted dividend yields 
and beta since it is liklely that the stock will achieve a large dividend yield. 
Thus, in other cases when only one of the metrics (between predicted dividend yields and beta) outperforms S&P500, 
we recommend to hold since there is a potential (but not certain) for the stock to achieve a decent dividend yield, 
and if neither of them are outperforming, we recommend to sell.
Additionally, in all cases, we recommend to sell if the stock is predicted to produce a net loss or we cannot perform analysis on principle protection 
due to insufficient data in the next 5 years through principle protection analysis.

[Conclusion]
"""
            if self.missing_principle_protection_flag:
                conclusion = f'Overall, since we cannot perform analysis on principle protection, the income analysis yields a recommendation to {self.income_decision} {self.stock}.'
            else:
                flags = [self.dividend_yield_flag, self.beta_flag, self.principle_protection_flag]
                count_true = sum(flags)
                if not self.dividend_pred_fiveyrs:
                    conclusion = 'Overall, since the stock does not achieve principle protection (produces a net loss) '
                    if count_true == 0:
                        conclusion += f'and underperforms or has insufficient data to perform analysis in predicted 5 year dividend yield and beta'
                    else:
                        if self.dividend_yield_flag and self.beta_flag:
                            conclusion += f'although the stock outperforms in predicted 5 year dividend yield and beta'
                        elif self.dividend_yield_flag:
                            conclusion += f'although the stock outperforms in predicted 5 year dividend yield and underperforms or has insufficient data to perform analysis in beta'
                        else:
                            conclusion += f'although the stock outperforms in beta and underperforms or has insufficient data to perform analysis in predicted 5 year dividend yield'
                else:
                    conclusion = 'Overall, the stock achieves principle protection (produces a net gain), '
                    if count_true == 1:
                        conclusion += f'however, it underperforms or has insufficient data to perform analysis in predicted 5 year dividend yield and beta'
                    else:
                        if self.dividend_yield_flag and self.beta_flag:
                            conclusion += f'and outperforms in predicted 5 year dividend yield and beta'
                        elif self.dividend_yield_flag:
                            conclusion += f'and outperforms in predicted 5 year dividend yield but underperforms or has insufficient data to perform analysis in beta'
                        else:
                            conclusion += f'and outperforms in beta but underperforms or has insufficient data to perform analysis in predicted 5 year dividend yield'
                conclusion += f', thus according to the decision process described above, the Income Analysis yields a recommendation to {self.income_decision} {self.stock}.'
            explanation += conclusion

        return explanation

    def growth_explanation(self):
        explanation = f"""
[Introduction]
According to the growth analysis, we recommend to {self.growth_decision} {self.stock}. 
This program performs two fundamental analyses and a stock price prediction to make a decision on growth portfolio stocks.
We use S&P500 as the baseline, and analyze whether the stock will outperform S&P500 or not, and buy or hold if it will, and sell if it will not.

[Preliminary Information]
- {self.stock} is in the {self.sector} sector and is {self.marketcap_type}

[Explanation of Analyses]
Analysis 1: P/E ratio
The Price-to-Earnings (P/E) ratio is a fundamental financial metric used to assess the valuation of a company's stock by dividing 
its current market price per share by its earnings per share (EPS). 
It enables investors to compare the stock's price to its earnings, aiding in determining whether it's overvalued, undervalued, 
or fairly valued relative to peers or the market. 
Moreover, the P/E ratio provides insights into growth expectations, with a higher ratio suggesting higher anticipated earnings growth and vice versa, 
and also serves as a risk assessment tool, as a higher P/E ratio may indicate greater risk associated with the investment. 
In essence, the P/E ratio offers a concise means for investors to gauge market sentiment, make valuation comparisons, and assess investment risk.
In this program, we compare the P/E ratio to the average P/E ratios of the sector/market cap size  that the stock is in and determine a stock 
to be outperforming if the P/E ratio is equal to or greater than that of the average.

Analysis 2: Upside obtained through DCF Analysis of Intrinsic Value
DCF (Discounted Cash Flow) Analysis calculates the intrinsic value of a stock by estimating its future cash flows and discounting them 
back to present value using a discount rate. It provides investors with a valuation based on the net present value of expected future cash flows, 
aiding in determining whether a stock is undervalued or overvalued.
In this program, we calculate the intrinsic value based on a DCF analysis, 
and compare it to the current value in order to obtain the upside of the stock, 
and compare the stock's upside with the average upside of the sector/market cap size that the stock is in.
The upside of the stock is calculated by (intrinsic value - current stock price) / current stock price, 
and therefore the larger the upside, the more undervalued the stock is (i.e. we analyze that the stock price should go up in the future), 
and thus would support the decision to buy or hold.
We determine the stock to be outperforming if its upside is equal to or greater than that of the average.

Analysis 3: Predicted stock price growth rate based on linear regression on historical stock prices
Stock price prediction using linear regression on historical stock prices involves using past price data to create a linear model that predicts future prices. 
By analyzing historical price trends, the model estimates future price movements.  
This approach assists investors in making decisions based on projected price movements and identifying potential buying or selling opportunities.
In this program, we predict the stock price for the next 5 years and incorporate it into our decision process.
In other words, if the predicted stock price growth is high, it will support the decision to buy/hold, and if it is low, it will support the decision to sell.
We determine the stock to be outperforming if the predicted stock price growth is equal to or greater than that of S&P500.

For both P/E ratio and upside, we compare it to the average of the sector / market cap group the stock is in, since they tend to vary 
a lot between sectors and market caps, and using the same threshold for all stocks will favor some sectors or market caps over others 
and hinder portfolio diversification.

[Results of Analyses]
Analysis 1:
{self.stock}'s P/E ratio is {'not available' if math.isnan(self.peratio) else f"""{self.peratio:.2f} and the average P/E ratio for all stocks in S&P500 in the {self.sector} sector that are {self.marketcap_type} is {self.sector_peratio_average:.2f}.
Therefore, {self.stock} {self.performance(self.peratio_flag)} peer stocks in P/E ratio."""}

Analysis 2:
The DCF analysis on {self.stock} {'could not be performed, since there was insufficient information available' if math.isnan(self.intrinsic_value) else f"""yields an intrinsic value of {self.intrinsic_value:.2f}.
Since the current price of {self.stock} is {self.current_price:.2f}, this yields an upside of {self.upside:.2f}.
The average upside for all the stocks in the S&P500 in the {self.sector} sector that are {self.marketcap_type} is {self.sector_upside_average:.2f}.
Therefore, {self.stock} {self.performance(self.upside_flag)} peer stocks in upside."""}

Analysis 3:
The linear regression model on past stock prices of {self.stock} {'could not be calculated, since there was no price data available.'if len(self.price_pred_fiveyrs) == 0 else f"""predicts the stock price of {self.stock} for the next 5 years to be {["{:.2f}".format(num) for num in self.price_pred_fiveyrs]}.
This yields a predicted growth rate of {self.fiveyr_delta_rate:.2f} over the next five years for {self.stock}.
The average predicted growth rate of S&P500 stocks is {self.sp_fiveyr_delta_rate:.2f}.
Therefore, {self.stock} {self.performance(self.fiveyr_growth_flag)} peer stocks in predicted growth rate in the next 5 years."""}

[Decision Process]
We determine the decision of buy, sell, hold, through on how many metrics the stock outperforms its peers.
If the stock outperforms in no metrics, we recommend to sell, if the stock outperforms in one metric we recommend to hold, 
and if the stock outperforms in two or more metrics we recommend to buy.
This is because while each metric on its own may not perfectly predict the growth of the stock, the more metric the stock outperforms in, 
we can be more condfident in its growth potential. 

[Conclusion]
"""
        analyses = ['P/E ratio analysis, ', 'upside analysis, ', '5 year growth rate analysis, ']
        flags = [self.peratio_flag, self.upside_flag, self.fiveyr_growth_flag]
        count_true = sum(flags)
        conclusion = f'Overall, since the stock outperforms S&P500 in '
        if count_true == 0:
            conclusion += f'none of the analyses, '
        elif count_true == 3:
            conclusion += f'all of the analyses, '
        else:
            for index, flag in enumerate(flags):
                if flag:
                    conclusion += analyses[index]
            conclusion += 'but underperforms S&P500 or has insufficient data to perform analysis in '
            for index, flag in enumerate(flags):
                if not flag:
                    conclusion += analyses[index]
        conclusion += f'the Growth Analysis yields a recommendation to {self.growth_decision} {self.stock}.'
        
        explanation += conclusion
    
        return explanation

    def default_explanation(self):
        explanation = f"""
[Introduction]
For a default portfolio, we recommend to {self.default_decision} {self.stock}. 
The strategy for a default portfolio stock is to perform both growth and income analysis and combine the result of the two.
The growth analysis performs two fundamental analyses and a stock price prediction to make a decision on the growth potential of the stock,
and if the stock has historically paid dividends, the income analysis analyzes the predicted future dividend yields of the stock and the beta of the stock, 
and considers principle protection to make a decision on the income potential of the stock.
A detailed description of both growth and income analysis is appended below.

[Decision Process]
If growth analysis recommends to sell or both analysis recommends to sell, the default strategy will recommend to sell, 
since this means that the stock is likley to underperform S&P500 or produce a net loss.
If income analysis recommends to sell but growth analysis recommends to hold or buy, the default strategy will recommend to hold, 
since this means that the stock is likley to underperform S&P500 in terms of income, but there is potential growth in stock value.
If either analysis recommends to buy (and the analysis doesn't recommend to sell), the default strategy will recommend to buy, 
since this means that the stock is likely to outperform S&P500 and produce a net gain.
If both analysis recommends to hold, the default strategy will recommend to hold.

[Results of Analyses and Conclusion]
For {self.stock}, the recommendation based on growth analysis is to {self.growth_decision}, 
and the recommendation based on income analysis is to {self.income_decision}.
Therefore, for a Default Portfolio, we recommend to {self.default_decision}.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Description of the growth analysis:
"""
        explanation += self.growth_explanation()
        explanation += """
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Description of the income analysis:
"""
        explanation += self.income_explanation()
        return explanation
    
    def esg_explanation(self):
        explanation = ""
        if self.no_esg_score_flag:
            explanation += f"""
[Introduction]
For an ESG portfolio, we recommend to {self.esg_decision} {self.stock}. 
Generally, the strategy for a ESG portfolio stock is to perform both growth and income analysis, combine the result of the two to obtain a default strategy, 
and consider the ESG risk score of the stock to adjust the recommendation. 
However, {self.stock} does not have ESG data. Therefore, we provide a recommendation based on just the default strategy.
A detailed description of both growth and income analysis is appended below.

[Decision Process]
- Default Strategy
If growth analysis recommends to sell or both analysis recommends to sell, the default strategy will recommend to sell, 
since this means that the stock is likley to underperform S&P500 or produce a net loss.
If income analysis recommends to sell but growth analysis recommends to hold or buy, the default strategy will recommend to hold, 
since this means that the stock is likley to underperform S&P500 in terms of income, but there is potential growth in stock value.
If either analysis recommends to buy (and the analysis doesn't recommend to sell), the default strategy will recommend to buy, 
since this means that the stock is likely to outperform S&P500 and produce a net gain.
If both analysis recommends to hold, the default strategy will recommend to hold.

[Results of Analyses and Conclusion]
For {self.stock}, the recommendation based on growth analysis is to {self.growth_decision}, and the recommendation based on income analysis is to {self.income_decision}.
Therefore, the Default Strategy is to {self.default_decision}, and thus for a ESG portfolio, we also recommend to {self.esg_decision}.
"""
        else:
            explanation += f"""
[Introduction]
For an ESG portfolio, we recommend to {self.esg_decision} {self.stock}. 
The strategy for a ESG portfolio stock is to perform both growth and income analysis, combine the result of the two to obtain a default strategy, 
and consider the ESG risk score of the stock to adjust the recommendation.
A detailed description of both growth and income analysis is appended below.

[Decision Process]
- Default Strategy
If growth analysis recommends to sell or both analysis recommends to sell, the default strategy will recommend to sell, 
since this means that the stock is likley to underperform S&P500 or produce a net loss.
If income analysis recommends to sell but growth analysis recommends to hold or buy, the default strategy will recommend to hold, 
since this means that the stock is likley to underperform S&P500 in terms of income, but there is potential growth in stock value.
If either analysis recommends to buy (and the analysis doesn't recommend to sell), the default strategy will recommend to buy, 
since this means that the stock is likely to outperform S&P500 and produce a net gain.
If both analysis recommends to hold, the default strategy will recommend to hold.

- Default Strategy to ESG Strategy
When the default strategy is to sell, we always recommend to sell, since holding this stock will result in a loss.
When the default strategy is to hold, we recommend to sell if the ESG risk score is higher relative to its peer stocks and to buy if the ESG risk score is lower, 
since we prefer to increase the number of stocks that are ESG friendly in the portfolio and to decrease the number of stocks that are not ESG friendly.
When the default strategy is to buy, we recommend to hold if the ESG risk score is higher relative to its peer stocks and to buy if the ESG risk score is lower,
since we prefer not to increase the number of stocks that are not ESG friendly in the portfolio and to increase the number of stocks that are ESG friendly.

[Results of Analyses and Conclusion]
For {self.stock}, the recommendation based on growth analysis is to {self.growth_decision}, and the recommendation based on income analysis is to {self.income_decision}.
Therefore, the default strategy is to {self.default_decision}. 
The ESG risk score for {self.stock} is {self.esg_risk_score:.2f} and the ESG risk score average for peer stocks is {self.peer_esg_risk_score:.2f}, which means that {self.stock} {self.performance(self.esg_flag)} compared to its peer stocks in ESG risk score.
Since the Default Strategy is to {self.default_decision} and the stock {self.performance(self.esg_flag)} in terms of ESG, for a ESG portfolio, we recommend to {self.esg_decision}.
"""
        explanation += f"""
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Description of the growth analysis:
"""
        explanation += self.growth_explanation()
        explanation += """
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Description of the income analysis:
"""
        explanation += self.income_explanation()
        return explanation

# %%
# Calls the Decisions class to obtain the decision and explanation and returns them as a tuple
def invest(ticker, client=False):
    # Check if ticker is valid
    if Ticker(ticker).history(period='1d').empty:
        sys.exit("Ticker does not exist.")
    decision_maker = Decisions(ticker)
    match client:
        case 'income':
            decision = decision_maker.income()
            explanation = decision_maker.get_explanation(client)
        case 'growth':
            decision = decision_maker.growth()
            explanation = decision_maker.get_explanation(client)
        case 'esg':
            decision = decision_maker.esg()
            explanation = decision_maker.get_explanation(client)
        case False:
            decision = decision_maker.default()
            explanation = decision_maker.get_explanation(client)
        case _:
            ValueError(f"Client type {client} is not supported")
    return (decision, explanation)

# %% [markdown]
# # Examples

# %% [markdown]
# ## Growth (buy): Amazon

# %%
stock = 'AMZN'
client = 'growth' 

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## Growth (hold): WRB

# %%
stock = 'WRB'
client = 'growth' 

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## Growth (sell): AFL

# %%
stock = 'AFL'
client = 'growth' 

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## Income (buy): AT&T

# %%
stock = 'T'
client = 'income' 

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## Income (hold): CTVA

# %%
stock = 'CTVA'
client = 'income' 

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## Income (sell): APH

# %%
stock = 'APH'
client = 'income' 

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## ESG (buy): ACN

# %%
stock = 'ACN'
client = 'esg'

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## ESG (hold): FMC
# 

# %%
stock = 'FMC'
client = 'esg'

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## ESG (sell): CAT

# %%
stock = 'CAT'
client = 'esg'

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# # Edge Case Examples

# %% [markdown]
# ## Invalid Stock

# %%
stock = 'invalid_ticker'

decision, explanation = invest(stock)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## ESG Information Missing/Unavailable

# %%
stock = 'AMCR'
client = 'esg'

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## No Dividend History/Dividend Information Missing

# %%
stock = 'TSLA'
client = 'income'

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# ## P/E Ratio Information Missing/Unavailable

# %%
stock = 'MMM'
client = 'growth'

decision, explanation = invest(stock, client)
print('Recommendation:', decision)
print('Explanation:', explanation)

# %% [markdown]
# # Appendix
# Recommended not to run due to long run time (~ 1 hour/appendix)

# %% [markdown]
# ## Appendix A
# Code to obtain 'AVGPERATIOS'

# %%
AVGPERATIOS = {'Technology': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Healthcare': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Financial Services': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Consumer Cyclical': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Consumer Defensive': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Industrials': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Energy': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Utilities': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Basic Materials': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Real Estate': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Communication Services': {'largecap': [], 'midcap': [], 'smallcap': []}}
# Obtained from sources NYU stern website for each sector (if insufficient data from S&P500 stocks)
default_pe_ratio = float('nan')

# Obtain P/E ratios for all stocks in S&P500
for ticker in SP_LIST[:20]:
    info = GetInfo(ticker)
    sector = info.sector()
    marketcap = info.marketcap_type(info.marketcap())
    peratio = info.peratio()
    AVGPERATIOS[sector][marketcap].append(peratio)

# Calculate the average peratios for each sector and capsize
for sector in SECTORS:
    for marketcap in MARKETCAPS:
        # Remove all 'nan' values
        peratios = [x for x in AVGPERATIOS[sector][marketcap] if str(x) != 'nan']
        # If insufficient data from S&P500 stocks, use default value
        if len(peratios) != 0:
            AVGPERATIOS[sector][marketcap] = sum(peratios)/len(peratios)
        else:
            AVGPERATIOS[sector][marketcap] = default_pe_ratio


# %% [markdown]
# ## Appendix B
# Code to obtain 'AVGUPSIDES'

# %%
AVGUPSIDES = {'Technology': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Healthcare': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Financial Services': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Consumer Cyclical': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Consumer Defensive': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Industrials': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Energy': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Utilities': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Basic Materials': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Real Estate': {'largecap': [], 'midcap': [], 'smallcap': []}, 'Communication Services': {'largecap': [], 'midcap': [], 'smallcap': []}}
# Obtained from sources NYU stern website for each sector (if insufficient data from S&P500 stocks)
default_upsides = float('nan')

# Calculate the upside for all stocks in S&P500
for ticker in SP_LIST[:20]:
    info = GetInfo(ticker)
    sector = info.sector()
    marketcap = info.marketcap_type(info.marketcap())
    strategy = Analysis(ticker)
    upside = strategy.calculate_upside(strategy.calculate_dcf_intrinsic_value())
    AVGUPSIDES[sector][marketcap].append(upside)

# Calculate the average upside for each sector and capsize
for sector in SECTORS:
    for marketcap in MARKETCAPS:
        # Remove all 'nan' values
        upsides = [x for x in AVGUPSIDES[sector][marketcap] if str(x) != 'nan']
        # If insufficient data from S&P500 stocks, use default value
        if len(upsides) != 0:
            AVGUPSIDES[sector][marketcap] = sum(upsides)/len(upsides)
        else:
            AVGUPSIDES[sector][marketcap] = default_upsides

# %% [markdown]
# 


