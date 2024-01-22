# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:10:34 2023

@author: Nick Katzenberger
"""
#from google.colab import files
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as sm
import statistics
from statsmodels.stats.anova import anova_lm

RedQuality = pd.DataFrame(pd.read_excel('winequality-red.xlsx'))
type(RedQuality)

variancePH = statistics.variance(RedQuality['"pH"'], RedQuality['"pH"'].mean())

print("Variance of pH: ", variancePH)
print("Variance of quality",statistics.variance(RedQuality['"quality"'], RedQuality['"quality"'].mean()))

#fig, (ax1, ax2) = plt.subplots(1, 2)

plt.plot(RedQuality['"pH"'], RedQuality['fixed acidity'],'go', markersize=2)
plt.plot([2.8,3.872],[12.256, 4],'k--') #Regression line 
plt.xlabel('pH level')
plt.ylabel("Fixed Acidity")
plt.title('pH vs Fixed Acidity')
plt.show()

"""
plt.plot(RedQuality['"pH"'], RedQuality['"chlorides"'],'bo', markersize=2)
plt.plot([3.4058, 2.87],[0,0.62],'k--') #Regression line 
plt.xlabel('pH level') #flipped axis  pH vs chlorides
plt.ylabel("Chloride Percentage")
plt.title('pH vs Chloride Percentage')   
plt.show()


plt.scatter(RedQuality['"pH"'], RedQuality['"residual sugar"'], c = 'purple', s=2)
plt.plot([3.4058, 3.281],[0,16],'k--') #Regression line 
plt.xlabel('pH level') #flipped axis pH vs residual sugar
plt.ylabel("Residual Sugar Content (g/l)")
plt.title('pH vs Sugar Content')
plt.show()
"""

plt.hist(RedQuality['"quality"'], bins = 8) #Quality Histogram
plt.xlabel('Quality')
plt.ylabel('Frequency')
plt.title("Frequency of Quality Rankings")
plt.show()

Qualities = RedQuality['"quality"'].value_counts() #pie chart creation
labels = ['5', '6', '7', '4', '8', '3']
colors = ['orange', 'yellow', 'green', 'red', 'cyan', 'brown']
explode = (0, 0, 0, 0, 0.6, 0.1)
plt.pie(Qualities, labels=labels, colors = colors, explode = explode, autopct='%.1f%%', startangle=10)
plt.xlabel(" ") #Get rid of previous axis labels
plt.ylabel(" ")
plt.title("Percentages of Quality Ratings")
plt.show()

#rename columns in order to make regression functions work
RedQuality.rename(columns = {'"pH"': 'pH','"chlorides"': 'chlorides', 'fixed acidity': 'fixed_acidity', 
                             '"residual sugar"': 'residual_sugar'}, inplace = True)
SLR = sm.ols(formula = 'fixed_acidity ~ pH', data = RedQuality).fit()
print(SLR.summary()) #Prints summary statistics for Simple Linear Regression
print(anova_lm(SLR)) #Prints ANOVA table from SLR
MLR=sm.ols(formula = 'pH ~ chlorides + residual_sugar', data = RedQuality).fit()
print(MLR.summary()) #Prints summary statistics for Multiple Linear Regression
print(anova_lm(MLR)) #Prints ANOVA table from MLR


CA = RedQuality['"citric acid"']
CA.replace([0], np.nan, inplace = True)
plt.bar( RedQuality['"quality"'], CA)
plt.title("Citric Acid v Quality")
plt.ylabel("citric acid g/mol")
plt.xlabel("quality")
plt.show()

VA = RedQuality['"volatile acidity"']
VA.replace([0], np.nan, inplace = True)
plt.bar( RedQuality['"quality"'], VA)
plt.title("Volatile Acid v Quality")
plt.ylabel("Volatile Acid mg/L")
plt.xlabel("quality")
plt.show()

PFreeSulf = RedQuality['"free sulfur dioxide"']/RedQuality['"total sulfur dioxide"']
plt.hist(PFreeSulf, bins = 5)
plt.title("Free Sulfur/Total Sulfur")
plt.xlabel("Percentage (Decimal Fomat)")
plt.ylabel("Frequency")
plt.show()

plt.bar(RedQuality['"quality"'], PFreeSulf)
plt.title("Quality vs Free sulfur/Total Sulfur")
plt.xlabel("Quality")
plt.ylabel("Free Sulfur/Total Sulfur")
plt.show()

plt.scatter(RedQuality['residual_sugar'], RedQuality['pH'],c='purple', s=2 )
plt.plot([0,16],[3.4058, 3.281],'k--') #Regression line 
plt.title("Residual Sugar vs pH")
plt.xlabel("Residual Sugar Content (g/L)")
plt.ylabel("pH")
plt.show() 

plt.plot(RedQuality['chlorides'], RedQuality['pH'],'bo', markersize=2)
plt.plot([0,0.62],[3.4058, 2.87],'k--') #Regression line 
plt.ylabel('pH level')
plt.xlabel("Chloride Percentage")
plt.title('pH vs Chloride Percentage')
plt.show()

print(RedQuality['pH'].describe())
print(RedQuality['"quality"'].describe())
print(PFreeSulf.mean())
"""
X = RedQuality[['chlorides', 'residual_sugar']] #shows both plots on 1 graph, but not very useful
Y = RedQuality['pH']
plt.plot(X, Y, 'o', markersize=2)
plt.show()"""