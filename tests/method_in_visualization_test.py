import unittest

from visualization.simulator_visualizer import MainWindowKeyboard


class VisualizationTest(unittest.TestCase):
    def setUp(self):
        self.window = MainWindowKeyboard(for_test=True)

    def test_get_data_for_buttons(self):
        data = self.window.get_data_for_buttons()
        answer = {
            'Ё': {'x': 90, 'y': 350, 'weight': 50, 'height': 50},
            '1': {'x': 150, 'y': 350, 'weight': 50, 'height': 50},
            '2': {'x': 210, 'y': 350, 'weight': 50, 'height': 50},
            '3': {'x': 270, 'y': 350, 'weight': 50, 'height': 50},
            '4': {'x': 330, 'y': 350, 'weight': 50, 'height': 50},
            '5': {'x': 390, 'y': 350, 'weight': 50, 'height': 50},
            '6': {'x': 450, 'y': 350, 'weight': 50, 'height': 50},
            '7': {'x': 510, 'y': 350, 'weight': 50, 'height': 50},
            '8': {'x': 570, 'y': 350, 'weight': 50, 'height': 50},
            '9': {'x': 630, 'y': 350, 'weight': 50, 'height': 50},
            '0': {'x': 690, 'y': 350, 'weight': 50, 'height': 50},
            '-': {'x': 750, 'y': 350, 'weight': 50, 'height': 50},
            '=': {'x': 810, 'y': 350, 'weight': 50, 'height': 50},
            'Й': {'x': 170, 'y': 410, 'weight': 50, 'height': 50},
            'Ц': {'x': 230, 'y': 410, 'weight': 50, 'height': 50},
            'У': {'x': 290, 'y': 410, 'weight': 50, 'height': 50},
            'К': {'x': 350, 'y': 410, 'weight': 50, 'height': 50},
            'Е': {'x': 410, 'y': 410, 'weight': 50, 'height': 50},
            'Н': {'x': 470, 'y': 410, 'weight': 50, 'height': 50},
            'Г': {'x': 530, 'y': 410, 'weight': 50, 'height': 50},
            'Ш': {'x': 590, 'y': 410, 'weight': 50, 'height': 50},
            'Щ': {'x': 650, 'y': 410, 'weight': 50, 'height': 50},
            'З': {'x': 710, 'y': 410, 'weight': 50, 'height': 50},
            'Х': {'x': 770, 'y': 410, 'weight': 50, 'height': 50},
            'Ъ': {'x': 830, 'y': 410, 'weight': 50, 'height': 50},
            '\\': {'x': 890, 'y': 410, 'weight': 50, 'height': 50},
            'Ф': {'x': 190, 'y': 470, 'weight': 50, 'height': 50},
            'Ы': {'x': 250, 'y': 470, 'weight': 50, 'height': 50},
            'В': {'x': 310, 'y': 470, 'weight': 50, 'height': 50},
            'А': {'x': 370, 'y': 470, 'weight': 50, 'height': 50},
            'П': {'x': 430, 'y': 470, 'weight': 50, 'height': 50},
            'Р': {'x': 490, 'y': 470, 'weight': 50, 'height': 50},
            'О': {'x': 550, 'y': 470, 'weight': 50, 'height': 50},
            'Л': {'x': 610, 'y': 470, 'weight': 50, 'height': 50},
            'Д': {'x': 670, 'y': 470, 'weight': 50, 'height': 50},
            'Ж': {'x': 730, 'y': 470, 'weight': 50, 'height': 50},
            'Э': {'x': 790, 'y': 470, 'weight': 50, 'height': 50},
            'Я': {'x': 220, 'y': 530, 'weight': 50, 'height': 50},
            'Ч': {'x': 280, 'y': 530, 'weight': 50, 'height': 50},
            'С': {'x': 340, 'y': 530, 'weight': 50, 'height': 50},
            'М': {'x': 400, 'y': 530, 'weight': 50, 'height': 50},
            'И': {'x': 460, 'y': 530, 'weight': 50, 'height': 50},
            'Т': {'x': 520, 'y': 530, 'weight': 50, 'height': 50},
            'Ь': {'x': 580, 'y': 530, 'weight': 50, 'height': 50},
            'Б': {'x': 640, 'y': 530, 'weight': 50, 'height': 50},
            'Ю': {'x': 700, 'y': 530, 'weight': 50, 'height': 50},
            '.': {'x': 760, 'y': 530, 'weight': 50, 'height': 50},
            'Tab': {'x': 90, 'y': 410, 'weight': 70, 'height': 50},
            'Caps Lock': {'x': 90, 'y': 470, 'weight': 90, 'height': 50},
            'Shift_L': {'x': 90, 'y': 530, 'weight': 120, 'height': 50},
            ' ': {'x': 280, 'y': 590, 'weight': 470, 'height': 50},
            'Backspace': {'x': 870, 'y': 350, 'weight': 70, 'height': 50},
            'Enter': {'x': 850, 'y': 470, 'weight': 90, 'height': 50},
            'Shift_R': {'x': 820, 'y': 530, 'weight': 120, 'height': 50}
        }
        self.assertEqual(data, answer)

    def test_get_data_for_labels(self):
        data = self.window.get_data_for_labels()
        answer = {
            'Знаки:':
                {
                    'related_item': {
                        'text': '0', 'x': 240, 'weight': 90,
                        'y': 160, 'height': 20},
                    'x': 240, 'y': 130, 'weight': 90, 'height': 20},
            'Симв./мин.:':
                {
                    'related_item': {
                        'text': '0', 'x': 350, 'weight': 90,
                        'y': 160, 'height': 20},
                    'x': 350, 'y': 130, 'weight': 90, 'height': 20},
            'Ошибки:':
                {
                    'related_item': {
                        'text': '0', 'x': 460, 'weight': 90,
                        'y': 160, 'height': 20},
                    'x': 460, 'y': 130, 'weight': 90, 'height': 20},
            'Точность:':
                {
                    'related_item': {
                        'text': '100%', 'x': 570, 'weight': 90,
                        'y': 160, 'height': 20},
                    'x': 570, 'y': 130, 'weight': 90, 'height': 20},
            'Время:':
                {
                    'related_item': {
                        'text': '00:00:00', 'x': 680, 'weight': 90,
                        'y': 160, 'height': 20},
                    'x': 680, 'y': 130, 'weight': 90, 'height': 20},
            'Таймер:':
                {
                    'related_item': {
                        'text': '', 'x': 790, 'weight': 90,
                        'y': 160, 'height': 20},
                    'x': 790, 'y': 130, 'weight': 90, 'height': 20},
            'Прогресс:':
                {
                    'related_item': {
                        'text': '', 'x': 90, 'weight': 120,
                        'y': 160, 'height': 20},
                    'x': 100, 'y': 130, 'weight': 90, 'height': 20}
        }
        self.assertEqual(answer, data)

    def test_select_letter_in_text(self):
        line = 'abrakadabra'
        self.assertEqual(
            self.window.select_letter_in_text(line, 5),
            'abrak[a]dabra')


if __name__ == '__main__':
    unittest.main()
