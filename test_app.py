import app
from flask import session
from logic import Logic
from unittest import TestCase 

class AppTestCase(TestCase): 
  def test_converter(self): 
    # This checks to see if $1 USD is equal to $1 USD when passes through converter
    self.assertEqual(app.c.convert('USD', 'USD', 1.00), 1.00)

  def test_country_codes(self): 
    # This tests to see is the USD country code is in the list of country codes
    assert "USD" in Logic.codes

  def test_add_form_data(self):
    # This will test if the correct item is prepended to the arrays
    Logic.add_form_data('from', 'to', 'amount')
    self.assertEqual(Logic.req_from[0], 'from')
    self.assertEqual(Logic.req_to[0], 'to')
    self.assertEqual(Logic.req_amt[0], 'amount')

  def test_check_form_session(self): 
    # This will test to see if the session is appropriately changed when passed 
    # though the check_form_session() function.
    with app.app.test_client() as client:
      client.get('/')

      Logic.add_form_data('USf', 'CAD', '100')

      Logic.check_form_session()

      self.assertEqual(session['from_flash'], True)



class FlaskAppTestCase(TestCase): 
  def test_home_page(self):
    with app.app.test_client() as client:
        # can now make requests to flask via `client`
        resp = client.get('/')
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h1>Convert Your Currency</h1>', html)
        
  def test_redirect_to_answers_page(self): 
    with app.app.test_client() as client:

      resp = client.post('/checkform',
                           data={
                           'converting-from': 'USD', 
                           'converting-to': 'CAD', 
                           'amount': '100'
                           })

      resp.get_data(as_text=True)

      self.assertEqual(resp.status_code, 302)

  

