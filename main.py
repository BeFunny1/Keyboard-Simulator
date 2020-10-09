import sys
from PyQt5 import QtWidgets

from visualization import WindowKeyboard

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    keyboard_simulator_window = QtWidgets.QDialog()
    user_interface = WindowKeyboard(keyboard_simulator_window, False)
    keyboard_simulator_window.show()
    sys.exit(app.exec_())
