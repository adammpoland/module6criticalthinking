from ShopptingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase
from datetime import datetime

shopping_cart = ShoppingCart("Adam", datetime.today().strftime('%Y-%m-%d'))

def init_item():
    item = ItemToPurchase(input("Item Name: "),int(input("Item Price: ")), int(input("Item Quantity: ")), input("Item Description: "))
    return item
def menu():
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items descriptions")
    print("o - Output shopping cart")
    print("q - Quit")

def print_menu():
    menu_character = ''
    while menu_character != 'q':
        menu()
        menu_character = input("Choose an option: ")
        if (menu_character == 'a'):
            item = init_item()
            shopping_cart.add_item(item)
        elif(menu_character == 'r'):
            shopping_cart.remove_item(input("Enter an item name to remove it"))
        elif (menu_character == 'c'):
            #shopping_cart.modify_item()
            print("To do")
        elif (menu_character == 'i'):
            shopping_cart.print_descriptions()
        elif (menu_character == 'o'):
            shopping_cart.print_total()

if __name__=="__main__":
   print_menu()