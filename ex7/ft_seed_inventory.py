
def ft_seed_inventory(seed_type: str, quality: int, unit: str) -> None:
    seed_type = seed_type[:1].upper() + seed_type[1:]

    if unit == "packets":
        res = f"{seed_type} seeds: {quality} {unit} available"
    elif unit == "grams":
        res = f"{seed_type} seeds: {quality} {unit} total"
    elif unit == "area":
        res = f"{seed_type} seeds: covers {quality} square meters"
    else:
        res = "Unknown unit type"
    print(res)

# def ft_seed_inventory(seed_type: str, quality: int, unit: str) -> None:
#     messages = {
#         "packets": f"{seed_type} seeds: {quality} packets available",
#         "grams": f"{seed_type} seeds: {quality} grams total",
#         "area": f"{seed_type} seeds: covers {quality} square meters"
#     }

#     res = messages.get(unit, "Unknown unit type")
#     print(res)
