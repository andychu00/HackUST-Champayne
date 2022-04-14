from ._anvil_designer import buttonTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..RequestReceived import RequestReceived

class button(buttonTemplate):
  def __init__(self, status, store, refno, date, price, conadd, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.status = status
    self.refno = refno
    self.store_label.content = store
    self.refno_label.content = refno
    self.date_label.content = date
    self.price_label.content = price
    self.conadd_label.content = conadd

    # Any code you write here will run when the form opens.
  # Edited
  def Received_click(self, **event_args):
    """This method is called when the button is clicked"""
    all_db = app_files.fake_db
    user = anvil.server.call('get_login_email')
    db = all_db["Sheet1"]
    for r in db.rows:
      if (r["user_id"] == user) and (r["reference_no"] == self.refno):
        r["status"] = 'received'
    self.content_panel.clear()
    self.content_panel.add_component(RequestReceived())
    
  # Edited
  def Refund_click(self, **event_args):
    """This method is called when the button is clicked"""
    all_db = app_files.fake_db
    user = anvil.server.call('get_login_email')
    db = all_db["Sheet1"]
    for r in db.rows:
      if (r["user_id"] == user) and (r["reference_no"] == self.refno):
        r["status"] = 'refunded'
    self.content_panel.clear()
    self.content_panel.add_component(RequestReceived())


