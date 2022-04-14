import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def get_userCart():
  return anvil.server.session.get('userCart', [])

@anvil.server.callable
def add_userCart(detail):
  # detail is a dictionary
  userCart = get_userCart()
  userCart.append(detail)
  anvil.server.session['userCart'] = userCart
  
@anvil.server.callable
def remove_userCart(index):
  userCart = get_userCart()
  del userCart[index]
  anvil.server.session['userCart'] = userCart
  
@anvil.server.callable
def reset_userCart():
  anvil.server.session['userCart'] = []
