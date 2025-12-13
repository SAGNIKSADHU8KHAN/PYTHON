import pandas as pd
import numpy as np

exam_data = {"name": ["Anastasia", "Dima", "Katherine", "James", "Emily", "Michelle", "Mathew", "Laura", "Kevin", "Jonas"], 
             "score": [12.5, 9, 16, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
             "attempts" : [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             "qualify" : ["yes" ,"no","yes","no","no","yes","yes","no","no","yes"]}

lebels = ["a","b","c","d","e","f","g","h","i","j"]

df = pd.DataFrame(exam_data, index=lebels)

print("Summary of the basic information of the provided dataframe")

print(df.info())
