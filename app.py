from flask import Flask, jsonify, redirect, render_template, request, session
from forex_python.converter import CurrencyRates
from secret import secret_key
from logic import Logic


app = Flask(__name__)
app.secret_key = secret_key()

c = CurrencyRates()

logic = Logic




@app.route('/')
# This is the main route. In this route we set the sessions that will later allow us to determine whether to show a flash message or not
def application():
    if session.get('from_flash') is None:
        session['from_flash'] = False

    if session.get('to_flash') is None:
        session['to_flash'] = False

    if session.get('amount_flash') is None:
        session['amount_flash'] = False

    return render_template('form.html', req_from = logic.req_from, req_to = logic.req_to, req_amt = logic.req_amt)

@app.route('/checkform', methods = ['POST', 'GET'])
# When the user submits the form it is submitted via a POST route. Then the information is checked to see if 
# all the forms had valid data submissions. Based on whether that validation passes or fails the user will then be 
# redirected. If they passed the user will get redirected to the '/answers' route. If the validation fails they will be redirected to 
# the '/' route where a message will be flashed to them showing what information was incorrect. 
def checkform():
   logic.add_form_data(request.form['converting-from'], request.form['converting-to'], request.form['amount'])

   logic.check_form_session()

   if logic.req_from[0] in logic.codes and logic.req_to[0] in logic.codes and logic.req_amt[0].isdigit():
        return redirect('/answer')
   else:
        return redirect('/')

@app.route('/answer')
# Upon succesfull validation the user will be sent to the '/answers' route which will calculate and show the answer. 
def answer():
    converted_amt = c.convert(logic.req_from[0], logic.req_to[0], float(logic.req_amt[0]))
    # The code bellow formats the float number to only have 2 decimal spaces
    formated_amt = "{:.2f}".format(converted_amt)
    return render_template('answer.html', amt = formated_amt, req_from = logic.req_from[0], req_to = logic.req_to[0])

