from simulator_logic.work_with_text import WorkWithText
from work_with_confg.config_handler import ConfigHandler
from PyQt5 import QtCore
import time


class Simulator:
    def __init__(self, user_interface, for_test: bool):
        if not for_test:
            self.window = user_interface
            self.config_handler = ConfigHandler()

            worker = WorkWithText()
            self.text = worker.read_file('text1.txt')
            self.symbols = worker.split(self.text)

            self.current_symbols = self.symbols.pop()

            self.stopwatch = self.create_stopwatch()
            self.stopwatch_time = QtCore.QTime(0, 0, 0)
        self.current_line = ''

        self.progress = 0
        self.number_of_entered_characters = 0
        self.number_of_invalid_characters = 0
        self.accuracy = 100

        self.is_first_activity = True

        self.key_press_time = []
        self.current_time_ns = 0

        self.index = 0

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

    def preparation(self):
        self.update_text()
        self.window.point_to_the_button(self.current_symbols.upper())

    def activity(self, key: str, number_key: int):
        if self.is_first_activity:
            self.stopwatch.start(1000)
            self.is_first_activity = False
        numbers_unaccountable_characters \
            = self.config_handler.read_config_file(
             'numbers_unaccountable_characters.json')
        if key == self.current_symbols:
            self.current_line += self.current_symbols
            self.update_line(self.current_line)
            if len(self.symbols) != 0:
                self.current_symbols = self.symbols.pop()
                self.window.point_to_the_button(self.current_symbols.upper())
                self.index += 1
            else:
                self.window.point_to_the_button('')
                self.stopwatch.stop()
            self.number_of_entered_characters += 1
            self.key_press_time.append(time.perf_counter_ns())
            self.update_statistic_data()
            self.update_text()

        elif number_key not in numbers_unaccountable_characters.values():
            self.number_of_invalid_characters += 1
            self.update_statistic_data()
        max_length_line = 126
        if len(self.current_line) == max_length_line:
            self.current_line = ''
            self.update_line(self.current_line)

    def calculate_number_of_symbols_in_last_second(self):
        current_time = time.perf_counter_ns()
        nanoseconds_per_second = 1000000000
        index_of_the_first_matching_element = None
        for index, element in enumerate(self.key_press_time):
            if current_time - element < nanoseconds_per_second:
                index_of_the_first_matching_element = index
                break
        if index_of_the_first_matching_element is not None:
            del self.key_press_time[:index_of_the_first_matching_element]
        else:
            self.key_press_time.clear()
        return len(self.key_press_time)

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
        self.window.set_text_and_select_letter(self.text, self.index)


if __name__ == '__main__':
    pass
