from ._anvil_designer import ChampayneLoginTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Champayne_payment import Champayne_payment

class ChampayneLogin(ChampayneLoginTemplate):
  def __init__(self, address, value, order_list, **properties):
    self.init_components(**properties)
    
    self.address = address
    self.value = value
    self.order_list = order_list
   

  def login_button_click(self, **event_args):
    if self.email_field.text == '': 
      alert('Please enter a random email, e.g. test@gamil.com')
      return
    elif self.password_field.text == '': 
      alert('Please enter a random password, e.g. 123456')
      return
    self.go_to_pay()
  
  def go_to_pay(self):
    open_form(Champayne_payment(user=self.email_field.text, shipping_address=self.address, 
                                value = self.value, detail = self.order_list))

