import pandas as pd
import numpy as np

def run_success_sensitivity(total_patients, net_price, cogs, start_rate=0.70, end_rate=0.95, step=0.05):
    """
    Simulates the impact of varying clinical success rates on ROI.
    """
    rates = np.arange(start_rate, end_rate + step, step)
    sensitivity_results = []

    for rate in rates:
        # Using the logic: ROI = (Revenue - Cost) / Cost
        # Revenue: Successful pts (100% price) + Failed pts (50% price due to OBR)
        success_rev = (total_patients * rate) * net_price
        failure_rev = (total_patients * (1 - rate)) * (net_price * 0.5)
        
        total_rev = success_rev + failure_rev
        total_costs = (total_patients * cogs) + 100000
        roi = (total_rev - total_costs) / total_costs
        
        sensitivity_results.append({
            "Success_Rate": round(rate, 2),
            "Total_Revenue": round(total_rev, 2),
            "ROI_Percent": round(roi * 100, 2)
        })

    return pd.DataFrame(sensitivity_results)
