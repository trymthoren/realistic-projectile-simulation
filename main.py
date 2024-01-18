import sys
from gui import MainWindow
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
