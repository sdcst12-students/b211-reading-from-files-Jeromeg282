"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

import pandas as pd
data = pd.read_csv('task5.csv')

def stocksearch():
    symbol = input("Enter stock symbol: ")
    filter = data[data['Symbol'].str.contains(f"^{symbol}", case=False, regex=True)]

    if filter.empty:
        print("No matches")
    elif len(filter) > 1:
        print(f"There are {len(filter)} stocks with that symbol")
    else:
        print(filter)

stocksearch()

