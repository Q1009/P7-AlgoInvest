from utils import measure_execution_time
from utils import measure_memory_usage
from typing import List

class Action:
    def __init__(self, name, cost, benefit_percent):
        self.name = name
        self.cost = cost
        self.benefit_percent = benefit_percent

    @classmethod
    def from_csv(cls, csv_string):
        name, cost, benefit = csv_string.split(',')
        benefit_percent = benefit.rstrip('\n')
        return cls(name, float(cost), float(benefit_percent))
    
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

# @measure_memory_usage
@measure_execution_time
def greedy_knapsack(actions: List[Action], max_weight):
    """
    Solve the knapsack problem using a greedy algorithm.

    :param actions: A list of Action objects.
    :param max_weight: The maximum weight capacity of the knapsack.
    :return: The total value and the list of selected actions.
    """
    # Sort actions by benefit_percent in descending order
    actions = sorted(actions, key=lambda x: x.benefit_percent, reverse=True)

    total_value = 0
    total_weight = 0
    selected_actions = []

    for action in actions:
        if total_weight + action.cost <= max_weight and action.cost > 0:
            selected_actions.append(action)
            total_value += action.benefit_percent * action.cost / 100
            total_weight += action.cost

    return total_value, total_weight, selected_actions

if __name__ == "__main__":

    file_path = 'dataset2.csv'
    budget = 500

    action_data = extract_action_data(file_path)
    actions = create_action_objects(action_data)
    max_value, total_cost, best_combo = greedy_knapsack(actions, budget)
    print("Best combination of actions:")
    for item in best_combo:
        print(item.name, item.cost, item.benefit_percent)
    print(f"Total cost: {round(total_cost,2)}€ out of {budget}€")
    print (f"Total return: {round(max_value,2)}€")