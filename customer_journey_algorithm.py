import random
from collections import defaultdict
from typing import List, Dict

# Constants
NUM_JOURNEYS = 1000
MAX_LAYERS = 10
ACTIONS = ['Transfer money', 'Check balance', 'Top up', 'Pay bill', 'Create credit card', 'Play game', 'Withdraw']

def generate_journey(max_layers: int) -> List[str]:
    """
    Generate a random customer journey.
    
    :param max_layers: Maximum number of actions in the journey
    :return: List representing the customer journey
    """
    journey = ['Sign in']
    layer_num = random.randint(1, max_layers)
    journey.extend(random.choice(ACTIONS) for _ in range(layer_num))
    journey.append('End')
    return journey

def count_layer_interactions(journeys: List[List[str]]) -> Dict[str, Dict[str, int]]:
    """
    Count interactions between layers in customer journeys.
    
    :param journeys: List of customer journeys
    :return: Dictionary of layer interaction counts
    """
    interactions = defaultdict(lambda: defaultdict(int))
    for journey in journeys:
        for i in range(len(journey) - 1):
            interactions[journey[i]][journey[i+1]] += 1
    # print(interactions)
    return interactions

def calculate_percentages(interactions: Dict[str, Dict[str, int]]) -> Dict[str, Dict[str, float]]:
    """
    Calculate percentage of layer interactions from counts.
    
    :param interactions: Dictionary of layer interaction counts
    :return: Dictionary of layer interaction percentages
    """
    percentages = {}
    for current_layer, next_layers in interactions.items():
        total = sum(next_layers.values())
        percentages[current_layer] = {next_layer: count / total * 100 for next_layer, count in next_layers.items()}
    return percentages

def calculate_layer_interactions(journeys: List[List[str]]) -> Dict[str, Dict[str, float]]:
    """
    Calculate layer interaction percentages for customer journeys.
    
    :param journeys: List of customer journeys
    :return: Dictionary of layer interaction percentages
    """
    interactions = count_layer_interactions(journeys)
    return calculate_percentages(interactions)

if __name__ == "__main__":
    customer_journeys = [generate_journey(MAX_LAYERS) for _ in range(NUM_JOURNEYS)]

    layer_interaction_percentages = calculate_layer_interactions(customer_journeys)

    print("Layer interaction percentages:")
    for current_layer, next_layers in layer_interaction_percentages.items():
        print(f"From {current_layer}:")
        for next_layer, percentage in next_layers.items():
            print(f"  To {next_layer}: {percentage:.2f}%")
        print()