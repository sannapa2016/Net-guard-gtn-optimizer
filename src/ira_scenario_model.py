def apply_ira_penalty(current_price, base_price, cpi_u_rate):
    """
    Calculates the penalty rebate if price growth exceeds CPI-U.
    """
    allowed_price = base_price * (1 + cpi_u_rate)
    if current_price > allowed_price:
        penalty_per_unit = current_price - allowed_price
        return penalty_per_unit
    return 0
