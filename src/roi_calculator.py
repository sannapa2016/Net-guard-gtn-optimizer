def calculate_3year_roi(patient_count, avg_net_price, mgmt_cost):
    """
    Predicts 3-year ROI considering patient volume and net price stability.
    """
    total_revenue = patient_count * avg_net_price
    # Assume management costs include clinical support and GTN scrubbing
    roi = (total_revenue - mgmt_cost) / mgmt_cost
    return roi * 100 # ROI as a percentage
