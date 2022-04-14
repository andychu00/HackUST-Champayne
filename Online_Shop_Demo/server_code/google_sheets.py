import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from anvil.google.drive import app_files
from datetime import date
from random import randint

order_db = app_files.orders_set['Sheet1']
shipping_db = app_files.shipping_set['Sheet1']
champayne_db = app_files.champayne_db['Sheet1']
numberList = list(map(chr,range(48,58)))
charList = list(map(chr,range(97,123)))

@anvil.server.callable
def get_new_ref(last_ref):
  # last_ref = order_db.rows[-1]['reference_no']
  word = last_ref.split('_')[0]
  number = int(last_ref.split('_')[1]) + 1
  if (number/10000) >= 1: 
    word = chr(ord(word)+1)
    number = str(1) 
  else: 
    number = str(number)
  
  return f'{word}_{number}'

def get_contract_address():
  code = '0x'
  for i in range(26):
    if randint(0, 100) >= 50: code += charList[randint(0,len(charList)-1)] 
    else: code += numberList[randint(0,len(numberList)-1)]
  
  return code

@anvil.server.callable
def add_orders(user, address, order_list):
  global order_db, shipping_db
  
  currentDate = str(date.today())
  ref_no = get_new_ref(order_db.rows[-1]['reference_no'])
  init_id = int(order_db.rows[-1]['order_id'].split('_')[1]) + 1
  track_code = f"{randint(100000000,1000000000)}"
  value = 0
  for i, detail in enumerate(order_list):
    value += detail['price']
    order_db.add_row(reference_no=ref_no, order_id=f"x_{init_id+i}", order_date=currentDate,
                     product_id=detail['id'], product_size=detail['size'], product_price=detail['price'])
    
  shipping_db.add_row(reference_no=ref_no, order_date=currentDate, shipping_address=address,
                      order_price=value, shipping_status='Shipped', transport_co='UPS', tracking_code=track_code)
  
  champayne_db.add_row(user_id=user, store_name='XShop', reference_no=ref_no, price=value,
                       order_date=currentDate, shipping_status='Shipped', transport_co='UPS', 
                       tracking_code=track_code, contract_address=get_contract_address())

  order_db = app_files.orders_set['Sheet1']
  shipping_db = app_files.shipping_set['Sheet1']