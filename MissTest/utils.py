#===============================#
#   Main Functions MissTest     #
#       Daniel Jiménez M        #
#          2023-04-02           #
#===============================#


# Libraries --------------
from scipy import stats,chi2_contingency
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 




## Functions ---------

def contingency_tables(data, col1, col2):
    observed = pd.crosstab(data[col1].isna(), data[col2].isna())
    _, _, _, expected = chi2_contingency(observed)
    expected = pd.DataFrame(expected, columns=observed.columns, index=observed.index)
    return observed, expected

def plot_heatmap(observed, expected, title):
    diff = observed - expected
    plt.figure(figsize=(8, 6))
    sns.heatmap(diff, annot=True, cmap='coolwarm', fmt='.2f', cbar=False)
    plt.xlabel("Column 2")
    plt.ylabel("Column 1")
    plt.title(title)
    plt.show()