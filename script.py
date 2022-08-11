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
  print("The date with the most orders place was: " + date_most_ordered + " with " + str(most_ordered) + " orders.")

# list of order ids 
def orderID(): 
  order_id = orders_data['Order ID']

  # adding all the order ids into a list
  order_id_lst = []

  for id in order_id: 
    order_id_lst.append(id)
  
  pprint.pprint(order_id_lst, width = 1, indent = 4)

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
# totalCharged()