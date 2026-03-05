import streamlit as st
from utils.helpers import format_currency
from chatbot.response_generator import generate_response
from data.emi_data import emi_database


st.set_page_config(page_title="EMI Repayment Assistant")

st.title(" EMI Repayment Assistant")
st.write("Ask questions about your loan EMI.")


# Customer selection
customer_id = st.selectbox(
    "Select Customer",
    list(emi_database.keys())
)

customer_data = emi_database[customer_id]

st.write("Customer:", customer_data["name"])


# Loan summary
st.info(
    f"Loan Amount: {format_currency(customer_data['loan_amount'])} | "
    f"EMI Amount: {format_currency(customer_data['emi_amount'])}"
)


# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# User input
user_query = st.chat_input("Ask about your EMI...")


if user_query:
    response = generate_response(customer_id, user_query)

    st.session_state.chat_history.append(("user", user_query))
    st.session_state.chat_history.append(("assistant", response))


# Display chat
for sender, message in st.session_state.chat_history:
    st.chat_message(sender).write(message)