import numpy as np
import random
import air_resistance

def generate_random_trials(num_trials, v0_range, theta_range, g, k, m):
    trials = []
    for _ in range(num_trials):
        v0 = random.uniform(*v0_range)
        theta = random.uniform(*theta_range)
        time_of_flight = 2 * v0 * np.sin(np.radians(theta)) / g
        x, y = air_resistance.trajectory_with_drag(v0, theta, 0, g, k, m, dt=0.01)
        trials.append((x, y, v0, theta))
    return trials


def trajectory_without_drag(v0, angle, h0, g, dt=0.01):
    """
    Calculate the trajectory of a projectile without air resistance.
    :param v0: Initial velocity
    :param angle: Launch angle in degrees
    :param h0: Initial height
    :param g: Acceleration due to gravity
    :param dt: Time step for simulation
    :return: Arrays of x and y coordinates
    """
    theta = np.radians(angle)
    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)
    time_of_flight = (vy0 + np.sqrt(vy0**2 + 2 * g * h0)) / g
    times = np.arange(0, time_of_flight, dt)
    x_vals = vx0 * times
    y_vals = h0 + vy0 * times - 0.5 * g * times**2

    # Filter out any negative y values that may occur after hitting the ground
    y_vals = np.maximum(y_vals, 0)

    return x_vals, y_vals

