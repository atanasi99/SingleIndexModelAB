import pandas as pd
import numpy as np

def log_returns(df, ticker, T):
    # Assign stock price for chosen stock
    stock_price = df[ticker]

    # If conditional statement if sampling frequency is Daily
    if T == 'D':
        # Compute log-returns
        returns = np.diff(np.log(stock_price))
    # Conditional statement for sampling frequencies that are Monthly and Annual
    else:
        # Resample the stock price for the corresponding stock
        stock_price = stock_price.resample(T).last()
        # Compute log-returns
        returns = np.diff(np.log(stock_price))
    
    ## Assign returns of stock to DataFrame
    returns = pd.DataFrame({ticker: returns}, index = stock_price.index[1:])

    # Return the returns of the stock
    return(returns)