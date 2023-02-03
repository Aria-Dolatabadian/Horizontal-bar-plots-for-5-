import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv (r'NBS1.csv')
print (df)
sns.set_theme(style="whitegrid")
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("bright")
sns.barplot(x="TNL", y="Chromosomes", data=df,
            label="TNL", color="g")
sns.set_color_codes("bright")
sns.barplot(x="CNL", y="Chromosomes", data=df,
            label="CNL", color="m")
sns.set_color_codes("bright")
sns.barplot(x="NBS", y="Chromosomes", data=df,
            label="NBS", color="y")
sns.set_color_codes("bright")
sns.barplot(x="RLP", y="Chromosomes", data=df,
            label="RLP", color="r")
sns.set_color_codes("bright")
sns.barplot(x="RLK", y="Chromosomes", data=df,
            label="RLK", color="k")
ax.legend(ncol=2, loc="best", frameon=True)
ax.set(xlim=(0, 220), ylabel="",
       xlabel="RLK, RLP, NBS, CNL and TNL distributions across the chromosomes")
sns.despine(left=True, bottom=True)
plt.show()
