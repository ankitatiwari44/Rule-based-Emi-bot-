def detect_intent(query: str):

    query = query.lower()

    # NEXT EMI DATE
    if ("next" in query and ("emi" in query or "installment" in query or "payment" in query)) \
        or "due date" in query:
        return "next_emi_date"


    # EMI AMOUNT
    if ("emi amount" in query
        or "monthly emi" in query
        or "installment amount" in query
        or "amount to be paid" in query
        or "monthly payment" in query
        or ("how much" in query and ("pay" in query or "emi" in query))):
        return "emi_amount"


    # REMAINING BALANCE
    if ("remaining balance" in query
        or "loan balance" in query
        or "outstanding" in query
        or "balance left" in query
        or "loan left" in query
        or ("loan" in query and "left" in query)):
        return "remaining_balance"


    # FORECLOSURE
    if ("foreclosure" in query
        or "close loan" in query
        or "loan closure" in query
        or "prepayment" in query
        or ("close" in query and ("loan" in query or "account" in query))
        or ("close" in query and "today" in query)):
        return "foreclosure_amount"


    # EMIs LEFT
    if ("emis left" in query
        or "remaining emis" in query
        or "installments left" in query
        or "payments left" in query
        or ("how many" in query and ("emi" in query or "installment" in query))):
        return "emis_left"


    return "unknown"