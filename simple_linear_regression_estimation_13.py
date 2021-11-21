# %%

import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels as sm
import statsmodels.formula.api as smf

df = pd.read_excel("dataset/TrainExer13.xls")


print(df.columns)
sns.lmplot(data=df, x="Year", y="Winning time men")

results = smf.ols("wtm ~ Year", data=df.rename(columns={"Winning time men": "wtm"})).fit()

print(results.summary())
