from flask import Flask, render_template

from forms import forms_bp
from auth import auth_bp
from db import database_bp
from db_utils import get_all_products

app = Flask(__name__)
app.config.from_prefixed_env()

app.register_blueprint(forms_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(database_bp)

@app.route('/')
def index():
    products = get_all_products()

    context = {
        'products': products
    }

    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
