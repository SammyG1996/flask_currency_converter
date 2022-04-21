from lib2to3.pytree import convert
import app
from unittest import TestCase 

class AppTestCase(TestCase): 
  def test_converter(self): 
    # This checks to see if $1 USD is equal to $1 USD when passes through converter
    self.assertEqual(app.c.convert('USD', 'USD', 1.00), 1.00)

  def test_country_codes(self): 
    # This tests to see is the USD country code is in the list of country codes
    assert "USD" in app.codes

  # class FlaskAppTestCase(TestCase): 
  #   def 

  

