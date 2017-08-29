user_name = input("What's your name?")
user_delivery = input("Would you like it delivered?")
delivery_charge = 3
customer_order = []
customer_price = []

if user_delivery == "yes":
  user_address = input("What is your address?")
  user_number = input("What is your phone number?")
  customer_price.append(delivery_charge)
else:
  del customer_price[:]

while True:
  pizza_menu_regular = ["Ham & Cheese", "Hawaiian", "Meatlovers", "Pepperoni", "Vegetarian", "Cheesy"]
  pizza_menu_gourmet = ["Chicken & Cranberry", "BBQ Chicken & Bacon", "Butter Chicken Pizza", "Seafood Deluxe", "Chicken Satay Pizza", "Smoked Salmon Pizza"]
  regular_pizza = 8.50
  gourmet_pizza = 13.50
  user_input = input("""What would you like to order?
 Regular Pizzas
 1) Ham & Cheese - $8.50
 2) Hawaiian - $8.50
 3) Meatlovers - $8.50
 4) Pepperoni - $8.50
 5) Vegetarian - $8.50
 6) Cheesy - $8.50
 Gourmet Pizzas
 7) Chicken & Cranberry - $13.50
 8) BBQ Chicken & Bacon - $13.50
 9) Butter Chicken Pizza - $13.50
 10) Seafood Delux - $13.50
 11) Chicken Satay Pizza - $13.50
 12) Smoked Salmon Pizza - $13.50
 type 'end' when finished""")
  if user_input == "1":
    customer_order.append(pizza_menu_regular[0])
    customer_price.append(regular_pizza)
  if user_input == "2":
    customer_order.append(pizza_menu_regular[1])
    customer_price.append(regular_pizza)
  if user_input == "3":
    customer_order.append(pizza_menu_regular[2])
    customer_price.append(regular_pizza)
  if user_input == "4":
    customer_order.append(pizza_menu_regular[3])
    customer_price.append(regular_pizza)
  if user_input == "5":
    customer_order.append(pizza_menu_regular[4])
    customer_price.append(regular_pizza)
  if user_input == "6":
    customer_order.append(pizza_menu_regular[5])
    customer_price.append(regular_pizza)
  if user_input == "7":
    customer_order.append(pizza_menu_gourmet[0])
    customer_price.append(gourmet_pizza)
  if user_input == "8":
    customer_order.append(pizza_menu_gourmet[1])
    customer_price.append(gourmet_pizza)
  if user_input == "9":
    customer_order.append(pizza_menu_gourmet[2])
    customer_price.append(gourmet_pizza)
  if user_input == "10":
    customer_order.append(pizza_menu_gourmet[3])
    customer_price.append(gourmet_pizza)
  if user_input == "11":
    customer_order.append(pizza_menu_gourmet[4])
    customer_price.append(gourmet_pizza)
  if user_input == "12":
    customer_order.append(pizza_menu_gourmet[5])
    customer_price.append(gourmet_pizza)
  if user_input == "end":
    break
  else:
    print("Please choose one of the available pizzas")

if user_delivery == "yes":
  print(user_name)
  print("Delivery")
  print(user_address)
  print(user_number)
  print(customer_order)
  print("Total Price: ${:.2f}".format(sum(customer_price)))
 
if user_delivery == "no":
  print(user_name)
  print("Pick Up")
  print(customer_order)
  print("Total Price: ${:.2f)".format(sum(customer_price)))
