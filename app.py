from flask import Flask, render_template, request, redirect

app = Flask(__name__)

account_balance = 3000

@app.route('/')
def index():
    return render_template('index.html', balance=account_balance)

@app.route('/deposit', methods=['POST'] )
def deposit():
    global account_balance
    amount = float(request.form['amount'])
    account_balance +=amount
    return redirect('/')
