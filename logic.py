from flask import session
# from flask import session

class Logic():

  def __init__(self, from_flash, to_flash, amount_flash):
    self.from_flash = from_flash
    self.to_flash = to_flash
    self.amount_flash = amount_flash


  codes = ['EUR', 'IDR', 'BGN', 'ILS', 'GBP', 
  'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 
  'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 
  'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 
  'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 
  'PLN', 'PHP', 'ZAR']

  req_from = []
  req_to = []
  req_amt = []

  def add_form_data(frm, to, amt):
    Logic.req_from.insert(0, frm)
    Logic.req_to.insert(0, to)
    Logic.req_amt.insert(0, amt)



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