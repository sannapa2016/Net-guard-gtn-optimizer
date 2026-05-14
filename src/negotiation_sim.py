def simulate_rebate_impact(current_vol, current_net_price, proposed_rebate_inc, elasticity=1.5):
    """
    Calculates if a volume increase offsets a decrease in Net Price.
    Elasticity of 1.5 assumes a 1% rebate increase yields a 1.5% volume gain.
    """
    new_net_price = current_net_price * (1 - proposed_rebate_inc)
    projected_vol_gain = current_vol * (proposed_rebate_inc * elasticity)
    new_total_vol = current_vol + projected_vol_gain
    
    current_revenue = current_vol * current_net_price
    projected_revenue = new_total_vol * new_net_price
    
    return {
        "revenue_delta": projected_revenue - current_revenue,
        "is_profitable": projected_revenue > current_revenue,
        "new_net_price": new_net_price
    }
