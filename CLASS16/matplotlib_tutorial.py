#%%
#testing

participants = [
    ("Mike", 100),
    ("Lauren", 200),
    ("Danger Rat", 300),
    ("TBD", 50)
]

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(participants)

# %%

df.columns = ["Participant", "Score"]
plt.figure(figsize=(8, 6))
plt.bar(df["Participant"], df["Score"])#,color='#7bf244')


plt.title("Participants Scores")
plt.ylabel("Number")
# plt.xticks(df["Participant"])
# plt.grid(which='major',axis='y')
# plt.xticks(rotation=30)
plt.style.use("seaborn-bright")

# %%

# https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#1.-Scatter-plot
