import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 14


class Experiment:
    def __init__(self, mu, std, n_trials):
        self.mu = mu
        self.std = std
        self.n_trials = n_trials
        
    def run(self, seed):
        np.random.seed(seed)
        
        s = 0
        count = 0
        history = []
        for i in range(self.n_trials):
            x = np.random.normal(self.mu, self.std)

            s = s + x
            count = count + 1

            history.append(s / count)
            
        self.history = history
    
    def visualize(self):
        plt.figure(figsize=(6, 4))
        plt.plot(self.history, 'k-')
        plt.hlines(self.mu, xmin=0, xmax=self.n_trials, linestyle='dashed', color='red')
        plt.grid()
        plt.show()