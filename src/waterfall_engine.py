import pandas as pd

def calculate_gtn_waterfall(wac, rebates, gov_discounts, distribution_fees):
    """
    Calculates the Net Price by stripping away layers of discounts.
    """
    gross_sales = wac
    commercial_net = gross_sales - (gross_sales * rebates)
    statutory_net = commercial_net - (gross_sales * gov_discounts)
    final_net_price = statutory_net - (gross_sales * distribution_fees)
    
    gtn_perc = (final_net_price / wac) * 100
    return final_net_price, gtn_perc

def flag_margin_leakage(df, floor_percent=40):
    """
    Flags any accounts where the Net Price is below the 
    defined profitability 'floor'.
    """
    df['is_leakage'] = df['gtn_efficiency'] < floor_percent
    return df
