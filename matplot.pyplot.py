import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

fig, ax = plt.subplots(figsize=(12,6))

sepal_lw = ax.scatter(iris['sepal_length'], iris['sepal_width'], label='Sepal')
petal_lw = ax.scatter(iris['petal_length'], iris['petal_width'], label='Petal')

plt.legend(handles=[sepal_lw, petal_lw]);