from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..ItemPurchase import ItemPurchase

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_hot_items()

  def load_hot_items(self):
    self.items = anvil.server.call('get_item_details').search()
    
    self.home_hot1_image.source = self.items[0]['item_image']
    self.home_hot1_text.text = f"{self.items[0]['item_name']}\nHK$ {self.items[0]['item_price']}"
    self.home_hot2_image.source = self.items[1]['item_image']
    self.home_hot2_text.text = f"{self.items[1]['item_name']}\nHK$ {self.items[1]['item_price']}"
    self.home_hot3_image.source = self.items[2]['item_image']
    self.home_hot3_text.text = f"{self.items[2]['item_name']}\nHK$ {self.items[2]['item_price']}"
    
  def go_to_item_purchase(self, id):
    self.content_panel.clear()
    self.content_panel.add_component(ItemPurchase(id))

  def home_hot1_cart_button_click(self, **event_args):
    self.go_to_item_purchase(self.items[0]['item_id'])

  def home_hot2_cart_button_click(self, **event_args):
    self.go_to_item_purchase(self.items[1]['item_id'])

  def home_hot3_cart_button_click(self, **event_args):
    self.go_to_item_purchase(self.items[2]['item_id'])





