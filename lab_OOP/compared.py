
import pandas as pd

from matury import final_mapper
from matury import dictionary_2025
import numpy as np

data_work = {}
data_25 = {}
for (k1, v1), (k2, v2) in zip(final_mapper.items(), dictionary_2025.items()):
    element_1 , element_2 = k1.split(), k2.split()
    data_work[(", ".join(element_1))] = v1
    data_25[(", ".join(element_2))] = v2
    simbol = k1[0:4]
    simbol.replace(",", "0")
    s = (int(simbol))
    for (k1, v1), (k2, v2) in zip(dictionary_2025.items(), final_mapper.items()):
        if  k1.startswith(str(simbol)) == k2.startswith(str(simbol)):
           print(f"{k2:<110}: {v2:7.2f} : {v1:7.2f}")
    break













