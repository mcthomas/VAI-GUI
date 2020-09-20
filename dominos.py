from pizzapy import Customer, StoreLocator, Order, CreditCard

def get_menu():
    customer = Customer('Barack', 'Obama', 'barack@whitehouse.gov', '2024561111', '40 Bay St, Toronto, ON, M5J2X2')
    my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
    if(my_local_dominos):
        print(my_local_dominos)
        menu = my_local_dominos.get_menu()
        return 1, menu.search(Name='Coke'), menu.search(Name='Pizza')
    else:
        return 0, [[]], [[]]


#order = Order.begin_customer_order(customer, my_local_dominos)
#order.add_item('2LDCOKE')
#order.remove_item('2LDCOKE')
#card = CreditCard('00800123422343234', '7666', '777', '90210')
#Credits : https://github.com/techwithtim/pizzapi
