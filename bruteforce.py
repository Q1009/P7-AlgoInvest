from itertools import combinations
import csv

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

def find_best_combination(actions, budget):
    all_combinations = []
    valid_combinations = []
    best_combination = []
    max_benefit = 0

    for r in range(1, len(actions) + 1):
        for combo in combinations(actions, r):
            combination = {}
            all_names = []
            total_cost = 0
            total_benefit = 0

            for action in combo:
                all_names.append(action.name)
                total_cost += action.cost
                total_benefit += float(action.benefit_percent.rstrip('%')) * action.cost / 100
            combination['actions'] = all_names
            combination['total_cost'] = total_cost
            combination['total_benefit'] = total_benefit
            all_combinations.append(combination)
            if total_cost <= budget:
                valid_combinations.append(combination)

    valid_combinations_by_benefit = sorted(valid_combinations, key=lambda x: x['total_benefit'], reverse=True)
    print("Top valid combinations by benefit:")
    for combo in valid_combinations_by_benefit[:5]:  # Show top 5 combinations
        print(combo)

    print(len(all_combinations))
    print(len(valid_combinations))
            # total_cost = sum(action.cost for action in combo)
            # total_benefit = sum(action.benefit for action in combo)

            # if total_cost <= budget and total_benefit > max_benefit:
            #     best_combination = combo
            #     max_benefit = total_benefit

    return None

if __name__ == "__main__":

    file_path = 'actions_list.csv'

    action_data = extract_action_data(file_path)
    actions = create_action_objects(action_data)
    find_best_combination(actions, 500)