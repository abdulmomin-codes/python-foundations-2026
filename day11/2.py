#Build an InventoryItem class with attributes item_id, name, price, and quantity.
# Implement an instance method total_value() 
#returning price * quantity, and an apply_discount(percentage) method that reduces price in place.
# Instantiate 3 objects, place them in a list, and calculate the total inventory value using a loop.
class InventoryItem:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)
        
item1 = InventoryItem('I001', 'Mosquito repeller', 200, 5)
item2 = InventoryItem('I002', 'Cricket Bat', 800, 2)
item3 = InventoryItem('I003', 'Basketball', 500, 1)
items_list = [item1, item2, item3]
total = 0
for item in items_list:
    total += item.total_value()
print(total)   
print(f'Item1 total is {item1.total_value()}')
item2.apply_discount(10)
print(item2.price)