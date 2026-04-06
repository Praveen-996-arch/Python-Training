
import pandas as pd
student_dict = {"student": ["Manu", "Praveen", "Isha", "Eleanor", "Sam", "Sophie"],
                "score": [56, 76, 98, 45, 67, 89]}

pandas_dict = pd.DataFrame(student_dict)
# print(pandas_dict)
pandas_new = {row.student : row.score for index,row in pandas_dict.iterrows()}
print(pandas_new)