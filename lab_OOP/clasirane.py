
import pandas as pd
pd.option_context('display.max_rows', None , 'display.max_columns', None)
from matury import final_mapper
from matury import dictionary_2025

new_mapper = {}
values_list2 =[]

for (k1, v1), (k2, v2) in zip(dictionary_2025.items(), sorted(final_mapper.items(), key=lambda x: x[1], reverse=True)):
    if v2 >= v1:
        values_list2.append(v2)
print()
series = pd.Series(dictionary_2025)
pr = pd.DataFrame(series)
with pd.option_context('display.max_rows', None , 'display.max_columns', None):
    print(series)




