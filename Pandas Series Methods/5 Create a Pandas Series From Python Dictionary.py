# Create a Pandas Series From Python Dictionary
import pandas as pd
population_dict = {'India': 1366417754,
                   'China': 1397715000,
                   'USA': 328239523,
                   'England': 55977200,
                   'Russia': 143666931,
                   'Japan':126264931}
population = pd.Series(population_dict)
print(population)