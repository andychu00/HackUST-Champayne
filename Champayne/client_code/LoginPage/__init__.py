from ._anvil_designer import LoginPageTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class LoginPage(LoginPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def login_button_click(self, **event_args):
    if self.email_input.text == '': 
      alert('Please enter your user email')
      return
    elif self.password_input.text == '':
      alert('Please enter your password')
      return
    
    # Check if the email exists in fake_db, if exist => return True
    if anvil.server.call('check_exist', email = self.email_input.text):
      anvil.server.call('user_login', email = self.email_input.text)
    else:
      alert('Please purchase some item in XShop before visit this website, thanks!')
    open_form('Base')


