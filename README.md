# VPBank-challenge2

# Challenge 2: Customer Journey Algorithm

This project simulates customer journeys through various actions on a platform, and calculates the interaction percentages between different layers of actions.

## Files

- `journey_analysis.py`: The main Python script containing the code for generating customer journeys, counting interactions, and calculating interaction percentages.

## Requirements

- Python 3.x

## Installation

No external libraries are required for this script as it only uses standard Python libraries.

## Usage

To run the script, simply execute it with Python:

```bash
python journey_analysis.py
```

## Code Overview

### Constants

- `NUM_JOURNEYS`: The number of customer journeys to simulate (default: 1000).
- `MAX_LAYERS`: The maximum number of actions in a customer journey (default: 10).
- `ACTIONS`: The list of possible actions in a customer journey.

### Functions

#### `generate_journey(max_layers: int) -> List[str]`

Generates a random customer journey.

- **Parameters:**
  - `max_layers`: Maximum number of actions in the journey.
  
- **Returns:**
  - A list representing the customer journey.

#### `count_layer_interactions(journeys: List[List[str]]) -> Dict[str, Dict[str, int]]`

Counts interactions between layers in customer journeys.

- **Parameters:**
  - `journeys`: List of customer journeys.
  
- **Returns:**
  - A dictionary of layer interaction counts.

#### `calculate_percentages(interactions: Dict[str, Dict[str, int]]) -> Dict[str, Dict[str, float]]`

Calculates percentage of layer interactions from counts.

- **Parameters:**
  - `interactions`: Dictionary of layer interaction counts.
  
- **Returns:**
  - A dictionary of layer interaction percentages.

#### `calculate_layer_interactions(journeys: List[List[str]]) -> Dict[str, Dict[str, float]]`

Calculates layer interaction percentages for customer journeys.

- **Parameters:**
  - `journeys`: List of customer journeys.
  
- **Returns:**
  - A dictionary of layer interaction percentages.

### Main Execution

1. Generate a list of customer journeys using `generate_journey()`.
2. Calculate layer interaction percentages using `calculate_layer_interactions()`.
3. Print the layer interaction percentages.

## Example Output

```plaintext
Layer interaction percentages:
From Sign in:
  To Pay bill: 14.00%
  To Withdraw: 18.30%
  To Top up: 14.30%
  To Transfer money: 11.20%
  To Create credit card: 14.10%
  To Check balance: 14.00%
  To Play game: 14.10%

From Pay bill:
  To Play game: 13.16%
  To Transfer money: 12.28%
  To Create credit card: 11.53%
  To End: 18.92%
  To Top up: 11.03%
  To Check balance: 12.03%
  To Pay bill: 11.28%
  To Withdraw: 9.77%

From Play game:
  To End: 17.96%
  To Withdraw: 11.08%
  To Create credit card: 11.97%
  To Transfer money: 12.48%
  To Play game: 11.46%
  To Check balance: 10.96%
  To Pay bill: 12.48%
  To Top up: 11.59%

From Withdraw:
  To Check balance: 13.16%
  To Create credit card: 11.81%
  To Pay bill: 10.58%
  To End: 18.82%
  To Withdraw: 10.70%
  To Play game: 12.79%
  To Transfer money: 11.19%
  To Top up: 10.95%

From Check balance:
  To Play game: 10.90%
  To Pay bill: 11.91%
  To Check balance: 11.15%
  To End: 18.50%
  To Withdraw: 9.51%
  To Create credit card: 11.91%
  To Transfer money: 12.29%
  To Top up: 13.81%

From Create credit card:
  To Withdraw: 15.08%
  To Pay bill: 12.30%
  To Transfer money: 12.79%
  To Top up: 8.81%
  To Create credit card: 12.67%
  To Play game: 11.94%
  To Check balance: 10.49%
  To End: 15.92%

From Transfer money:
  To Check balance: 11.56%
  To Play game: 10.38%
  To Create credit card: 14.98%
  To Transfer money: 9.86%
  To End: 19.19%
  To Pay bill: 12.09%
  To Withdraw: 11.30%
  To Top up: 10.64%

From Top up:
  To Play game: 10.47%
  To Transfer money: 10.85%
  To Withdraw: 11.89%
  To Pay bill: 12.40%
  To Top up: 12.92%
  To Check balance: 12.53%
  To End: 16.93%
  To Create credit card: 12.02%
```

## License

This project is licensed under the MIT License.

---

By following this README, users should be able to understand the purpose of the script, how to set it up, and what to expect when they run it.
