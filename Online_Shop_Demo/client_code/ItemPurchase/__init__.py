from ._anvil_designer import ItemPurchaseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemPurchase(ItemPurchaseTemplate):
  def __init__(self, id,  **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.id = id
    self.item = anvil.server.call('get_item_details').get(item_id=id)
    self.sizeList = anvil.server.call('get_item_sizeList', itemID=id)
    
    self.item_image.source = self.item['item_image']
    self.item_name.text = self.item['item_name']
    self.item_price.text = f"HK$ {self.item['item_price']}"
    self.item_size_select.items = self.sizeList

  def item_add_button_click(self, **event_args):
    addItem = {'id': self.id,
               'size': self.item_size_select.selected_value,
               'price': self.item['item_price']}
    anvil.server.call('add_userCart', detail=addItem)
    print(anvil.server.call('get_userCart'))
    alert('Added to cart successfully!')

