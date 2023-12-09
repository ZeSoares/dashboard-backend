from flask import jsonify
from . import customer_routes
from app.models import Customers

@customer_routes.route('/getCustomers', methods=['GET'])
def get_customers():
    customers = Customers.objects.all()
    customer_list = []
    for customer in customers:
        customer_info = {
            'username': customer.username,
            'name': customer.name,
            'address': customer.address,
            'birthdate': str(customer.birthdate),
            'email': customer.email,
            'accounts': customer.accounts,
            'tier_and_details': customer.tier_and_details
        }
        customer_list.append(customer_info)

    return jsonify(customers=customer_list)
