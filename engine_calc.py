import pandas as pd
from sklearn.feature_selection import chi2
import scipy.stats as stats


df = pd.read_excel("C:projects\data\enginedata.xlsx")

df=df["V(α) [dm3]"]
to_verify=[1, 100, 360, 500, 720]

for i in to_verify:
 probabilty = stats.chi2.ppf(q=0.95, df=df[i])
 print((probabilty),end=" ")

