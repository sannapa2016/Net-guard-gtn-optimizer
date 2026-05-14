def calculate_projected_roi(patient_count, net_price, cog_per_unit, years=3):
    """
    Calculates 3-year ROI considering production costs and revenue protection.
    """
    total_revenue = patient_count * net_price * years
    total_cost = (patient_count * cog_per_unit * years) + 500000 # Admin/Scrubbing overhead
    
    roi = (total_revenue - total_cost) / total_cost
    return roi
