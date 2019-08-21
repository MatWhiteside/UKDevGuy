# Define our product class
class Product:
    # Initialise all the variables
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    # Return the total price of the product
    def get_total(self):
        return self.price * self.quantity
    

# Create some products for our supermarket
apples = Product("Apples", 0.50, 150)
bananas = Product("Bananas", 0.60, 200)
cakes = Product("Cakes", 2.00, 20)
chicken = Product("Chickens", 7.50, 10)

# Put our products into a list
product_list = [apples, bananas, cakes, chicken]

# Output all of our products
for product in product_list:
    # Note that product.price:.2f outputs the product price
    # formatted to two decimal places
    print(f"We have {product.quantity} {product.name} priced at £{product.price:.2f} each.")

# Calculate total stock price
total_price = sum([product.get_total() for product in product_list])
print(f"The total price of all stock is £{total_price:.2f}")