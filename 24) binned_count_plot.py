import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.histplot(data, x="total_bill", binwidth=5)
plt.show()