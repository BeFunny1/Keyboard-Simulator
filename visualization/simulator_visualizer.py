from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from work_with_confg.config_handler import ConfigHandler


class MainWindowKeyboard(QMainWindow):
    def __init__(self, for_test: bool):
        self.config_handler = ConfigHandler()
        if not for_test:
            QMainWindow.__init__(self)
            self.buttons, self.labels, self.text_label, self.line_label, self.timer \
                = self.setupUi(self)
            self.logic_activity = None

    def update_stopwatch(self, time: str):
        self.labels['Время:']['related_item'].setText(time)

    def update_the_keyboard_layout(self, old_language: str, new_language: str):
        characters_of_the_language = self.config_handler.read_config_file(
            'symbols_on_the_keyboard_by_language.json')
        for index, symbol in enumerate(characters_of_the_language[old_language]):
            new_symbol = characters_of_the_language[new_language][index]
            self.buttons[old_language + '_' + symbol].setText(new_symbol)
            self.buttons[new_language + '_' + new_symbol] = self.buttons.pop(old_language + '_' + symbol)

    @staticmethod
    def select_letter_in_text(line: str, index: int) -> str:
        line_after_symbol, symbol, line_before_symbol \
            = line[:index], line[index], line[1 + index:]
        symbol = f'[{symbol}]'
        return line_after_symbol + symbol + line_before_symbol

    def update_labels(self, accuracy, progress,
                      number_invalid_symbols,
                      number_entered_symbols):
        self.labels['Знаки:']['related_item'].setText(
            str(number_entered_symbols))
        self.labels['Ошибки:']['related_item'].setText(
            str(number_invalid_symbols))
        self.labels['Точность:']['related_item'].setText(
            str(accuracy) + '%')
        self.labels['Прогресс:']['related_item'].setValue(
            progress)

    def update_speed(self, number_of_symbols_per_minute):
        self.labels['Симв./мин.:']['related_item'].setText(
            str(number_of_symbols_per_minute))

    def establish_communication(self, activity):
        self.logic_activity = activity

    def keyPressEvent(self, event):
        self.logic_activity(event.text(), event.key())

    def point_to_the_button(self, first_part_of_the_key: str, second_part_of_the_key: str):
        keyboard_shortcuts \
            = self.config_handler.read_config_file('keyboard_shortcuts.json')
        trial_key = f'{first_part_of_the_key}_{second_part_of_the_key}'
        if second_part_of_the_key.isupper():
            key = [f'{first_part_of_the_key}_{second_part_of_the_key.upper()}',
                   f'{first_part_of_the_key}_Shift_R',
                   f'{first_part_of_the_key}_Shift_L']
        elif trial_key not in self.buttons:
            for language in ['multi_language', first_part_of_the_key]:
                if second_part_of_the_key in keyboard_shortcuts[language]:
                    key = []
                    for x in keyboard_shortcuts[language][second_part_of_the_key]:
                        key.append(f'{first_part_of_the_key}_{x}')
                    break
            else:
                key = f'{first_part_of_the_key}_{second_part_of_the_key.upper()}'
        else:
            key = trial_key
        self.hide_all_buttons()
        for button in self.buttons:
            if button in key:
                self.select_a_button(button)

    def hide_all_buttons(self):
        styles = self.config_handler.read_config_file('button_style.json')
        for button in self.buttons:
            self.buttons[button].setStyleSheet(styles['hide'])

    def select_a_button(self, key: str):
        styles = self.config_handler.read_config_file('button_style.json')
        self.buttons[key].setStyleSheet(styles['press'])

    def set_text_and_select_letter(self, text: str, index: int):
        text = self.select_letter_in_text(text, index)
        self.text_label.setText(text)

    def set_line_label_text(self, text: str):
        self.line_label.setText(text)

    def setupUi(self, keyboard_simulator_window) \
            -> (dict, dict, QtWidgets.QLabel, QtWidgets.QLabel):
        self.customize_window(keyboard_simulator_window)
        buttons = self.create_buttons(keyboard_simulator_window)
        labels = self.create_labels_and_his_related_element(
            keyboard_simulator_window)
        line_label = self.create_line_label(keyboard_simulator_window)
        text_label = self.create_text_label(keyboard_simulator_window)
        timer = self.create_timer(keyboard_simulator_window)
        lines = {
            1: [180, 150, 90, 3],
            2: [330, 150, 510, 3]
        }
        for key in lines:
            data = lines[key]
            self.create_line(
                data[0], data[1],
                data[2], data[3],
                keyboard_simulator_window
            )
        QtCore.QMetaObject.connectSlotsByName(keyboard_simulator_window)
        return buttons, labels, text_label, line_label, timer

    @staticmethod
    def customize_window(keyboard_simulator_window):
        keyboard_simulator_window.setFocusPolicy(QtCore.Qt.NoFocus)
        keyboard_simulator_window.setObjectName("KeyboardSimulator")
        keyboard_simulator_window.setMinimumSize(QtCore.QSize(1024, 768))
        keyboard_simulator_window.setMaximumSize(QtCore.QSize(1024, 768))
        keyboard_simulator_window.setBaseSize(QtCore.QSize(1024, 768))
        keyboard_simulator_window.setWindowTitle("Клавиатурный тренажёр")

    def get_data_for_buttons(self) -> dict:
        data = {}
        rows_and_indexes_for_row =\
            self.config_handler.read_config_file(
                'rows_and_indexes_for_row.json')
        for index in rows_and_indexes_for_row:
            row = rows_and_indexes_for_row[index]['row']
            x_start, y = rows_and_indexes_for_row[index]['indexes']
            for i, key_name in enumerate(row):
                data[key_name] = {}
                data[key_name]['x'] = x_start + 60 * i
                data[key_name]['y'] = y
                data[key_name]['weight'] = 50
                data[key_name]['height'] = 50
        special_keys \
            = self.config_handler.read_config_file('special_keys.json')
        for key in special_keys.keys():
            data[key] = {}
            data[key]['x'] = special_keys[key][0]
            data[key]['y'] = special_keys[key][1]
            data[key]['weight'] = special_keys[key][2]
            data[key]['height'] = special_keys[key][3]
        return data

    def create_buttons(self, keyboard_simulator_window) -> dict:
        data = self.get_data_for_buttons()
        buttons = {}
        for key in data.keys():
            button = QtWidgets.QPushButton(keyboard_simulator_window)
            button.setEnabled(True)
            button.setGeometry(
                QtCore.QRect(
                    data[key]['x'],
                    data[key]['y'],
                    data[key]['weight'],
                    data[key]['height']
                )
            )
            button.setObjectName('button_' + key)
            button.setText(key)
            button.setEnabled(False)
            buttons['russian_' + key] = button
        return buttons

    def get_data_for_labels(self) -> dict:
        labels = self.config_handler.read_config_file('labels.json')
        data = {}
        index = 0
        for label in labels.keys():
            data[label] = {}
            data[label]['related_item'] = {}
            related_item_default_text = labels[label]
            data[label]['related_item']['text'] = related_item_default_text
            if label != 'Прогресс:':
                data[label]['x'] = 320 + index * 110
                data[label]['related_item']['x'] = 320 + index * 110
                data[label]['related_item']['weight'] = 90
            else:
                data[label]['x'] = 180
                data[label]['related_item']['x'] = 170
                data[label]['related_item']['weight'] = 120
            data[label]['y'] = 130
            data[label]['related_item']['y'] = 160
            data[label]['weight'] = 90

            data[label]['height'] = 20
            data[label]['related_item']['height'] = 20
            index += 1
        return data

    def create_labels_and_his_related_element(
            self, keyboard_simulator_window) -> dict:
        data = self.get_data_for_labels()
        labels_and_related_items = {}
        for key in data.keys():
            label = self.create_label(
                data[key], key, keyboard_simulator_window
            )
            data_about_related_item = data[key]['related_item']
            if key != 'Прогресс:':
                related_item = self.create_label(
                    data_about_related_item,
                    data_about_related_item['text'],
                    keyboard_simulator_window
                )
            else:
                related_item = self.create_progress_bar(
                    data_about_related_item,
                    keyboard_simulator_window
                )
            labels_and_related_items[key] = {}
            labels_and_related_items[key]['label'] = label
            labels_and_related_items[key]['related_item'] = related_item
        return labels_and_related_items

    @staticmethod
    def create_timer(keyboard_simulator_window) -> QtWidgets.QTimeEdit:
        timer = QtWidgets.QTimeEdit(keyboard_simulator_window)
        timer.setGeometry(QtCore.QRect(760, 100, 90, 20))
        timer.setReadOnly(False)
        timer.setObjectName("timeEdit")
        timer.setDisplayFormat("hh:mm:ss")
        return timer

    @staticmethod
    def create_progress_bar(data, keyboard_simulator_window) \
            -> QtWidgets.QProgressBar:
        x, y, weight, height \
            = data['x'], data['y'], data['weight'], data['height']
        progress_bar = QtWidgets.QProgressBar(keyboard_simulator_window)
        progress_bar.setGeometry(QtCore.QRect(x, y, weight, height))
        progress_bar.setProperty("value", 0)
        progress_bar.setObjectName("progressBar")
        return progress_bar

    @staticmethod
    def create_label(data, text, keyboard_simulator_window) \
            -> QtWidgets.QLabel:
        x, y, weight, height \
            = data['x'], data['y'], data['weight'], data['height']
        label = QtWidgets.QLabel(keyboard_simulator_window)
        label.setGeometry(QtCore.QRect(x, y, weight, height))
        label.setTextFormat(QtCore.Qt.AutoText)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName('label' + text)
        label.setText(text)
        return label

    @staticmethod
    def create_line_label(keyboard_simulator_window) -> QtWidgets.QLabel:
        line_label = QtWidgets.QLabel(keyboard_simulator_window)
        line_label.setGeometry(QtCore.QRect(110, 300, 810, 40))
        line_label.setObjectName("line_label")
        line_label.setStyleSheet("border: 1px solid black;")
        return line_label

    @staticmethod
    def create_text_label(keyboard_simulator_window) -> QtWidgets.QLabel:
        text_label = QtWidgets.QLabel(keyboard_simulator_window)
        text_label.setGeometry(QtCore.QRect(110, 200, 810, 90))
        text_label.setObjectName("text_label")
        text_label.setWordWrap(True)
        text_label.setStyleSheet("border: 1px solid black;")
        return text_label

    @staticmethod
    def create_line(x, y, weight, height, keyboard_simulator_window):
        line = QtWidgets.QFrame(keyboard_simulator_window)
        line.setGeometry(QtCore.QRect(x, y, weight, height))
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line")
