'''
The items that a customer can order are: salad, hamburger, and water.

Write a function called item_order that takes as input a string named order. The string contains only words for the
items the customer can order separated by one space.
The function returns a string that counts the number of each item and consolidates them in the following order:
salad:[# salad] hamburger:[# hambruger] water:[# water]

If an order does not contain an item, then the count for that item is 0. Notice that each item is formatted as
[name of the item][a colon symbol][count of the item] and all item groups are separated by a space.

For example:
If order = "salad water hamburger salad hamburger" then the function returns "salad:2 hamburger:2 water:1"
If order = "hamburger water hamburger" then the function returns "salad:0 hamburger:2 water:1"
'''

def item_order(order):
    order_list = [x.lower() for x in order.split(' ') if x != ""]

    salad_ct = order_list.count('salad')
    hamburger_ct = order_list.count('hamburger')
    water_ct = order_list.count('water')

    print 'salad:%d hamburger:%d water:%d' %(salad_ct,hamburger_ct,water_ct)
    return None

item_order('hamburger water hamburger')