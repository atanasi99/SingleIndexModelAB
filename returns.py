import pandas as pd
import numpy as np

def log_returns(df, T):
    """
    Function to compute log returns for different sampling frequencies
    """
    # Assign stock price for selected ticker
    stock_price = df

    match T:
        # If conditional statement if sampling frequency is Daily
        case 'D':
            # Compute log-returns
            returns = np.diff(np.log(stock_price))
        # Normal case where sampling is annual or monthly
        case _:
            # Resample the stock price for the corresponding stock
            stock_price = stock_price.resample(T).last()
            # Compute log-returns
            returns = np.diff(np.log(stock_price))
    
    ## Assign returns of stock to DataFrame
    returns = pd.DataFrame({"Stock": returns}, index = stock_price.index[1:])

    # Return the returns of the stock
    return(returns)