import pandas as pd

# Mock Market Data: WAC = $150,000 per dose
data = {
    'market_segment': ['Commercial_PBM_A', 'Medicaid_State_B', '340B_Hospital_C'],
    'rebate_rate': [0.45, 0.23, 0.00],        # Discretionary rebates
    'statutory_rate': [0.00, 0.13, 0.55],     # Mandatory gov discounts
    'dist_fees': [0.03, 0.03, 0.03]           # Logistics
}

df = pd.DataFrame(data)

# Calculate GTN for each segment
results = df.apply(lambda row: calculate_gtn_waterfall(150000, row['rebate_rate'],
                                                     row['statutory_rate'],
                                                     row['dist_fees']), axis=1)

df[['net_price', 'gtn_efficiency']] = pd.DataFrame(results.tolist(), index=df.index)

# Flag segments that "leak" too much margin
df = flag_margin_leakage(df, floor_percent=45)

print("--- GTN Optimization Report ---")
print(df[['market_segment', 'net_price', 'gtn_efficiency', 'is_leakage']])
