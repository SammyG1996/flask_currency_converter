from flask import Flask, jsonify, redirect, render_template, request, session
from forex_python.converter import CurrencyRates
from secret import secret_key


app = Flask(__name__)
app.secret_key = secret_key()

c = CurrencyRates()

req_from = []
req_to = []
req_amt = []

codes = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 
'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 
'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 
'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 
'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 
'PLN', 'PHP', 'ZAR']

@app.route('/')
def application():
    if session.get('from_flash') is None:
        session['from_flash'] = False

    if session.get('to_flash') is None:
        session['to_flash'] = False

    if session.get('amount_flash') is None:
        session['amount_flash'] = False

    return render_template('form.html', req_from = req_from, req_to = req_to, req_amt = req_amt)

@app.route('/checkform', methods = ['POST', 'GET'])
def checkform():
   req_from.insert(0, request.form['converting-from'])
   req_to.insert(0, request.form['converting-to'])
   req_amt.insert(0, request.form['amount'])

   if req_from[0] not in codes:
       session['from_flash'] = True
   else: session['from_flash'] = False

   if req_to[0] not in codes:
        session['to_flash'] = True
   else: session['to_flash'] = False

   if not req_amt[0].isdigit():
        session['amount_flash'] = True 
   else: session['amount_flash'] = False

   if req_from[0] in codes and req_to[0] in codes and req_amt[0].isdigit():
        return redirect('/answer')
   else:
        return redirect('/')

@app.route('/answer')
def answer():
    converted_amt = c.convert(req_from[0], req_to[0], float(req_amt[0]))
    # The code bellow formats the float number to only have 2 decimal spaces
    formated_amt = "{:.2f}".format(converted_amt)
    return render_template('answer.html', amt = formated_amt, req_from = req_from[0], req_to = req_to[0])

