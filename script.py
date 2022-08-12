import pandas as pd
import math
import pprint

# read file
orders_data = pd.read_csv('amazon_orders.csv')

# prints columns of the file
#print(orders_data.columns)

# dates orders were placed
def orderDate():
  order_dates = orders_data['Order Date']

  # list and dictionary creation for order dates
  total_order_dates_dct = {}
  order_dates_lst = []

  # total days ordered on Amazon from 01/01/06 to current day
  for order_date in order_dates: 
    order_dates_lst.append(order_date)

  # updating values from list to dictionary 
  for date in order_dates_lst: 
    if date in total_order_dates_dct:
      total_order_dates_dct[date] += 1
    else: 
      total_order_dates_dct[date] = 1

  # using pprint for readability 
  pprint.pprint(total_order_dates_dct, width = 1, indent = 4)

  # gets the date with the most orders and the # of orders
  most_ordered = max(total_order_dates_dct.values())
  date_most_ordered = max(total_order_dates_dct, key = total_order_dates_dct.get)

  # prints date with the most orders and the # of orders on that day
  print("")
  print("The date with the most orders placed was: " + date_most_ordered + " with " + str(most_ordered) + " orders.")

# list of order ids 
def orderID(): 
  order_id = orders_data['Order ID']

  # adding all the order ids into a list
  order_id_lst = []

  for id in order_id: 
    order_id_lst.append(id)
  
  pprint.pprint(order_id_lst, width = 1, indent = 4)

# dictionary of the different payment types
def paymentInstrumentType(): 
  payment_types = orders_data['Payment Instrument Type']

  # adding all the order ids into a list
  payment_type_lst = []
  total_payment_types_dct = {}

  # adding payment types to a list after replacing the numbers in Visa and clearing whitespace
  for type in payment_types: 
    for ch in '0123456789-': 
      type = type.replace(ch, '')
    if 'and' in type: 
      new_type = re.sub(' +', ' ',type) # re.sub(pattern, repl, string, count=0, flags=0)
      payment_type_lst.append(new_type)
    else: 
      payment_type_lst.append(type.strip())
    
  
  # updating values from list to dictionary
  for type in payment_type_lst:
    if type in total_payment_types_dct: 
      total_payment_types_dct[type] += 1
    else: 
      total_payment_types_dct[type] = 1

  # printing the payment types
  print("The following are your payment types: ")
  pprint.pprint(total_payment_types_dct, width = 1, indent = 4)

# dates packages were shipped
def shipmentDate():
  shipment_dates = orders_data['Shipment Date']
  
  # list and dictionary creation for shipment dates
  total_shipment_dates_dct = {}
  shipment_dates_lst = []

  # total days ordered on Amazon from 01/01/06 to current day
  for shipment_date in shipment_dates: 
    if pd.isna(shipment_date) == False:
      shipment_dates_lst.append(shipment_date)

  # updating values from list to dictionary 
  for date in shipment_dates_lst: 
    if date in total_shipment_dates_dct:
      total_shipment_dates_dct[date] += 1
    else: 
      total_shipment_dates_dct[date] = 1

  # using pprint for readability 
  print("Shipment Dates: ")
  pprint.pprint(total_shipment_dates_dct, width = 1, indent = 4)

  most_shipped = max(total_shipment_dates_dct.values())
  date_most_shipped = max(total_shipment_dates_dct, key = total_shipment_dates_dct.get)

  print("")
  print("The date with the most orders shipped was: " + date_most_shipped + " with " + str(most_shipped) + " packages shipped.")
  
# total amount spent in Amazon from 01/01/06 to current day
def totalCharged():
  total_charged = orders_data['Total Charged']

  # changing the 'Total Charged' section into a list if the value is not nAn
  total_charged_lst = []
  for total_charge in total_charged: 
    if pd.isna(total_charge) == False:
      num = float(total_charge.replace('$','')) 
      total_charged_lst.append(num)
  # print(total_charged_lst)

  # prints total spent by user
  total_spent = sum(total_charged_lst)
  print("You spent a total of: $" + str(round(total_spent,2)))

# callling functions
# orderDate()
# orderID()
# paymentInstrumentType()
# totalCharged()