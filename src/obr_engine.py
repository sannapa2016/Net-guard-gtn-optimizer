import pandas as pd

def process_outcome_rebate(patient_id, current_result, target_benchmark, payment_amount, refund_percentage=0.50):
    """
    Calculates a refund if a clinical milestone (e.g., motor function score) is missed.
    """
    is_successful = current_result >= target_benchmark
    refund_due = 0
    
    if not is_successful:
        refund_due = payment_amount * refund_percentage
        
    return {
        "patient_id": patient_id,
        "status": "Success" if is_successful else "Failure",
        "refund_amount": refund_due,
        "net_realized_revenue": payment_amount - refund_due
    }
