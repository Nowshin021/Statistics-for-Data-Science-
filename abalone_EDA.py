#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
df = pd.read_csv('abalone.csv')

df.columns=['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight','Rings']
#%%
#Skewness and kurtosis
fig, axes = plt.subplots(1, 3, figsize=(20,6))
sns.set_style("darkgrid")
fig.suptitle('Highest and lowest skewness and kurtosis of the dataset : ',fontsize=12)

##Skewness of Height : 
height_skew=df['Height'].skew()
height_skew="{0:.3f}".format(height_skew)
result2="right skewed "+"("+ str(height_skew) +")"


#kurtosis of height :

height_kurt=df['Height'].kurt()
height_kurt = "{0:.3f}".format(height_kurt)

result2_kurt = "leptokurtic "+ "("+ str(height_kurt) +")"

ax1=sns.histplot(df['Height'], ax=axes[1], bins=80, kde=True, color='g')

ax1.set(title="Distribution of height")
ax1.set_ylabel("Frequency", size=12)
#xy==x and y co-ordinates of the arrow
ax1.annotate(result2+"\n"+result2_kurt, xy=(.3, 70),color = 'g',  xycoords='data',
            xytext=(0.2, .8), textcoords='axes fraction',
            fontsize = 14, arrowprops = dict(arrowstyle = '->',color='black',
             connectionstyle = "arc3, rad = -0.3")
            )



length_skew=df['Length'].skew()
length_skew="{0:.3f}".format(length_skew)
result1="left skewed "+"(" +str(length_skew)+")"

ax2=sns.histplot(df['Length'], ax=axes[0], bins=80, kde=True,color='b')
ax2.set(title="Distribution of Length")
ax2.set_ylabel("Frequency", size=12)
#xy==x and y co-ordinates of the arrow
ax2.annotate(result1, xy=(.3, 70),color = 'b',  xycoords='data',
            xytext=(0.1, .8), textcoords='axes fraction',
            fontsize = 14, arrowprops = dict(arrowstyle = '->',color='black',
             connectionstyle = "arc3, rad = 0.3")
            )


#lowest kurtosis:
diameter_kurt=df['Diameter'].kurt()
diameter_kurt = "{0:.3f}".format(diameter_kurt)

result3_kurt = "platykurtic "+ "("+ str(diameter_kurt) +")"

ax3=sns.histplot(df['Diameter'], ax=axes[2], bins=50, kde=True, color='#cc0000')
ax3.set(title="Distribution of Diameter")
ax3.set_ylabel("Frequency", size=12)
#xy==x and y co-ordinates of the arrow
ax3.annotate(result3_kurt, xy=(.2, 50),color = '#cc0000',  xycoords='data',
            xytext=(0.1, .8), textcoords='axes fraction',
            fontsize = 14, arrowprops = dict(arrowstyle = '->',color='black',
             connectionstyle = "arc3, rad = 0.3")
            )
plt.savefig("distribution.png",dpi=72)
plt.show()

print(df['Length'].mean())

#%%
#gridsize: the number of hexagons in the x-direction and the y-direction
#output analysis based on length and diameter HExbin plots

fig, axes = plt.subplots(1 ,2, figsize=(16,8))
fig.suptitle('Hexbin plots to show ther relationship  of Rings(age) with respect to Diameter and Length the dataset : ',fontsize=12)
ax=axes[0]
ax.hexbin(df["Length"], df["Rings"], gridsize=25,cmap=plt.cm.Greens_r)
ax.set(xlabel='Length', ylabel='Number of rings')
ax.set_title("Hexbin plot of Length vs Rings")


ax=axes[1]
ax.hexbin(df["Diameter"], df["Rings"], gridsize=25,cmap=plt.cm.Blues_r)
ax.set(xlabel='Diameter', ylabel='Number of rings')
ax.set_title("Hexbin plot of Diameter vs Rings")
plt.savefig("hexbins.png",dpi=72)
plt.show()

#%%
#correlation max and min
plt.figure(figsize=(10, 10))
plt.subplot(2,2,1)
sns.scatterplot(x=df['Shucked weight'], y=df['Rings'])
plt.title("Minimum Correlation")

plt.subplot(2,2,2)
sns.scatterplot(x=df['Length'], y=df['Diameter'])
plt.title("Maximum Correlation")

plt.savefig("correlation.png",dpi=72)
plt.show()

#%%
#output analysis based on gender
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
#KDE plot
sns.set(style="darkgrid")

m = df[['Sex', 'Rings']].query('Sex == "M"')
f = df[['Sex', 'Rings']].query('Sex == "F"')
i = df[['Sex', 'Rings']].query('Sex == "I"')

# plotting both distibutions on the same figure
fig = sns.kdeplot(m['Rings'], label="Male", color="r")
fig = sns.kdeplot(f['Rings'], label="Female", color="b")
fig = sns.kdeplot(i['Rings'], label="Infant", color="g")
plt.legend(loc="upper right")
plt.xlabel("Rings")

plt.savefig("density.png",dpi=72)
plt.show()




#%%
