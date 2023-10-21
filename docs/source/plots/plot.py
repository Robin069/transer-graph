import matplotlib.pyplot as plt
import seaborn as sns

statworx_palette = sns.color_palette(["#0000FF", "#000000", "#FE0D6C"], as_cmap=True)
sns.set_palette(statworx_palette)

df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")
plt.show()
