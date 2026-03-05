from chatbot.intent_detector import detect_intent
from services.emi_service import get_customer_data


def generate_response(customer_id, query):

    intent = detect_intent(query)
    customer_data = get_customer_data(customer_id)

    if not customer_data:
        return "Customer not found."

    if intent == "next_emi_date":
        return f"Your next EMI is due on {customer_data['next_emi_date']}."

    elif intent == "emi_amount":
        return f"Your EMI amount is ₹{customer_data['emi_amount']}."

    elif intent == "remaining_balance":
        return f"Your remaining loan balance is ₹{customer_data['remaining_balance']}."

    elif intent == "foreclosure_amount":
        return f"The foreclosure amount today is ₹{customer_data['foreclosure_amount']}."

    elif intent == "emis_left":
        return f"You have {customer_data['emis_left']} EMIs remaining."

    else:
        return "Sorry, I couldn't understand your question."