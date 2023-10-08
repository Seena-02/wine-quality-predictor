import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression



# Read Data

redwine_data = pd.read_csv("wine-quality/winequality-red.csv")

redwine_data.info()

# Visualize
sns.regplot(x="pH", y="density", data=redwine_data)

plt.show()