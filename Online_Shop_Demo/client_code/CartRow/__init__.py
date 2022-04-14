from ._anvil_designer import CartRowTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class CartRow(CartRowTemplate):
  def __init__(self, id, size, row_num, remove_func, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.id = id
    self.item = anvil.server.call('get_item_details').get(item_id=id)
    self.item_image.source = self.item['item_image']
    self.item_name.text = self.item['item_name']
    self.item_size.text = size
    self.item_price.text = f"HK$ {self.item['item_price']}"
    
    self.row_num = row_num
    self.remove_func = remove_func

  def remove_button_click(self, **event_args):
    self.remove_func(self.row_num)



