print("WELCOME TO SHOPPING CART")
cart = []
while True:
    item = input("Enter an item (type 'done' when finished): ")
    if item == "done":
        break
    if item != "":
        cart.append(item)
        print(item, "added to cart.")

print("\nYour Shopping Cart:")

if len(cart) == 0:
    print("Your cart is empty.")
else:
    i = 0
    while i < len(cart):
        print(cart[i])
        i = i + 1
        
print("\nTotal Items in Cart:", len(cart))

cart = tuple(cart)
print("Cart as Tuple:", cart)

print("Checkout")