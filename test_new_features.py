import sys

from PyQt5 import QtCore


def timerEvent():
    global time
    time = time.addSecs(1)
    print(time.toString("ss"))


app = QtCore.QCoreApplication(sys.argv)

timer = QtCore.QTimer()
time = QtCore.QTime(0, 0, 50)

timer.timeout.connect(timerEvent)
timer.start(1000)

sys.exit(app.exec_())