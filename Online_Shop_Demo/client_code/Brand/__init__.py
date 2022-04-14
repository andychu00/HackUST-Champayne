from ._anvil_designer import BrandTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..itemList import itemList

class Brand(BrandTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
  
  def go_to_itemList(self, brand):
    self.content_panel.clear()
    self.content_panel.add_component(itemList(brand))

  def nike_link_click(self, **event_args):
    self.go_to_itemList('NIKE')

  def converse_link_click(self, **event_args):
    self.go_to_itemList('Converse')

  def hoka_link_click(self, **event_args):
    self.go_to_itemList('HOKA')



