import csv
from src.track_orders import TrackOrders


def restaurant_orders(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: {path_to_file}")

    try:
        with open(path_to_file, "rt") as f:
            return [line for line in csv.reader(f)]

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: {path_to_file}")


def analyze_log(path_to_file):
    track_orders = TrackOrders()
    orders = restaurant_orders(path_to_file)
    for client, dish, day in orders:
        track_orders.add_new_order(client, dish, day)

    most_ordered = track_orders.get_most_ordered_dish_per_customer("maria")
    times_ordered = track_orders.customer_order_frequency["arnaldo"][
        "hamburguer"
    ]
    never_ordered = track_orders.get_never_ordered_per_customer("joao")
    never_visited = track_orders.get_days_never_visited_per_customer("joao")

    with open("data/mkt_campaign.txt", "w") as f:
        f.write(
            f"{most_ordered}\n"
            f"{times_ordered}\n"
            f"{never_ordered}\n"
            f"{never_visited}"
        )
