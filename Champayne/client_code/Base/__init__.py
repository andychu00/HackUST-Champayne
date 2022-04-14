from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..MyTransactions import MyTransactions
from ..LoginPage import LoginPage

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.change_sign_in_text()
    self.go_to_home()

  # Edited
  def change_sign_in_text(self):
    user = anvil.server.call('get_login_email')
    if user != '': 
      self.sign_in.text = user
    else:
      self.sign_in.text = "Sign In"
      
    self.toggle_my_transactions_link()

  # Edited
  def toggle_my_transactions_link(self):
    self.my_transaction.visible = (anvil.server.call('get_login_email') != '')
  
  def my_transaction_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(MyTransactions())

  def go_to_home(self):
    self.content_panel.clear()
    self.content_panel.add_component(Home())
    
  # Added
  def go_to_login(self):
    self.content_panel.clear()
    self.content_panel.add_component(LoginPage())
    
  # Edited
  def sign_in_click(self, **event_args):
    user = anvil.server.call('get_login_email')
    if user != '':
      logout = confirm('Would you like to logout?')
      if logout:
        anvil.server.call('user_logout')
        self.go_to_home()
        self.change_sign_in_text()
    else:
      self.go_to_login()



