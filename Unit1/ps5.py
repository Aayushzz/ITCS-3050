def calculate_tip(bill, service_quality):
    if service_quality == "poor":
        return 0.1*bill
    elif service_quality == "average":
        return 0.15*bill
    elif service_quality == "excellent":
        return 0.2*bill
    else: 
        return None
    