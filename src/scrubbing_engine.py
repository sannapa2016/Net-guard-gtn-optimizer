import pandas as pd

def scrub_340b_duplicates(claims_df, m_exclusion_file):
    """
    Identifies 'Duplicate Discounts' by matching claims against the 
    Medicaid Exclusion File (MEF) and 340B IDs.
    """
    # Flag 1: Match Pharmacy/Provider ID against the 340B Registry (MEF)
    claims_df['is_340b_entity'] = claims_df['provider_id'].isin(m_exclusion_file['340b_id'])
    
    # Flag 2: Identify claims where a Payer rebate is requested on a 340b unit
    # Law prohibits Medicaid rebates on 340B-purchased drugs
    claims_df['is_duplicate'] = (claims_df['is_340b_entity'] == True) & (claims_df['rebate_requested'] == True)
    
    # Calculate total 'Leakage' (the money you shouldn't have to pay)
    leakage_amount = claims_df[claims_df['is_duplicate']]['rebate_amount'].sum()
    
    return claims_df, leakage_amount
