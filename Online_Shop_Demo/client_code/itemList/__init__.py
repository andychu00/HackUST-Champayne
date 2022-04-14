from ._anvil_designer import itemListTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..itemCard import itemCard
from ..ItemPurchase import ItemPurchase

class itemList(itemListTemplate):
  def __init__(self, brand_name, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    items = anvil.server.call('get_item_details').search(item_brand=brand_name)
    item_panel = GridPanel()
    
    for i, item in enumerate(items):
      card = itemCard(id=item['item_id'],name=item['item_name'],image=item['item_image'],price=f"HK$ {item['item_price']}"
                      ,order_button=self.go_to_item_purchase)
      item_panel.add_component(card, row=str(i//2), width_xs=6)
    
    self.content_panel.add_component(item_panel)

  def go_to_item_purchase(self, id):
    self.content_panel.clear()
    self.content_panel.add_component(ItemPurchase(id))
  
  