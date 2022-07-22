class TrackOrders:
    def __init__(self):
        self.orders = list()
        self.dishes = set()
        self.days = set()
        self.days_frequency = dict()
        self.customer_order_frequency = dict()
        self.customer_day_frequency = dict()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append((customer, order, day))
        self.dishes.add(order)
        self.days.add(day)
        self.days_frequency[day] = self.days_frequency.get(day, 0) + 1
        self.customer_order_frequency[
            customer
        ] = self.customer_order_frequency.get(customer, {})
        self.customer_order_frequency[customer][order] = (
            self.customer_order_frequency[customer].get(order, 0) + 1
        )
        self.customer_day_frequency[
            customer
        ] = self.customer_day_frequency.get(customer, {})
        self.customer_day_frequency[customer][day] = (
            self.customer_day_frequency[customer].get(day, 0) + 1
        )

    def get_most_ordered_dish_per_customer(self, customer):
        return max(
            self.customer_order_frequency[customer].items(), key=lambda x: x[1]
        )[0]

    def get_never_ordered_per_customer(self, customer):
        return self.dishes.difference(
            set(self.customer_order_frequency[customer].keys())
        )

    def get_days_never_visited_per_customer(self, customer):
        return self.days.difference(
            set(self.customer_day_frequency[customer].keys())
        )

    def get_busiest_day(self):
        return max(self.days_frequency.items(), key=lambda x: x[1])[0]

    def get_least_busy_day(self):
        return min(self.days_frequency.items(), key=lambda x: x[1])[0]
