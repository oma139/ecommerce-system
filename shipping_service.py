def ship(items):
    print("Shipping the following items:")
    for item in items:
        print(f"- {item.get_name()} (Weight: {item.get_weight()} kg)")