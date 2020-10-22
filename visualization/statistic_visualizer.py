from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore


class StatisticVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")

    def setupUi(self, number_of_symbols_per_interval: dict,
                log_for_entering_parts_of_text: dict) -> None:
        self.customize_window(self)

        layouts = self.create_layouts()

        chart_view = self.create_line_chart(number_of_symbols_per_interval)
        layouts[0].addWidget(chart_view)

        labels = self.create_labels(log_for_entering_parts_of_text)
        for label in labels:
            layouts[1].addWidget(label)
        self.setCentralWidget(self.central_widget)

    @staticmethod
    def create_labels(log_for_entering_parts_of_text: dict) -> [QLabel]:
        data = []
        for time in log_for_entering_parts_of_text:
            label = QLabel()
            label.setObjectName('label'+str(time))

            line_for_label = log_for_entering_parts_of_text[time]['line']
            score_for_label = log_for_entering_parts_of_text[time]['score']
            time_for_label = f'{time[0]}:{time[1]}'
            text = \
                f'Time interval: {time_for_label};\n' \
                f'Line: ...{line_for_label}...;\n' \
                f'Symbols score: {score_for_label}'
            label.setText(text)
            data.append(label)
        return data

    @staticmethod
    def customize_window(statistic_visualizer_window) -> None:
        statistic_visualizer_window.setObjectName("StatisticVisualizer")
        statistic_visualizer_window.setMinimumSize(QtCore.QSize(1280, 720))
        statistic_visualizer_window.setMaximumSize(QtCore.QSize(1280, 720))
        statistic_visualizer_window.setBaseSize(QtCore.QSize(1280, 720))
        statistic_visualizer_window.setWindowTitle("Статистика")

    def create_layouts(self) -> [QtWidgets.QVBoxLayout]:
        layouts = []
        for index in range(2):
            vertical_layout_widget = QtWidgets.QWidget(self.central_widget)
            vertical_layout_widget.setGeometry(
                QtCore.QRect(710 * index + 10, 10, 620, 700))
            vertical_layout_widget.setObjectName(
                'verticalLayoutWidget' + str(index))
            vertical_layout = QtWidgets.QVBoxLayout(vertical_layout_widget)
            vertical_layout.setContentsMargins(0, 0, 0, 0)
            vertical_layout.setObjectName('verticalLayout' + str(index))
            layouts.append(vertical_layout)
        return layouts

    def create_line_chart(
            self, number_of_symbols_per_interval: dict) -> QChartView:
        series = QLineSeries(self)

        series.append(0, 0)
        for time in number_of_symbols_per_interval.keys():
            series.append(time, number_of_symbols_per_interval[time])

        chart = QChart()
        chart.addSeries(series)

        chart.legend().setVisible(False)
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle('Диаграмма')

        axis_x = QValueAxis()
        axis_x.setTitleText('Time')
        axis_y = QValueAxis()
        axis_y.setTitleText('Symbols counter per interval')
        chart.addAxis(axis_x, Qt.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        return chart_view


if __name__ == '__main__':
    pass
