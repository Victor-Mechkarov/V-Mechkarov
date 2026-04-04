
import pandas as pd
from matury import final_mapper
from matury import dictionary_2025

fmp = sorted(final_mapper.items(), key=lambda kvp: int(kvp[0][0:4]), reverse=True)
dct = sorted(dictionary_2025.items(), key=lambda kvp: int(kvp[0][0:4]), reverse=True)

for (el1), (el2) in zip(fmp, dct):
    print(f"{el1[0]}---:---{el2[0]}")








