import pandas as pd

file_errors_location = 'E:\Project(s)\Python\TA\Data SNMPTN 2016\Data SNMPTN 2016 IPB by @halokampus.xlsx'
df = pd.read_excel(file_errors_location)
# print(df)

# import pandas as pd

# df = pd.read_excel("path_to_excel_file")
# df_abc = df[df["Products"] == "ABC"] # this will only contain 2,4,6 rows
print(df)