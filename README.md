# Realistic Projectile Simulation

## Project Overview
The Realistic Projectile Simulation is an advanced computational tool designed for simulating projectile motion with a focus on realism. It accounts for various physical factors such as air resistance, wind speed, and angle of launch. This tool is ideal for educational purposes, physics research, and engineering applications.

## Installation and Setup
Requirements:
- Python 3.8 or higher
- PyQt6 for GUI components
- NumPy for numerical computations
- Matplotlib for plotting trajectories

Installation:
1. Clone the repository: `git clone https://github.com/trymthoren/realistic-projectile-simulation.git`
2. Navigate to the cloned directory.
3. Install dependencies: `pip install -r requirements.txt`

## File Descriptions
- `main.py`: The entry point of the application. It sets up the main window and the application loop.
- `gui.py`: Handles the graphical user interface, allowing users to input parameters and view simulations.
- `air_resistance.py`: Contains functions for calculating the effects of air resistance on the projectile.
- `angle_loop.py`: Iterates over different launch angles to simulate and compare trajectories.
- `monte_carlo_simulation.py`: Implements Monte Carlo simulations for a probabilistic analysis of projectile motion.

## Usage
To run the application:
1. Ensure you are in the project's root directory.
2. Execute `python main.py`.
3. Use the GUI to input simulation parameters and run simulations.

## Contributing
We welcome contributions, including bug fixes, feature requests, and documentation improvements. Please submit pull requests for any contributions.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
