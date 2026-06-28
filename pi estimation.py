import numpy as np
rng = np.random.default_rng()

def estimate_pi(num_samples):
    x_coord = 0
    y_coord = 0
    in_Circle = 0
    for i in range(num_samples):
        x_coord = rng.uniform(-1, 1)
        y_coord = rng.uniform(-1, 1)
        if (x_coord**2 + y_coord**2) <= 1:
            in_Circle += 1
    pi_value = (in_Circle / num_samples)*4
    return pi_value   


print(estimate_pi(10000))
