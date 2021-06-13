import pandas as pd

wine_sample = {'country': {0: 'Argentina', 1: 'Argentina', 2: 'Argentina', 3: 'Argentina', 4: 'Argentina', 5: 'Australia', 6: 'Australia', 7: 'Australia', 8: 'Australia', 9: 'Canada', 10: 'Canada', 11: 'Canada', 12: 'Canada', 13: 'Canada', 14: 'France', 15: 'France', 16: 'France', 17: 'France', 18: 'France', 19: 'Spain', 20: 'Spain', 21: 'Spain', 22: 'Spain', 23: 'US', 24: 'US'}, 'points': {0: 89, 1: 88, 2: 88, 3: 87, 4: 83, 5: 92, 6: 94, 7: 91, 8: 90, 9: 91, 10: 87, 11: 86, 12: 92, 13: 90, 14: 87, 15: 88, 16: 85, 17: 92, 18: 84, 19: 92, 20: 81, 21: 88, 22: 83, 23: 91, 24: 91}, 'price': {0: 26.0, 1: 24.0, 2: 25.0, 3: 18.0, 4: 13.0, 5: 26.0, 6: 65.0, 7: 30.0, 8: 25.0, 9: 20.0, 10: 32.0, 11: 30.0, 12: 85.0, 13: 70.0, 14: 84.0, 15: 17.0, 16: 12.0, 17: 400.0, 18: 17.0, 19: 69.0, 20: 12.0, 21: 22.0, 22: 17.0, 23: 135.0, 24: 44.0}}
df = pd.DataFrame(wine_sample)

# your code here
countries_amount = ...