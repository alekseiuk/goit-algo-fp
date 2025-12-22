def greedy_algorithm(items, budget):

    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    selected_items = []
    total_cost = 0
    total_calories = 0

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            selected_items.append(name)
            total_cost += data["cost"]
            total_calories += data["calories"]

    return selected_items, total_cost, total_calories


def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(item_names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - cost] + calories
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = item_names[i - 1]
            selected_items.append(name)
            w -= items[name]["cost"]

    total_calories = dp[n][budget]
    total_cost = sum(items[item]["cost"] for item in selected_items)

    return selected_items, total_cost, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Greedy algorithm:")
print(f"Items: {greedy_result[0]}, Total_cost: {greedy_result[1]}, Total_calories: {greedy_result[2]}")

print("Dynamic programming:")
print(f"Items: {dp_result[0]}, Total_cost: {dp_result[1]}, Total_calories: {dp_result[2]}")