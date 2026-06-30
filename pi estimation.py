
import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()
n_trials = [10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000]
print("Estimating the value of π using Monte Carlo method")
def estimate_pi(num_samples):
    x_coord = 0
    y_coord = 0
    in_Circle = 0
    x_coords = (rng.random(num_samples)) * 2 - 1
    y_coords = (rng.random(num_samples)) * 2 - 1
    origin_dist = (x_coords**2 + y_coords**2)**0.5
    mask =origin_dist**2 <= 1 
    in_Circle = np.sum(mask)
    pi_value = (in_Circle / num_samples)*4
    running_pi = np.cumsum(mask) / np.arange(1, num_samples + 1) * 4
    return pi_value, x_coords, y_coords, mask, running_pi

def plot_approximation(x_data, y_data, mask_data, cumulative):
    fig, axs = plt.subplots(1, 2)
    x_in = x_data[mask_data]
    y_in = y_data[mask_data]
    x_out = x_data[~mask_data]
    y_out = y_data[~mask_data]
    axs[0].scatter(x_in,y_in, color = 'red', s = 1)
    axs[0].scatter(x_out,y_out, color = 'blue', s = 1)
    axs[1].plot(cumulative)
    axs[1].axhline(np.pi, color = 'red', linestyle = '--')
    plt.show()


est_value, x_coords, y_coords, mask, cumulative = estimate_pi(10000)
print("Estimated value of π", est_value)
plot_approximation(x_coords, y_coords, mask, cumulative)