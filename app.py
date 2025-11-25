from flask import Flask, render_template, request, redirect, url_for
from database import init_db, add_item_db, get_all_items, search_items, delete_item
from models import Item

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    items = get_all_items()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        quantity = int(request.form['quantity'])
        code = request.form['code']

        new_item = Item(name, category, quantity, code)
        add_item_db(new_item)
        return redirect(url_for('index'))
    return render_template('add_item.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    items = []
    if request.method == 'POST':
        query = request.form['query']
        items = search_items(query)
    return render_template('search.html', items=items)

@app.route('/delete/<code>')
def delete(code):
    delete_item(code)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    
