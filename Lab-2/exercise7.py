"""EXERCISE 7"""

"""Shopping Cart Processor

Create a list of dictionaries representing 4 products. Each dictionary should contain product name, price, and quantity. Use a for loop to calculate the total cost of the cart. Then write a function called apply_discount(total) that returns the final price after a 10% discount when the total is greater than or equal to 2,000; otherwise, no discount is applied."""


product_list = [
    {"name": "lip gloss", "price": 400, "quantity": 5},
    {"name": "eyeliner", "price": 250, "quantity": 3},
    {"name": "blush", "price": 300, "quantity": 4},
    {"name": "bronzer", "price": 500, "quantity": 2},
    {"name": "foundation", "price": 600, "quantity": 1},
    {"name": "mascara", "price": 350, "quantity": 2}
]

total = 0.0
for product in product_list:
     total += (product["price"] * product["quantity"])

print(f"total: {total}")

def apply_discount(total):
    if total >= 2000:
        after_discount = total - (total * 0.1)
        return after_discount
    else:
        return "no discount"
print(f"after discount : {apply_discount(total)}")