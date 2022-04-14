from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Brand import Brand
from ..Cart import Cart
from ..AboutPage import AboutPage

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Home())

  def sidebar_brand_link_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Brand())

  def sidebar_home_link_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def topbar_cart_link_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(Cart())

  def sidebar_about_link_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(AboutPage())




