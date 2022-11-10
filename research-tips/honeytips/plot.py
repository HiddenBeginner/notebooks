import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 14


def lineplot(data):
    plt.figure(figsize=(6, 4))
    plt.hlines(10, xmin=0, xmax=25, linestyle='dashed', color='red')
    sns.lineplot(x='step', y='avg', data=data, color='black')
    plt.grid()
    plt.show()
