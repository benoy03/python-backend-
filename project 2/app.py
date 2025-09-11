from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecret"
DB = "ecommerce.db"

# ------------------------------
# Classes & Exceptions
# ------------------------------
class OutOfStockError(Exception): pass
class ProductNotFoundError(Exception): pass

class Product:
    def __init__(self, name, price, stock, id=None):
        self.id = id
        self.name = name
        self.price = price
        self._stock = stock

    def __str__(self): return f"{self.name} - ${self.price} ({self._stock} in stock)"
    @property
    def stock(self): return self._stock
    def reduce_stock(self, qty):
        if qty > self._stock:
            raise OutOfStockError(f"Only {self._stock} of {self.name} available")
        self._stock -= qty

class Book(Product):
    def __init__(self, name, price, stock, author, id=None):
        super().__init__(name, price, stock, id)
        self.author = author
    def __str__(self): return f"Book: {self.name} by {self.author} - ${self.price} ({self._stock} in stock)"

class Electronics(Product):
    def __init__(self, name, price, stock, warranty, id=None):
        super().__init__(name, price, stock, id)
        self.warranty = warranty
    def __str__(self): return f"Electronics: {self.name} - ${self.price} ({self._stock} in stock, {self.warranty}yr warranty)"

# ------------------------------
# Database Helpers
# ------------------------------
def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS products (
                 id INTEGER PRIMARY KEY, name TEXT, price REAL, stock INTEGER, type TEXT, extra TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS orders (
                 id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, total REAL, order_date TEXT)""")
    conn.commit()
    conn.close()

init_db()

def get_all_products():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    conn.close()
    result = []
    for p in products:
        if p['type'] == 'Book':
            result.append(Book(p['name'], p['price'], p['stock'], p['extra'], p['id']))
        elif p['type'] == 'Electronics':
            result.append(Electronics(p['name'], p['price'], p['stock'], int(p['extra']), p['id']))
        else:
            result.append(Product(p['name'], p['price'], p['stock'], p['id']))
    return result

def get_product_by_id(pid):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id=?", (pid,))
    p = c.fetchone()
    conn.close()
    if not p: raise ProductNotFoundError(f"Product {pid} not found")
    if p['type'] == 'Book': return Book(p['name'], p['price'], p['stock'], p['extra'], p['id'])
    elif p['type'] == 'Electronics': return Electronics(p['name'], p['price'], p['stock'], int(p['extra']), p['id'])
    return Product(p['name'], p['price'], p['stock'], p['id'])

# ------------------------------
# Routes
# ------------------------------
@app.route('/')
def index():
    products = get_all_products()
    cart_items = []
    total = 0
    if 'cart' in session:
        for pid, qty in session['cart'].items():
            p = get_product_by_id(int(pid))
            cart_items.append({'product': p, 'qty': qty, 'subtotal': p.price*qty})
            total += p.price*qty
    return render_template("index.html", products=products, cart_items=cart_items, total=total)

@app.route('/add/<int:pid>')
def add_to_cart(pid):
    if 'cart' not in session: session['cart'] = {}
    qty = int(request.args.get('qty', 1))
    session['cart'][str(pid)] = session['cart'].get(str(pid), 0) + qty
    flash("Added to cart!")
    return redirect(url_for('index'))

@app.route('/checkout')
def checkout():
    if 'cart' not in session or not session['cart']:
        flash("Cart is empty")
        return redirect(url_for('index'))

    conn = get_db()
    c = conn.cursor()
    total = 0
    for pid, qty in session['cart'].items():
        p = get_product_by_id(int(pid))
        if qty > p.stock:
            flash(f"Not enough stock for {p.name}")
            return redirect(url_for('index'))
        c.execute("UPDATE products SET stock=? WHERE id=?", (p.stock - qty, p.id))
        c.execute("INSERT INTO orders (product_id, quantity, total, order_date) VALUES (?, ?, ?, ?)",
                  (p.id, qty, p.price*qty, datetime.now().isoformat()))
        total += p.price*qty
    conn.commit()
    session['cart'] = {}
    flash(f"Checkout successful! Paid ${total}")
    return redirect(url_for('index'))

@app.route('/init')
def init_sample():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM products")
    if c.fetchone()[0] > 0:
        conn.close()
        flash("Sample products already exist")
        return redirect(url_for('index'))

    c.execute("INSERT INTO products (name, price, stock, type, extra) VALUES (?,?,?,?,?)",
              ("Python 101", 29.99, 10, "Book", "John Doe"))
    c.execute("INSERT INTO products (name, price, stock, type, extra) VALUES (?,?,?,?,?)",
              ("Smartphone", 499.99, 5, "Electronics", "2"))
    conn.commit()
    conn.close()
    flash("Sample products added")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
