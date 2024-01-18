from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QTextEdit, QCheckBox
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import monte_carlo_simulation
import angle_loop
import air_resistance

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

    def plot(self, data, line_style='r-', label=None):
        self.axes.clear()
        self.axes.plot(data[0], data[1], line_style, label=label)
        if label:
            self.axes.legend()
        self.axes.set_title('Projectile Motion')
        self.axes.set_xlabel('Distance (m)')  # Label for x-axis
        self.axes.set_ylabel('Height (m)')    # Label for y-axis
        self.draw()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Projectile Motion Simulator")
        self.setGeometry(100, 100, 800, 600)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.v0_input = QLineEdit(self)
        self.v0_input.setPlaceholderText("Enter initial velocity (v0)")
        layout.addWidget(self.v0_input)

        self.theta_input = QLineEdit(self)
        self.theta_input.setPlaceholderText("Enter launch angle (theta)")
        layout.addWidget(self.theta_input)

        self.diameter_input = QLineEdit(self)
        self.diameter_input.setPlaceholderText("Enter diameter of the ball (cm)")
        layout.addWidget(self.diameter_input)

        self.mass_input = QLineEdit(self)
        self.mass_input.setPlaceholderText("Enter mass of the ball (kg)")
        layout.addWidget(self.mass_input)

        self.with_drag_checkbox = QCheckBox("With Drag", self)
        layout.addWidget(self.with_drag_checkbox)

        self.without_drag_checkbox = QCheckBox("Without Drag", self)
        layout.addWidget(self.without_drag_checkbox)

        self.monte_carlo_button = QPushButton("Run Monte Carlo Simulation", self)
        self.monte_carlo_button.clicked.connect(self.runMonteCarloSimulation)
        layout.addWidget(self.monte_carlo_button)

        self.angle_loop_button = QPushButton("Run Angle Loop", self)
        self.angle_loop_button.clicked.connect(self.runAngleLoop)
        layout.addWidget(self.angle_loop_button)

        self.reset_button = QPushButton("Reset", self)
        self.reset_button.clicked.connect(self.resetSimulation)
        layout.addWidget(self.reset_button)

        self.results_area = QTextEdit(self)
        self.results_area.setReadOnly(True)
        layout.addWidget(self.results_area)

        self.plot_canvas = PlotCanvas(self, width=5, height=4)
        layout.addWidget(self.plot_canvas)

    def runMonteCarloSimulation(self):
        # Extract parameters
        v0 = float(self.v0_input.text())
        theta = float(self.theta_input.text())
        diameter_cm = float(self.diameter_input.text())
        mass = float(self.mass_input.text())
        g = 9.81  # Acceleration due to gravity
        k = air_resistance.calculate_drag_constant(diameter_cm, mass)

        # Clear previous results
        self.results_area.clear()
        self.plot_canvas.axes.clear()

        result_text = ""  # For displaying results

        if self.with_drag_checkbox.isChecked():
            # Simulation with drag
            x, y = air_resistance.trajectory_with_drag(v0, theta, 0, g, k, mass, dt=0.01)
            self.plot_canvas.plot((x, y), 'r-', label='With Drag')
            max_height = np.max(y)
            max_distance = x[-1]
            result_text += f"With Drag - Max Height: {max_height:.2f} m, Max Distance: {max_distance:.2f} m\n"

        if self.without_drag_checkbox.isChecked():
            # Simulation without drag
            x, y = trajectory_without_drag(v0, theta, 0, g, dt=0.01)
            self.plot_canvas.plot((x, y), 'b--', label='Without Drag')
            max_height = np.max(y)
            max_distance = x[-1]
            result_text += f"Without Drag - Max Height: {max_height:.2f} m, Max Distance: {max_distance:.2f} m\n"

        self.results_area.setText(result_text)
        self.plot_canvas.axes.legend()
        self.plot_canvas.draw()



    def runAngleLoop(self):
        v0 = float(self.v0_input.text())
        g = 9.81  # Acceleration due to gravity
        diameter_cm = float(self.diameter_input.text())
        mass = float(self.mass_input.text())
        k = air_resistance.calculate_drag_constant(diameter_cm, mass)

        angle_results = angle_loop.loop_over_angles(v0, g, range(5, 90, 5), k, mass)
        
        # Format and display the results
        formatted_results = "\n".join([f"Angle: {angle}°, Distance: {distance:.2f} m" for angle, distance in angle_results])
        self.results_area.setText(formatted_results)


    def resetSimulation(self):
        self.v0_input.clear()
        self.theta_input.clear()
        self.diameter_input.clear()
        self.mass_input.clear()
        self.results_area.clear()
        self.plot_canvas.axes.clear()
        self.plot_canvas.draw()
        self.with_drag_checkbox.setChecked(False)
        self.without_drag_checkbox.setChecked(False)
        
        
    def main():
        app = QApplication([])
        main_window = MainWindow()
        main_window.show()
        app.exec()

        if __name__ == "__main__":
            main()
