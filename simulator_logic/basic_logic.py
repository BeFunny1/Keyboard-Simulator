import sys

from PyQt5.uic.properties import QtWidgets

from simulator_logic.work_with_text import WorkWithText
from visualization.statistic_visualizer import StatisticVisualizer
from work_with_confg.config_handler import ConfigHandler
from simulator_logic.calculate_statistic import StatisticCalculating
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import time


class Simulator:
    def __init__(self, user_interface, for_test: bool):
        if not for_test:
            self.window = user_interface
            self.config_handler = ConfigHandler()

            worker = WorkWithText()
            self.text = worker.read_file('text1.txt')
            self.symbols = worker.split(self.text)
            self.suggestions_in_the_text \
                = worker.split_string_into_substrings(self.text, max_line_length=120)
            self.suggestions_in_the_text.reverse()
            self.current_suggestions_on_display = self.suggestions_in_the_text.pop()

            self.current_symbols = self.symbols.pop()
            self.language = ''
            self.language = self.define_the_language(self.current_symbols)

            self.stopwatch = self.create_stopwatch()
            self.stopwatch_time = QtCore.QTime(0, 0, 0)

        self.current_line = ''

        self.start_time = 0
        self.timer = None

        self.progress = 0
        self.number_of_entered_characters = 0
        self.number_of_invalid_characters = 0
        self.accuracy = 100

        self.key_press_time = []
        self.current_time_ns = 0
        self.current_index_symbol = 0

        self.is_first_activity = True
        self.the_end = False

    def define_the_language(self, symbol: str) -> str:
        symbol = symbol.upper()
        characters_of_the_language = self.config_handler.read_config_file(
            'characters_of_the_language.json')
        if self.language == '':
            for language in characters_of_the_language:
                if symbol in characters_of_the_language[language]:
                    return language
        else:
            if symbol in characters_of_the_language[self.language]:
                return self.language
            else:
                for language in characters_of_the_language:
                    if symbol in characters_of_the_language[language]:
                        return language
        return 'russian'

    def create_stopwatch(self):
        stopwatch = QtCore.QTimer()
        stopwatch.timeout.connect(self.stopwatch_event)
        return stopwatch

    def stopwatch_event(self):
        self.stopwatch_time = self.stopwatch_time.addSecs(1)
        self.window.update_stopwatch(self.stopwatch_time.toString("hh:mm:ss"))

        number_of_symbols_per_minute \
            = self.calculate_number_of_symbols_in_last_second() * 60
        self.window.update_speed(number_of_symbols_per_minute)
        if self.stopwatch_time == self.timer:
            self.stop_the_workout()

    def preparation(self):
        self.update_text()
        if self.language != 'russian':
            self.window.update_the_keyboard_layout('russian', self.language)
        self.window.point_to_the_button(
            first_part_of_the_key=self.language,
            second_part_of_the_key=self.current_symbols)

    def activity(self, key: str, number_key: int):
        if not self.the_end:
            if self.is_first_activity:
                self.stopwatch.start(1000)
                self.start_time = time.time()
                self.read_time_from_the_timer()
                self.is_first_activity = False

            numbers_unaccountable_characters \
                = self.config_handler.read_config_file(
                'numbers_unaccountable_characters.json')
            if key == self.current_symbols:
                self.current_line += self.current_symbols
                self.update_line(self.current_line)
                if len(self.symbols) != 0:
                    self.current_symbols = self.symbols.pop()

                    language = self.define_the_language(self.current_symbols)
                    if language != self.language:
                        self.window.update_the_keyboard_layout(self.language, language)
                        self.language = language

                    self.window.point_to_the_button(
                        first_part_of_the_key=self.language,
                        second_part_of_the_key=self.current_symbols)
                    self.current_index_symbol += 1

                else:
                    self.stop_the_workout()
                if self.current_line == self.current_suggestions_on_display \
                        and not self.the_end:
                    self.reset_input_line()
                self.number_of_entered_characters += 1
                self.key_press_time.append(time.time() - self.start_time)
                self.update_statistic_data()
                self.update_text()

            elif number_key not in numbers_unaccountable_characters.values():
                self.number_of_invalid_characters += 1
                self.update_statistic_data()

    def calculate_statistic(self) -> (dict, dict):
        calculator = StatisticCalculating()
        number_of_characters_per_second \
            = calculator.get_count_the_number_of_repetitions(
              self.key_press_time)
        number_of_characters_per_interval \
            = calculator.calculate_data_based_on_the_interval(
              number_of_characters_per_second, interval=10)
        data = calculator.get_fast_typing_string(
            self.text, number_of_characters_per_interval)
        return number_of_characters_per_interval, data

    def create_statistic_window(self, number_of_symbols_per_interval: dict,
                                log_for_entering_parts_of_text: dict):
        self.statistic_window = StatisticVisualizer()
        self.statistic_window.setupUi(number_of_symbols_per_interval, log_for_entering_parts_of_text)
        self.statistic_window.show()

    def reset_input_line(self):
        self.current_suggestions_on_display = self.suggestions_in_the_text.pop()
        self.current_line = ''
        self.update_line(self.current_line)
        self.current_index_symbol = 0

    def stop_the_workout(self):
        self.window.hide_all_buttons()
        self.stopwatch.stop()
        self.the_end = True

        number_of_symbols_per_interval, log_for_entering_parts_of_text\
            = self.calculate_statistic()
        self.create_statistic_window(
            number_of_symbols_per_interval,
            log_for_entering_parts_of_text)

    def read_time_from_the_timer(self):
        timer = self.window.timer.time()
        self.window.timer.setReadOnly(True)
        if timer != QtCore.QTime(0, 0, 0):
            self.timer = timer
        self.window.setFocusPolicy(QtCore.Qt.NoFocus)

    def calculate_number_of_symbols_in_last_second(self):
        current_time = time.time()
        number_of_characters_entered = 0
        for index, element in enumerate(self.key_press_time):
            if current_time - element < 1:
                number_of_characters_entered += 1
        return number_of_characters_entered

    def update_statistic_data(self):
        self.accuracy = round((self.number_of_entered_characters /
                               (self.number_of_entered_characters +
                                self.number_of_invalid_characters)) * 100)
        self.progress = round((self.number_of_entered_characters /
                               len(self.text)) * 100)
        self.window.update_labels(self.accuracy, self.progress,
                                  self.number_of_invalid_characters,
                                  self.number_of_entered_characters)

    def update_line(self, new_line: str):
        self.window.set_line_label_text(new_line)

    def update_text(self):
        self.window.set_text_and_select_letter(
            self.current_suggestions_on_display, self.current_index_symbol)


if __name__ == '__main__':
    pass
