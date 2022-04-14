import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def get_item_details():
  return app_tables.items.client_readable()

@anvil.server.callable
def get_item_sizeList(itemID):
  sizeList = []
  itemList = app_tables.item_size.client_readable().search(item_id=itemID)
  for item in itemList:
    sizeList.append(item['item_size'])
  
  return sizeList

