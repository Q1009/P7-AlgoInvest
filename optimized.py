from utils import measure_execution_time
from utils import measure_memory_usage
from math import ceil

class Action:
    def __init__(self, name, cost, benefit_percent):
        self.name = name
        self.cost = cost
        self.benefit_percent = benefit_percent

    @classmethod
    def from_csv(cls, csv_string):
        name, cost, benefit = csv_string.split(',')
        benefit_percent = benefit.rstrip('\n')
        return cls(name, float(cost), benefit_percent)
    
def extract_action_data(file_path):
    actions = []
    with open(file_path, "r") as f:
        for x in f:
            actions.append(x)
    actions.pop(0)  # Remove header
    return actions

def create_action_objects(action_data):
    actions = []
    for data in action_data:
        action = Action.from_csv(data)
        actions.append(action)
    return actions

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
        item = (int(action.cost), float(action.benefit_percent.rstrip('%')) * action.cost / 100)
        items.append(item)
    n = len(items)
    # Create a 2D DP array to store the maximum value at each n and weight
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        cost, benefit = items[i - 1]
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + benefit)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the items included in the optimal solution
    w = budget
    total_cost = 0
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append((actions[i-1].name, items[i - 1]))
            w -= items[i - 1][0]
            total_cost += items[i - 1][0]

    selected_items.reverse()
    return dp[n][budget], total_cost, selected_items

@measure_memory_usage
# @measure_execution_time
def find_best_combination_1(actions, budget):
    """
    Solves the knapsack problem to find the best combination of actions.

    :param actions: A list of Action objects.
    :param budget: The maximum budget.
    :return: The maximum benefit and the list of selected actions.
    """
    items = []
    for action in actions:
        if action.cost <= 0:
            continue
        else:
            item = (action.name, ceil(action.cost), float(action.benefit_percent) * action.cost / 100)
            items.append(item)
    n = len(items)
    print(f"Number of valid items: {n}")
    # Create a 2D DP array to store the maximum value at each n and weight
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        name, cost, benefit = items[i - 1]
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + benefit)
            else:
                dp[i][w] = dp[i - 1][w]

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

@measure_memory_usage
# @measure_execution_time
def find_best_combination_2(actions, budget):
    """
    Solves the knapsack problem to find the best combination of actions.

    :param actions: A list of Action objects.
    :param budget: The maximum budget.
    :return: The maximum benefit and the list of selected actions.
    """
    items = []
    for action in actions:
        # if action.cost <= 1:
        if (float(action.benefit_percent)/100) * action.cost <= 5:
            continue
        else:
            item = (action.name, int(action.cost * 100), float(action.benefit_percent) * action.cost)
            items.append(item)
    n = len(items)
    print(f"Number of valid items: {n}")
    # Create a 2D DP array to store the maximum value at each n and weight
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        name, cost, benefit = items[i - 1]
        for w in range(1, budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + benefit)
            else:
                dp[i][w] = dp[i - 1][w]

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

    file_path = 'dataset1.csv'

    action_data = extract_action_data(file_path)
    actions = create_action_objects(action_data)
    max_value, total_cost, best_combo = find_best_combination_2(actions, 50000)
    print (f"Maximum benefit: {max_value}")
    print(f"Total cost: {total_cost}")
    print("Best combination of actions:")
    for item in best_combo:
        print(item)
