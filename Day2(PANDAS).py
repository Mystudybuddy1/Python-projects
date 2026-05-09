# import pandas as pd

# df = pd.read_excel('workout_data.xlsx')

# # print(df.to_string())

# # print(pd.options.display.max_rows)
# pd.options.display.max_rows = 9999
# print(df)
# print(pd.options.display.max_rows)
import pandas as pd

df = pd.read_json('C:\python Day 1\PANDAS\data.json')

# print(df.to_string())
print(df.tail(5))

