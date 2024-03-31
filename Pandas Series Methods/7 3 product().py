# Get product of Series values
import pandas as pd
list = [43,728,355,121,45,642,522]
numbers = pd.Series(list)
print(numbers.product())