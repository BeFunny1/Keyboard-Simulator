from PyQt5 import QtCore, QtWidgets


class WindowKeyboard(object):
    def __init__(self):
        pass
        # self.buttons = self.create_buttons()

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
            'Space': [280, 590, 470, 50],
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

    def create_buttons(self):
        data = self.get_data_for_buttons()
        buttons = {}
        for key in data.keys():
            button = QtWidgets.QPushButton(self.keyboard_window)
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
        return button

    @staticmethod
    def get_data_for_labels():
        labels = {
            'Знаки:': '0', 'Слов в минуту:': '0',
            'Ошибки:': '0', 'Точность:': '100%',
            'Время:': '0:00', 'Прогресс:': ''
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

    def create_labels_and_his_related_element(self):
        data = self.get_data_for_labels()
        labels_and_related_items = {}
        for key in data.keys():
            label = self.create_label(
                data[key]['x'], data[key]['y'],
                data[key]['weight'], data[key]['height'], key)
            data_about_related_item = data[key]['related_item']
            if key != 'Прогресс:':
                related_item = self.create_label(
                    data_about_related_item['x'],
                    data_about_related_item['y'],
                    data_about_related_item['weight'],
                    data_about_related_item['height'],
                    data_about_related_item['text']
                )
            else:
                progress_bar = QtWidgets.QProgressBar(self.keyboard_window)
                progress_bar.setGeometry(QtCore.QRect(
                    data_about_related_item['x'], data_about_related_item['y'],
                    data_about_related_item['weight'], data_about_related_item['height']
                ))
                progress_bar.setProperty("value", 100)
                progress_bar.setObjectName("progressBar")
                related_item = progress_bar
            labels_and_related_items[key] = {}
            labels_and_related_items[key]['label'] = label
            labels_and_related_items[key]['related_item'] = related_item
        return labels_and_related_items

    def create_label(self, x, y, weight, height, text):
        label = QtWidgets.QLabel(self.keyboard_window)
        label.setGeometry(QtCore.QRect(x, y, weight, height))
        label.setTextFormat(QtCore.Qt.AutoText)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName('label' + text)
        label.setText(text)
        return label

    def setupUi(self, keyboard_window):
        self.keyboard_window = keyboard_window
        buttons = self.create_buttons()
        labels = self.create_labels_and_his_related_element()
        self.keyboard_window.setObjectName("KeyboardSimulator")
        self.keyboard_window.setEnabled(True)
        self.keyboard_window.resize(1024, 768)
        self.keyboard_window.setMinimumSize(QtCore.QSize(1024, 768))
        self.keyboard_window.setMaximumSize(QtCore.QSize(1024, 768))
        self.keyboard_window.setBaseSize(QtCore.QSize(1024, 768))
        self.keyboard_window.setAutoFillBackground(False)
        self.keyboard_window.setSizeGripEnabled(False)
        self.keyboard_window.setModal(False)
        self.lineEdit = QtWidgets.QLineEdit(self.keyboard_window)
        self.lineEdit.setGeometry(QtCore.QRect(110, 250, 811, 91))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.keyboard_window)
        self.textBrowser.setGeometry(QtCore.QRect(110, 201, 811, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(self.keyboard_window)
        self.line.setGeometry(QtCore.QRect(180, 150, 90, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.keyboard_window)
        self.line_2.setGeometry(QtCore.QRect(330, 150, 510, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(self.keyboard_window)
        QtCore.QMetaObject.connectSlotsByName(self.keyboard_window)

    def retranslateUi(self, KeyboardSimulator):
        _translate = QtCore.QCoreApplication.translate
        KeyboardSimulator.setWindowTitle(_translate("KeyboardSimulator", "Клавиатурный тренажёр"))
