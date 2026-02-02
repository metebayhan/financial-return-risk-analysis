from utils import *

def display_as_percentage(val):
    return '{:.1f}%'.format(val * 100)

asset_a_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
asset_b_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

def get_returns(prices):
    returns = []

    for i in range(len(prices) - 1):
        returns.append(calculate_log_return(prices[i], prices[i + 1]))

    return returns

asset_a_returns = get_returns(asset_a_prices)
asset_b_returns = get_returns(asset_b_prices)

asset_a_returns_percentage = [display_as_percentage(r) for r in asset_a_returns]
asset_b_returns_percentage = [display_as_percentage(r) for r in asset_b_returns]

asset_a_annual_return = sum(asset_a_returns)
asset_b_annual_return = sum(asset_b_returns)

print("Annual return Asset A:", display_as_percentage(asset_a_annual_return))
print("Annual return Asset B:", display_as_percentage(asset_b_annual_return))

print("Variance Asset A:", calculate_variance(asset_a_returns))
print("Variance Asset B:", calculate_variance(asset_b_returns))

print("Std Dev Asset A:", display_as_percentage(calculate_stddev(asset_a_returns)))
print("Std Dev Asset B:", display_as_percentage(calculate_stddev(asset_b_returns)))

correlation = calculate_correlation(asset_a_returns, asset_b_returns)
print("Correlation:", correlation)

if calculate_stddev(asset_a_returns) > calculate_stddev(asset_b_returns):
    print("Asset A is riskier.")
else:
    print("Asset B is riskier.")
