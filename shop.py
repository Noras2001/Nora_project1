from classes.products import Electronics, Clothing, Books
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
one_flew_over_cuckoos_nest = Books(name="Пролетая над гнездом кукушки", price=400, author="Кен Кизи", genre="Психологический реализм")

# Создаем пользователей
customer = Customer(username="Mikhail", email="python@derkunov.ru", address="033 Russ Bur")
customer2 = Customer(username="Nora", email="nora@wonderland.org", address="0 bis, avenue Neverland")
admin = Admin(username="root", email="root@derkunov.ru", admin_level=5)

# Создаем корзину покупок и добавляем товары
cart = ShoppingCart(["customer2", "admin"])
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)
cart.add_item(one_flew_over_cuckoos_nest, 1)

# Выводим детали корзины
print(cart.get_details())
