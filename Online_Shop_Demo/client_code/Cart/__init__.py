from ._anvil_designer import CartTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..CartRow import CartRow
from ..ChampayneLogin import ChampayneLogin

class Cart(CartTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.order_items = anvil.server.call('get_userCart')
    self.total_payment = 0
    for i, detail in enumerate(self.order_items):
      row = CartRow(id=detail['id'], size=detail['size'], row_num=i,remove_func=self.remove_row)
      self.cart_content_panel.add_component(row, width_xs=12) # Loading the cart list
      self.total_payment += detail['price']
    
    self.total_price_label.text = f"HK$ {self.total_payment}"
  
  def remove_row(self, rowNum):
    anvil.server.call('remove_userCart', index=rowNum)
    self.content_panel.clear()
    self.content_panel.add_component(Cart())   

  def alipay_button_click(self, **event_args):
    alert('Alipay is currently offline! Please use Champayne.')

  def paypal_button_click(self, **event_args):
    alert('Paypal is currently offline! Please use Champayne.')

  def champayne_button_click(self, **event_args):
    if self.shipping_address.text == '':
      alert('Please enter the shipping address.')
    else:
      open_form(ChampayneLogin(address=self.shipping_address.text, 
                               value=self.total_payment, order_list=self.order_items))



