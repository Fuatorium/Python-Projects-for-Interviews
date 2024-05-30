import warnings
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore", category=UserWarning, module="seaborn")
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")


from database_connection import fetch_all_users

df = fetch_all_users()

print(df.describe())

sns.set(style="whitegrid")

fig, ax = plt.subplots(constrained_layout=True)
sns.pairplot(df)
plt.show()
