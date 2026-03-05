
from data.emi_data import emi_database


def get_customer_data(customer_id):

    return emi_database.get(customer_id, None)