class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }
        self.orders = list()

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] == 0:
                return False
            self.inventory[ingredient] -= 1
        self.orders.append((customer, order, day))

    def get_quantities_to_buy(self):
        quantities_to_buy = dict()
        for ingredient in self.inventory:
            quantities_to_buy[ingredient] = (
                self.MINIMUM_INVENTORY[ingredient] - self.inventory[ingredient]
            )
        return quantities_to_buy
