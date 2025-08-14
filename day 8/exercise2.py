class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price
        self.quantity = quantity

    def apply_discount(self, percent):
        discount = self.__price * (percent / 100)
        self.__price -= discount

    def restock(self, amount):
        self.quantity += amount

    def get_price(self):
        return self.__price

    def __add__(self, other):
        if self.product_id == other.product_id:
            return Product(self.product_id, self.name, self.__price, self.quantity + other.quantity)
        else:
            raise ValueError("Products must have the same ID to add quantities.")

    def __call__(self):
        print(f"{self.name}: ${self.__price:.2f}, Qty: {self.quantity}")


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size

    def apply_discount(self, percent):
        if percent > 20:
            percent = 20
        super().apply_discount(percent)


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight

    def apply_discount(self, percent):
        super().apply_discount(percent)
        if self.get_price() < 5:
            self._Product__price = 5
#add__ → Combines quantities of two same products.

#call__ → Allows calling the object like a function to print summary.