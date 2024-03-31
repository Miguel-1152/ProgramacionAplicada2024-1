# Accessing Pandas Series values by Using Labels
import pandas as pd
c = ( ["Spark","PySpark","Hadoop","Python","pandas","Oracle"] )
courses = pd.Series(c, index= ["subject0","subject1","subject2","subject3","subject4","subject5"] )
print(courses)