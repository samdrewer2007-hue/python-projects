import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()

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
    #make the plot
    x_in = x_coords[mask]
    y_in = y_coords[mask]
    x_out = x_coords[~mask]
    y_out = y_coords[~mask]
    plt.scatter(x_in,y_in, color = 'red', s = 1)
    plt.scatter(x_out,y_out, color = 'blue', s = 1)
    plt.gca().set_aspect('equal', adjustable='box')

    plt.show()


    return pi_value   




print(estimate_pi(10000))
