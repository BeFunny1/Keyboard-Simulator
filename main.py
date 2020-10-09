import sys
from PyQt5 import QtWidgets

from visualization import WindowKeyboard

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    KeyboardSimulator = QtWidgets.QDialog()
    ui = WindowKeyboard()
    ui.setupUi(KeyboardSimulator)
    KeyboardSimulator.show()
    sys.exit(app.exec_())
