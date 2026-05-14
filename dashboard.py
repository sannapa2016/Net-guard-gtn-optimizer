from src.roi_model import calculate_projected_roi

# Data pulled from your Waterfall and Scrubber results
current_net_price = 78000 # As seen in {3A3463F7-42D0-4E4E-96B2-4B5448DD1B84}.png
eligible_patients = 120    # From your Patient-360 pipeline
cogs = 25000               # Cost of Goods Sold

roi_pct = calculate_projected_roi(eligible_patients, current_net_price, cogs)

print("--- PREDICTIVE ROI DASHBOARD ---")
print(f"Target Population: {eligible_patients} Patients")
print(f"Net Price Retention: {((current_net_price/150000)*100):.1f}%")
print(f"Projected 3-Year ROI: {roi_pct:.2%}")
print("---------------------------------")
