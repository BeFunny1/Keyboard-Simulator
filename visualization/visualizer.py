from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class MainWindowKeyboard(QMainWindow):
    def __init__(self, for_test: bool):
        if not for_test:
            QMainWindow.__init__(self)
            self.buttons, self.labels, self.text_label, self.line_label \
                = self.setupUi(self)
            self.logic_activity = None

    @staticmethod
    def split_a_string_by_index(line: str, index: int):
        line_after_symbol = ''
        symbol = ''
        line_before_symbol = ''
        for index_symbol in range(len(line)):
            if index_symbol < index:
                line_after_symbol += line[index_symbol]
            elif index_symbol == index:
                symbol = line[index_symbol]
            elif index_symbol > index:
                line_before_symbol += line[index_symbol]
        return line_after_symbol, symbol, line_before_symbol

    def select_letter_in_text(self, line: str, index: int):
        line_after_symbol, symbol, line_before_symbol \
            = self.split_a_string_by_index(line, index)
        symbol = '[' + symbol + ']'
        return line_after_symbol + symbol + line_before_symbol

    def update_labels(self, accuracy, progress,
                      number_invalid_symbols, number_entered_symbols):
        self.labels['Знаки:']['related_item'].setText(
            str(number_entered_symbols))
        self.labels['Ошибки:']['related_item'].setText(
            str(number_invalid_symbols))
        self.labels['Точность:']['related_item'].setText(
            str(accuracy) + '%')
        self.labels['Прогресс:']['related_item'].setValue(
            progress)

    def establish_communication(self, activity):
        self.logic_activity = activity

    def keyPressEvent(self, event):
        self.logic_activity(event.text(), event.key())

    def point_to_the_button(self, key: str):
        keyboard_shortcuts = {
            '!': ['1', 'Shift_R', 'Shift_L'], '"': ['2', 'Shift_R', 'Shift_L'],
            '№': ['3', 'Shift_R', 'Shift_L'], ';': ['4', 'Shift_R', 'Shift_L'],
            '%': ['5', 'Shift_R', 'Shift_L'], ':': ['6', 'Shift_R', 'Shift_L'],
            '?': ['7', 'Shift_R', 'Shift_L'], '*': ['8', 'Shift_R', 'Shift_L'],
            '(': ['9', 'Shift_R', 'Shift_L'], ')': ['0', 'Shift_R', 'Shift_L'],
            '-': ['2', 'Shift_R', 'Shift_L'], '+': ['=', 'Shift_R', 'Shift_L'],
            '/': ['2', 'Shift_R', 'Shift_L'], ',': ['.', 'Shift_R', 'Shift_L']
        }
        if key in keyboard_shortcuts:
            key = keyboard_shortcuts[key]
        for button in self.buttons:
            if button not in key:
                self.buttons[button].setEnabled(False)
                self.buttons[button].setDefault(False)
            else:
                self.buttons[button].setEnabled(True)
                self.buttons[button].setDefault(True)

    def set_text_and_select_letter(self, text: str, index: int):
        text = self.select_letter_in_text(text, index)
        self.text_label.setText(text)

    def set_line_label_text(self, text: str):
        self.line_label.setText(text)

    def setupUi(self, keyboard_simulator_window):
        self.customize_window(keyboard_simulator_window)
        buttons = self.create_buttons(keyboard_simulator_window)
        labels = self.create_labels_and_his_related_element(
            keyboard_simulator_window)
        line_label = self.create_line_label(keyboard_simulator_window)
        text_label = self.create_text_label(keyboard_simulator_window)
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
        return buttons, labels, text_label, line_label

    @staticmethod
    def customize_window(keyboard_simulator_window):
        keyboard_simulator_window.setObjectName("KeyboardSimulator")
        keyboard_simulator_window.setEnabled(True)
        keyboard_simulator_window.resize(1024, 768)
        keyboard_simulator_window.setMinimumSize(QtCore.QSize(1024, 768))
        keyboard_simulator_window.setMaximumSize(QtCore.QSize(1024, 768))
        keyboard_simulator_window.setBaseSize(QtCore.QSize(1024, 768))
        keyboard_simulator_window.setAutoFillBackground(False)
        keyboard_simulator_window.setWindowTitle("Клавиатурный тренажёр")

    @staticmethod
    def get_data_for_buttons():
        data = {}
        first_row = ['Ё', '1', '2', '3', '4', '5', '6',
                     '7', '8', '9', '0', '-', '=']
        second_row = ['Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г',
                      'Ш', 'Щ', 'З', 'Х', 'Ъ', '\\']
        third_row = ['Ф', 'Ы', 'В', 'А', 'П', 'Р',
                     'О', 'Л', 'Д', 'Ж', 'Э']
        fourth_row = ['Я', 'Ч', 'С', 'М', 'И',
                      'Т', 'Ь', 'Б', 'Ю', '.']
        rows_and_indexes_for_row = {
            1: {'row': first_row, 'indexes': (90, 350)},
            2: {'row': second_row, 'indexes': (170, 410)},
            3: {'row': third_row, 'indexes': (190, 470)},
            4: {'row': fourth_row, 'indexes': (220, 530)}
        }
        for index in rows_and_indexes_for_row:
            row = rows_and_indexes_for_row[index]['row']
            x_start, y = rows_and_indexes_for_row[index]['indexes']
            for i in range(len(row)):
                key_name = row[i]
                data[key_name] = {}
                data[key_name]['x'] = x_start + 60 * i
                data[key_name]['y'] = y
                data[key_name]['weight'] = 50
                data[key_name]['height'] = 50
        special_keys = {
            'Tab': [90, 410, 70, 50],
            'Caps Lock': [90, 470, 90, 50],
            'Shift_L': [90, 530, 120, 50],
            ' ': [280, 590, 470, 50],
            'Backspace': [870, 350, 70, 50],
            'Enter': [850, 470, 90, 50],
            'Shift_R': [820, 530, 120, 50]
        }
        for key in special_keys.keys():
            data[key] = {}
            data[key]['x'] = special_keys[key][0]
            data[key]['y'] = special_keys[key][1]
            data[key]['weight'] = special_keys[key][2]
            data[key]['height'] = special_keys[key][3]
        return data

    def create_buttons(self, keyboard_simulator_window):
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
            buttons[key] = button
        return buttons

    @staticmethod
    def get_data_for_labels():
        labels = {
            'Знаки:': '0', 'Ошибки:': '0',
            'Точность:': '100%', 'Прогресс:': ''
        }
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

    def create_labels_and_his_related_element(self, keyboard_simulator_window):
        data = self.get_data_for_labels()
        labels_and_related_items = {}
        for key in data.keys():
            label = self.create_label(
                data[key]['x'], data[key]['y'], data[key]['weight'],
                data[key]['height'], key, keyboard_simulator_window
            )
            data_about_related_item = data[key]['related_item']
            if key != 'Прогресс:':
                related_item = self.create_label(
                    data_about_related_item['x'],
                    data_about_related_item['y'],
                    data_about_related_item['weight'],
                    data_about_related_item['height'],
                    data_about_related_item['text'],
                    keyboard_simulator_window
                )
            else:
                related_item = self.create_progress_bar(
                    data_about_related_item['x'],
                    data_about_related_item['y'],
                    data_about_related_item['weight'],
                    data_about_related_item['height'],
                    keyboard_simulator_window
                )
            labels_and_related_items[key] = {}
            labels_and_related_items[key]['label'] = label
            labels_and_related_items[key]['related_item'] = related_item
        return labels_and_related_items

    @staticmethod
    def create_progress_bar(x, y, weight, height, keyboard_simulator_window):
        progress_bar = QtWidgets.QProgressBar(keyboard_simulator_window)
        progress_bar.setGeometry(QtCore.QRect(x, y, weight, height))
        progress_bar.setProperty("value", 0)
        progress_bar.setObjectName("progressBar")
        return progress_bar

    @staticmethod
    def create_label(x, y, weight, height, text, keyboard_simulator_window):
        label = QtWidgets.QLabel(keyboard_simulator_window)
        label.setGeometry(QtCore.QRect(x, y, weight, height))
        label.setTextFormat(QtCore.Qt.AutoText)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName('label' + text)
        label.setText(text)
        return label

    @staticmethod
    def create_line_label(keyboard_simulator_window):
        line_label = QtWidgets.QLabel(keyboard_simulator_window)
        line_label.setGeometry(QtCore.QRect(110, 300, 810, 40))
        line_label.setObjectName("line_label")
        line_label.setStyleSheet("border: 1px solid black;")
        return line_label

    @staticmethod
    def create_text_label(keyboard_simulator_window):
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
