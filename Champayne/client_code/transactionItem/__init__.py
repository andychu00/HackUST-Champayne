from ._anvil_designer import transactionItemTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..button import button

class transactionItem(transactionItemTemplate):
  def __init__(self, store, ref, logis, track, date, price, status, ship, conadd, button, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.store_label.content = store
    self.refno_label.content = ref
    self.track_code_label.content = track
    self.logis_label.content = logis
    self.date_label.content = date
    self.price_label.content = price
    self.status_label.content = status
    self.shipping_label.content = ship
    self.conadd_label.content = conadd
    self.status = status
    self.store = store
    self.ref = ref
    self.date = date
    self.price = price
    self.conadd = conadd
    self.button.visible = status == "pending"
    # Any code you write here will run when the form opens.

  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(button(self.status, self.store, self.ref, self.date, self.price, self.conadd))

