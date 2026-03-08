print("=== shopping cart ===")
cart = []
prices = []

while True:
    item = input("\nAdd item (or 'done' to checkout): ")
    if item.lower() == "done":
        break
    price = float(input(f"price of {item} : ₹"))
    cart.append(item)
    prices.append(price)
    print(f"✅{item} ({price}) added to cart.")
print ("\n" + "=" * 35)
print ( "🛒 YOUR CART: ")
for i in range (len(cart)):
    print(f" {i+1}. {cart[i]} = ₹{prices[i]}")
print("=" * 35)
print (f"total items: {len(cart)}")
print (f"total price: ₹ {sum(prices):.2f}")