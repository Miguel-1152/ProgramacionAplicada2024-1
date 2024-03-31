
# Get array from Series using array attribute
import pandas as pd
pd.Series( ["Spark","PySpark","Hadoop","Python","pandas","Oracle"] )
courses = pd.Series( ["Spark","PySpark","Hadoop","Python","pandas","Oracle"] )
print(courses.array)