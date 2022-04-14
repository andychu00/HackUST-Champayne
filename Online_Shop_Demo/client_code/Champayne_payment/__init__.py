from ._anvil_designer import Champayne_paymentTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Champayne_payment(Champayne_paymentTemplate):
  def __init__(self, user, shipping_address, value, detail, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.user = user
    self.address = shipping_address
    self.price_label.text = f"HK$ {value}"
    self.detail = detail

  def credit_card_button_click(self, **event_args):
    anvil.server.call('add_orders', user=self.user, address=self.address, order_list=self.detail)
    alert("Simulate payment successful")
    anvil.server.call('reset_userCart')
    open_form('Base')

  def payme_button_click(self, **event_args):
    anvil.server.call('add_orders', user=self.user, address=self.address, order_list=self.detail)
    alert("Simulate payment successful")
    anvil.server.call('reset_userCart')
    open_form('Base')

  def alipay_button_click(self, **event_args):
    anvil.server.call('add_orders', user=self.user, address=self.address, order_list=self.detail)
    alert("Simulate payment successful")
    anvil.server.call('reset_userCart')
    open_form('Base')

  def credit_card_button_copy_click(self, **event_args):
    anvil.server.call('add_orders', user=self.user, address=self.address, order_list=self.detail)
    alert("Simulate payment successful")
    anvil.server.call('reset_userCart')
    open_form('Base')





