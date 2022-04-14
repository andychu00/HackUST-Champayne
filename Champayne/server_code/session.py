import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_login_email():
  return anvil.server.session.get('login_email', '')

@anvil.server.callable
def user_logout():
  anvil.server.session['login_email'] = ''
  
@anvil.server.callable
def check_exist(email):
  rows = list(app_files.fake_db['Sheet1'].list_rows())
  email_list = [r['user_id'] for r in rows]
  
  if email in email_list:
    return True
  else: 
    return False
  
@anvil.server.callable
def user_login(email):
  anvil.server.session['login_email'] = email