'''
Create a program that will keep track of items for a shopping list. The program should keep asking for new items until
nothing is entered (no input followed by enter/return key). The program should then display the full shopping list.
'''
shop_list =[]
loop = True

while loop:
    inp_str = raw_input('Enter the item to add to shopping list ')
    if inp_str != '':
        shop_list.append(inp_str)
    else:
        loop = False

print shop_list