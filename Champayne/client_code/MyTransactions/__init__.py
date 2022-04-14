from ._anvil_designer import MyTransactionsTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..transactionItem import transactionItem

class MyTransactions(MyTransactionsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.load_transactions()
    
  def back(self):
    self.content_panel.clear()
    self.load_transactions()
    
  # Edited
  def load_transactions(self):
    all_db = app_files.fake_db
    user = anvil.server.call('get_login_email')
    db = all_db["Sheet1"]
    
    for r in db.rows:
      if r["user_id"] == user:
        if r["status"] == "":
          t = transactionItem(store=r["store_id"], ref=r["reference_no"], logis=r["transport_co"], track=r["tracking_code"], date=r["date_of_purchase"], price=r["price"], status="pending", ship=r["shipping_status"], conadd=r["contract_address"], button=None) 
        else :
          t = transactionItem(store=r["store_id"], ref=r["reference_no"], logis=r["transport_co"], track=r["tracking_code"], date=r["date_of_purchase"], price=r["price"], status=r["status"], ship=r["shipping_status"], conadd=r["contract_address"], button=None) 
        self.content_panel.add_component(t)
