import sys

from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QMessageBox, QMainWindow, QApplication, QPushButton, QLayout, \
    QGridLayout, QFormLayout


class KpeWindow(QWidget):
    def __init__(self, parent):
        self.parent = parent
        QWidget.__init__(self, self.parent)

        main = QFormLayout(self)

        self.label = QLabel(self)
        # self.button = QPushButton()
        # self.button.setGeometry(QtCore.QRect(150, 410, 70, 50))
        self.label.setText('Test the keyPressEvent')
        main.addWidget(self.label)
        # main.addWidget(self.button)

        self.adjustSize()
        self.setLayout(main)

    def keyPressEvent(self, event):

        # QMessageBox.warning(self, 'MDI', 'keyPressEvent')
        self.label.setText('Heh')
        self.parent.button.setGeometry(QtCore.QRect(200, 410, 70, 50))


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('KeyPressEvent Test')
        self.setMinimumSize(QtCore.QSize(1024, 768))

        self.button = QPushButton(self)
        self.button.setGeometry(QtCore.QRect(150, 410, 70, 50))

        main = QVBoxLayout(self)
        child = KpeWindow(self)
        child.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setFocusProxy(child)
        main.addWidget(child)
        child.setFocus(True)

        self.adjustSize()
        self.setLayout(main)

    def heh(self):
        self.setWindowTitle('Heh')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
