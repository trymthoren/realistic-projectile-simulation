import numpy as np
import air_resistance

def loop_over_angles(v0, g, angle_range, k, m):
    results = []
    for theta in angle_range:
        time_of_flight = 2 * v0 * np.sin(np.radians(theta)) / g
        x, y = air_resistance.trajectory_with_drag(v0, theta, 0, g, k, m, dt=0.01)
        distance = x[-1]
        results.append((theta, distance))
    return results

