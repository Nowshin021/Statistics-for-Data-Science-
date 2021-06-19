
import numpy as np
import pandas as pd
import stat_modules as module

df = pd.read_csv('abalone.csv')
df.columns=['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight','Rings']
df.describe

#%%
sex = df['Sex']
height = df['Height']

print("Dataset")
print(df)
print()

#%%
length = df['Length']
print("Module Count", module.countData(length))
print("Pandas Count", length.count())
print()

#%%
diameter = df['Diameter']
print("Module Describe")
module.descData(diameter)
print()
print("Pandas Describe")
print(diameter.describe())
print()

#%%
length = df['Length']
print("Module Minimum", module.calcMinimum(length))
print("Pandas Minimum", length.min())
print()
print("Module Maximum", module.calcMaximum(length))
print("Pandas Maximum", length.max())
print()

#%%
length = df['Length']
print("Module Arg Minimum", module.calcArgMinimum(length))
print("Pandas Arg Minimum", length.argmin())
print()
print("Module Arg Maximum", module.calcArgMaximum(length))
print("Pandas Arg Maximum", length.argmax())
print()

#%%
length = df['Length']
print("Module Idx Minimum", module.calcIdxMinimum(length))
print("Pandas Idx Minimum", length.idxmin())
print()
print("Module Idx Maximum", module.calcIdxMaximum(length))
print("Pandas Idx Maximum", length.idxmax())
print()

#%%
whole_weight = df['Whole weight']
print("Module Quantile", module.calcQuantile(whole_weight, .85))
print("Pandas Quantile", whole_weight.quantile(.85))
print()

#%%
shucked_weight = df['Shucked weight']
print("Module Sum", module.calcSum(shucked_weight))
print("Pandas Sum", shucked_weight.sum())
print()

#%%
viscera_weight = df['Viscera weight']
print('Module Mean', module.calcMean(viscera_weight))
print('Pandas Mean', viscera_weight.mean())
print()

#%%
shell_weight = df['Shell weight']
print('Module Median', module.calcMedian(shell_weight))
print('Pandas Median', shell_weight.median())
print()

#%%
shucked_weight = df['Shucked weight']
print("Module Mean Absolute Deviation", module.calcMad(shucked_weight))
print("Pandas Mean Absolute Deviation", shucked_weight.mad())
print()

#%%
length = df['Length']
print("Module Product", module.calcProduct(length))
print("Pandas Product", length.prod())
print()

#%%
viscera_weight = df['Viscera weight']
print("Module Variance", module.calcVariance(viscera_weight))
print("Pandas Variance", viscera_weight.var())
print()

#%%
shell_weight = df['Shell weight']
print('Module Standard Deviation', module.calcStd(shell_weight))
print('Pandas Standard Deviation', shell_weight.std())
print()

#%%
whole_weight = df['Whole weight']
print("Module Skewness", module.calcSkewness(whole_weight))
print("Pandas Skewness", whole_weight.skew())
print()

#%%
shucked_weight = df['Shucked weight']
print("Module Kurtosis", module.calcKurtosis(shucked_weight))
print("Pandas Kurtosis", shucked_weight.kurt())
print()

#%%
viscera_weight = df['Viscera weight']
print("Module Cumulative Sum")
module.printCumulative(module.calcCumSum(viscera_weight))
print("Pandas Cumulative Sum")
print(viscera_weight.cumsum())
print()

#%%
shell_weight = df['Shell weight']
print("Module Cumulative Minimum")
module.printCumulative(module.calcCumMin(shell_weight))
print("Pandas Cumulative Minimum")
print(shell_weight.cummin())
print()

#%%
whole_weight = df['Whole weight']
print("Module Cumulative Maximum")
module.printCumulative(module.calcCumMax(whole_weight))
print("Pandas Cumulative Maximum")
print(whole_weight.cummax())
print()
#%%
shucked_weight = df['Shucked weight']
print("Module Cumulative Product")
module.printCumulative(module.calcCumProd(shucked_weight))
print("Pandas Cumulative Product")
print(shucked_weight.cumprod())
print()

#%%
viscera_weight = df['Viscera weight']
print("Module Arithmetic Difference")
module.printCumulative(module.calcDiff(viscera_weight))
print("Pandas Arithmetic Difference")
print(viscera_weight.diff())
print()

#%%
shell_weight = df['Shell weight']
print("Module Percentage Change")
module.printCumulative(module.calcPctChange(shell_weight))
print("Pandas Percentage Change")
print(shell_weight.pct_change())

