from ._anvil_designer import itemCardTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ItemPurchase import ItemPurchase

class itemCard(itemCardTemplate):
  def __init__(self, id, name, image, price, order_button, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.item_name.text = name
    self.item_image.source = image
    self.item_price.text = price
    self.item_id = id
    self.order_button = order_button
    
  def item_buy_button_click(self, **event_args):
    self.order_button(self.item_id)

