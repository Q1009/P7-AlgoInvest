from utils import measure_execution_time
from utils import measure_memory_usage

actions = [("action 1", 2, 10), ("action 2", 3, 20), ("action 3", 4, 30), ("action 4", 5, 40), ("action 5", 6, 50)]


@measure_memory_usage
# @measure_execution_time
def find_best_combination(actions, budget):
    """
    Solves the knapsack problem to find the best combination of actions.

    :param actions: A list of Action objects.
    :param budget: The maximum budget.
    :return: The maximum benefit and the list of selected actions.
    """
    items = []
    for action in actions:
        print(action)
        item = (action[0], action[1], action[2])
        items.append(item)
    n = len(items)
    # Create a 2D DP array to store the maximum value at each n and weight
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    print("DP Table:")
    for row in dp:
        print(row)

    # Build the DP table
    for i in range(1, n + 1):
        name, cost, benefit = items[i - 1]
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + benefit)
            else:
                dp[i][w] = dp[i - 1][w]

    print("DP Table:")
    for row in dp:
        print(row)

    # Backtrack to find the items included in the optimal solution
    w = budget
    total_cost = 0
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]
            total_cost += items[i - 1][1]

    selected_items.reverse()
    return dp[n][budget], total_cost, selected_items

if __name__ == "__main__":

    max_value, total_cost, best_combo =find_best_combination(actions, 10)
    print (f"Maximum benefit: {max_value}")
    print(f"Total cost: {total_cost}")
    print("Best combination of actions:")
    for item in best_combo:
        print(item)


    """
    Faire varier le budget pour voir l'impact sur les performances.
    Faire varier le nombre d'actions pour voir l'impact sur les performances.
    Finir la partie code
    S+1 finir la partie diapo + démarrage P6

    """