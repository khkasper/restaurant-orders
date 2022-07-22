from src.analyze_log import (
    most_ordered_dish_per_customer,
    never_ordered_per_customer,
    days_never_visited_per_customer,
)


class TrackOrders:
    def __init__(self):
        self.orders = list()
        self.weekdays = dict()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))
        self.weekdays[day] = self.weekdays.get(day, 0) + 1

    def get_most_ordered_dish_per_customer(self, customer):
        return most_ordered_dish_per_customer(customer, self.orders)

    def get_never_ordered_per_customer(self, customer):
        return never_ordered_per_customer(customer, self.orders)

    def get_days_never_visited_per_customer(self, customer):
        return days_never_visited_per_customer(customer, self.orders)

    def get_busiest_day(self):
        return max(self.weekdays.items(), key=lambda x: x[1])[0]

    def get_least_busy_day(self):
        return min(self.weekdays.items(), key=lambda x: x[1])[0]
