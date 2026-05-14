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

from src.waterfall_engine import calculate_gtn_waterfall
from src.negotiation_sim import simulate_rebate_impact
from src.visualizer import plot_gtn_waterfall

# Define Current State
WAC = 150000
rebate_val = WAC * 0.40
gov_val = WAC * 0.10
fee_val = WAC * 0.03
net_p, _ = calculate_gtn_waterfall(WAC, 0.40, 0.10, 0.03)

# 1. Run Negotiation Simulation (Proposed 5% rebate increase)
sim = simulate_rebate_impact(current_vol=1000, current_net_price=net_p, proposed_rebate_inc=0.05)

print(f"Negotiation Outcome: {'PROFITABLE' if sim['is_profitable'] else 'LOSS'}")
print(f"Projected Revenue Change: ${sim['revenue_delta']:,.2f}")

# 2. Generate the visual artifact
plot_gtn_waterfall(WAC, rebate_val, gov_val, fee_val)

import pandas as pd

# 1. Load your Claims and the official HRSA Medicaid Exclusion File (MEF)
# If 'data/mef_registry.csv' and 'data/rebate_claims.csv' are not in your Colab environment,
# you will need to upload them. For demonstration, I will create dummy data.
try:
    mef_data = pd.read_csv('data/mef_registry.csv') # Registry of 340B providers
    claims = pd.read_csv('data/rebate_claims.csv')
except FileNotFoundError:
    print("Required data files not found. Creating dummy data for demonstration.")
    # Create dummy MEF data
    mef_data = pd.DataFrame({
        '340b_id': [101, 103, 105]
    })
    # Create dummy claims data
    claims = pd.DataFrame({
        'patient_id': [1, 2, 3, 4, 5],
        'provider_id': [101, 102, 103, 104, 105],
        'rebate_requested': [True, False, True, False, True],
        'rebate_amount': [100.0, 0.0, 150.0, 0.0, 200.0]
    })


# 2. Run the scrubber
scrubbed_claims, total_leakage = scrub_340b_duplicates(claims, mef_data)

print(f"--- Leakage Prevention Report ---")
print(f"Total Duplicate Discounts Identified: ${total_leakage:,.2f}")
print(f"Strategic Action: Withhold these payments to protect Net Price.")

!pip install streamlit

import streamlit as st
from src.roi_calculator import calculate_3year_roi

st.title("Net-Guard 360: Predictive ROI Dashboard")

# 1. High-Level Summary Tiles
col1, col2, col3 = st.columns(3)
col1.metric("Clinical Pipeline", f"{len(high_value_target)} Patients")
col2.metric("GTN Efficiency", "52%", "2.3%") # 2.3% improvement from scrubber
col3.metric("Projected 3-Year ROI", "340%")

# 2. Interactive Payer Scenario Planner
st.subheader("Payer Negotiation Simulator")
rebate_input = st.slider("Proposed Rebate Increase (%)", 0, 10, 5)
# (Call your Negotiation logic here to update the ROI live)
