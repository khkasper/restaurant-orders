import csv


def restaurant_orders(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        with open(path_to_file, "rt") as f:
            return [line for line in csv.reader(f)]

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def restaurant_detailed_info(orders, info):
    return set(line[info] for line in orders)


def customers_orders_frequency(customer, orders):
    customer_infos = dict()
    for client, dish, _ in orders:
        if client == customer:
            customer_infos[dish] = customer_infos.get(dish, 0) + 1
    return customer_infos


def customer_detailed_info(customer, orders, info):
    return set(line[info] for line in orders if line[0] == customer)


def most_ordered_dish_per_customer(customer, orders):
    most_ordered = customers_orders_frequency(customer, orders)
    return max(most_ordered.items(), key=lambda x: x[1])[0]


def times_dish_ordered_per_customer(customer, dish, orders):
    return customers_orders_frequency(customer, orders)[dish]


def never_ordered_per_customer(customer, orders):
    dish = 1
    all_dishes = restaurant_detailed_info(orders, dish)
    ordered_dishes = customer_detailed_info(customer, orders, dish)
    return all_dishes.difference(ordered_dishes)


def days_never_visited_per_customer(customer, orders):
    weekday = 2
    all_weekdays = restaurant_detailed_info(orders, weekday)
    visited_weekdays = customer_detailed_info(customer, orders, weekday)
    return all_weekdays.difference(visited_weekdays)


def analyze_log(path_to_file):
    orders = restaurant_orders(path_to_file)

    most_ordered = most_ordered_dish_per_customer("maria", orders)
    times_ordered = times_dish_ordered_per_customer(
        "arnaldo", "hamburguer", orders
    )
    never_ordered = never_ordered_per_customer("joao", orders)
    never_visited = days_never_visited_per_customer("joao", orders)

    with open("data/mkt_campaign.txt", "w") as f:
        f.write(
            f"{most_ordered}\n"
            f"{times_ordered}\n"
            f"{never_ordered}\n"
            f"{never_visited}"
        )
