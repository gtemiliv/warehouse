import os
import psycopg2

from psycopg2.extras import DictCursor

def get_connection():
    host = os.environ.get('DB_HOST')
    user = os.environ.get('DB_USER')
    database = os.environ.get('DB_DATABASE')
    password = os.environ.get('DB_PASSWORD')

    if not all((host, user, database, password)):
        raise ValueError('Database environment variables not set')

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database,

        cursor_factory=DictCursor
    )

    return connection

def get_all_products():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM products')
    return cursor.fetchall()

def get_user_data(username):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
    user_data = cursor.fetchone()
    return user_data

def db_add_product(name, quantity, unit, price, currency, receipt_date, product_condition):
    connection = get_connection()
    cursor = connection.cursor()

    query = 'INSERT INTO products (name, quantity, unit, price, currency, receipt_date, product_condition) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    params = (name, quantity, unit, price, currency, receipt_date, product_condition)

    cursor.execute(query, params)
    connection.commit()

    return cursor.rowcount

def db_delete_product(product_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = 'DELETE FROM products WHERE id = %s'
    params = (product_id,)

    cursor.execute(query, params)
    connection.commit()

    return cursor.rowcount