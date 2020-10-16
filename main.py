import sys
from PyQt5.QtWidgets import QApplication

from simulator_logic.basic_logic import Simulator
from visualization.visualizer import MainWindowKeyboard

if __name__ == '__main__':
    app = QApplication(sys.argv)
    user_interface = MainWindowKeyboard(for_test=False)

    simulator = Simulator(user_interface, for_test=False)

    user_interface.establish_communication(simulator.activity)
    simulator.preparation()

    user_interface.show()
    sys.exit(app.exec_())
