import numpy as np

def calculate_drag_constant(diameter_cm, mass, rho=1.225, C_d=0.47):
    radius_m = (diameter_cm / 100) / 2
    A = np.pi * radius_m**2
    return 0.5 * C_d * rho * A
    
    
    
    
def drag_force(v, k):
    """
    Calculate the drag force.
    :param v: Velocity of the projectile (vector)
    :param k: Drag constant
    :return: Drag force (vector)
    """
    return -k * v * np.linalg.norm(v)

def acceleration(state, g, k, m):
    """
    Calculate the acceleration of the projectile considering drag.
    :param state: Current state [vx, vy]
    :param g: Acceleration due to gravity
    :param k: Drag constant
    :param m: Mass of the projectile
    :return: Acceleration (vector)
    """
    vx, vy = state
    v = np.array([vx, vy])
    gravity = np.array([0, -g])
    drag = drag_force(v, k) / m
    return gravity + drag

def runge_kutta_step(state, dt, g, k, m):
    """
    Perform a single step of the 4th-order Runge-Kutta method.
    :param state: Current state [x, y, vx, vy]
    :param dt: Time step
    :param g: Acceleration due to gravity
    :param k: Drag constant
    :param m: Mass of the projectile
    :return: Updated state
    """
    x, y, vx, vy = state

    # k1
    ax1, ay1 = acceleration([vx, vy], g, k, m)
    k1vx = ax1 * dt
    k1vy = ay1 * dt
    k1x = vx * dt
    k1y = vy * dt

    # k2
    ax2, ay2 = acceleration([vx + k1vx / 2, vy + k1vy / 2], g, k, m)
    k2vx = ax2 * dt
    k2vy = ay2 * dt
    k2x = (vx + k1vx / 2) * dt
    k2y = (vy + k1vy / 2) * dt

    # k3
    ax3, ay3 = acceleration([vx + k2vx / 2, vy + k2vy / 2], g, k, m)
    k3vx = ax3 * dt
    k3vy = ay3 * dt
    k3x = (vx + k2vx / 2) * dt
    k3y = (vy + k2vy / 2) * dt

    # k4
    ax4, ay4 = acceleration([vx + k3vx, vy + k3vy], g, k, m)
    k4vx = ax4 * dt
    k4vy = ay4 * dt
    k4x = (vx + k3vx) * dt
    k4y = (vy + k3vy) * dt

    # Combine
    vx_new = vx + (k1vx + 2*k2vx + 2*k3vx + k4vx) / 6
    vy_new = vy + (k1vy + 2*k2vy + 2*k3vy + k4vy) / 6
    x_new = x + (k1x + 2*k2x + 2*k3x + k4x) / 6
    y_new = y + (k1y + 2*k2y + 2*k3y + k4y) / 6

    return [x_new, y_new, vx_new, vy_new]
    
    
    
def trajectory_with_drag(v0, angle, h0, g, k, m, dt=0.01):
    """
    Calculate the trajectory of a projectile with air resistance using Runge-Kutta method.
    :param v0: Initial velocity
    :param angle: Launch angle in degrees
    :param h0: Initial height
    :param g: Acceleration due to gravity
    :param k: Drag constant
    :param m: Mass of the projectile
    :param dt: Time step for simulation
    :return: Arrays of x and y coordinates
    """
    
    theta = np.radians(angle)
    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)
    state = [0, h0, vx0, vy0]
    x_vals, y_vals = [], []
    
    while state[1] >= 0:  # While above the ground
        state = runge_kutta_step(state, dt, g, k, m)
        x_vals.append(state[0])
        y_vals.append(state[1])

    return np.array(x_vals), np.array(y_vals)

