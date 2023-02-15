from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('SELECT * FROM expenses')
    expenses = c.fetchall()
    c.execute('SELECT * FROM income')
    income = c.fetchall()
    c.execute('SELECT * FROM investments')
    investments = c.fetchall()
    conn.close()
    return render_template('home.html', expenses=expenses, income=income, investments=investments)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    amount = request.form['amount']
    category = request.form['category']
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('INSERT INTO expenses (amount, category) VALUES (?, ?)', (amount, category))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/add_income', methods=['POST'])
def add_income():
    amount = request.form['amount']
    source = request.form['source']
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('INSERT INTO income (amount, source) VALUES (?, ?)', (amount, source))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/add_investment', methods=['POST'])
def add_investment():
    amount = request.form['amount']
    asset = request.form['asset']
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('INSERT INTO investments (amount, asset) VALUES (?, ?)', (amount, asset))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
