from flask import session
# from flask import session

# This class contains all the Logic needed for the application
class Logic():

  # First I __init__ all the data that will be passed in
  def __init__(self, from_flash, to_flash, amount_flash):
    self.from_flash = from_flash
    self.to_flash = to_flash
    self.amount_flash = amount_flash


  # This list conatins all the country codes and is used for form validation.
  codes = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 
  'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 
  'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 
  'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 
  'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 
  'PLN', 'PHP', 'ZAR']

  # These list are initiated to be empty. They will be used in the code bellow. 
  req_from = []
  req_to = []
  req_amt = []

  # This will extract the form data from the forms and prepend them to the list.
  def add_form_data(frm, to, amt):
    Logic.req_from.insert(0, frm)
    Logic.req_to.insert(0, to)
    Logic.req_amt.insert(0, amt)


  # Now this will preform the form validation by using the the data that was prepended to the empty Lists. 
  # Based on whether they pass or fail validation the session will be set to either show the flash or not. 
  def check_form_session():
    if Logic.req_from[0] not in Logic.codes:
        session['from_flash'] = True
    else: session['from_flash'] = False

    if Logic.req_to[0] not in Logic.codes:
          session['to_flash'] = True
    else: session['to_flash'] = False
    
    if not Logic.req_amt[0].isdigit():
          session['amount_flash'] = True 
    else: session['amount_flash'] = False