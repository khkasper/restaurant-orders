import csv


def restaurant_orders(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        orders = []

        with open(path_to_file, "rt") as f:
            for line in csv.reader(f):
                orders.append(line)

        return orders
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def most_ordered_dish_per_customer(customer, orders):
    most_ordered = dict()

    for client, dish, _ in orders:
        if client == customer:
            if dish in most_ordered:
                most_ordered[dish] += 1
            else:
                most_ordered[dish] = 1

    return max(most_ordered.items(), key=lambda x: x[1])[0]


def times_dish_ordered_per_customer(customer, dish, orders):
    times_ordered = dict()

    for client, dish, _ in orders:
        if client == customer:
            if dish in times_ordered:
                times_ordered[dish] += 1
            else:
                times_ordered[dish] = 1

    return times_ordered[dish]


def never_ordered_per_customer(customer, orders):
    all_dishes = set()
    for _, dish, _ in orders:
        all_dishes.add(dish)

    ordered = set()
    for client, dish, _ in orders:
        if client == customer:
            ordered.add(dish)

    return all_dishes.difference(ordered)


def days_never_visited_per_customer(customer, orders):
    all_weekdays = set()
    for _, _, weekday in orders:
        all_weekdays.add(weekday)

    visited = set()
    for client, _, day in orders:
        if client == customer:
            visited.add(day)

    return all_weekdays.difference(visited)


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
