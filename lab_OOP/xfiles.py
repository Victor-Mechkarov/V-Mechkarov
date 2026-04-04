
import pandas as pd

X = pd.read_excel('ball.xlsx')
pd.set_option('display.max_columns', None, 'display.width', None, 'display.max_rows', None)

dfr = pd.DataFrame(X)
print(dfr)