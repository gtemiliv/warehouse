import psycopg2

from flask import Blueprint, request, redirect, session, abort
from db_utils import db_add_product, db_delete_product

database_bp = Blueprint('database_endpoints', __name__)


@database_bp.route('/add_product', methods=['POST'])
def add_product():
    if not session:
        return 'Unauthorized', 401
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    unit = request.form.get('unit')
    price = request.form.get('price')
    currency = request.form.get('currency')
    receipt_date = request.form.get('receipt_date')
    product_condition = request.form.get('product_condition')

    try:
        db_add_product(name, quantity, unit, price, currency, receipt_date, product_condition)
    except psycopg2.errors.DataError as exc:
        print(exc)
        return abort(400)

    return redirect('/')

@database_bp.route('/delete_product', methods=['POST'])
def delete_product():
    if not session:
        return abort(401)
    product_id = request.form['id']

    db_delete_product(product_id)

    return redirect('/')