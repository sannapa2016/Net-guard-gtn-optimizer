def calculate_projected_roi(patient_count, net_price, cog_per_unit, years=3):
    """
    Calculates 3-year ROI considering production costs and revenue protection.
    """
    total_revenue = patient_count * net_price * years
    total_cost = (patient_count * cog_per_unit * years) + 500000 # Admin/Scrubbing overhead
    
    roi = (total_revenue - total_cost) / total_cost
    return roi

def calculate_risk_adjusted_roi(total_patients, net_price, expected_success_rate, cogs):
    """
    Factors in the 'Outcome-Based' risk to the total ROI.
    """
    successful_patients = total_patients * expected_success_rate
    failed_patients = total_patients * (1 - expected_success_rate)
    
    # Revenue is full for success, halved for failure (assuming 50% OBR refund)
    total_revenue = (successful_patients * net_price) + (failed_patients * (net_price * 0.5))
    total_costs = (total_patients * cogs) + 100000 # Operational overhead
    
    return (total_revenue - total_costs) / total_costs
