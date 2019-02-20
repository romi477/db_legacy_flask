from flask import Blueprint, render_template
from models import Customer

cinemas = Blueprint('cinemas', __name__, template_folder='templates')

@cinemas.route('/customers')
def index():
    customers = Customer.query.all()
    return render_template('cinemas/index.html', customers=customers)

@cinemas.route('customers/<iso>/<name>')
def customer_detail(iso, name):
    customer = Customer.query.filter(Customer.iso==iso, Customer.name==name).first()
    return render_template('cinemas/customer_info.html', customer=customer)

