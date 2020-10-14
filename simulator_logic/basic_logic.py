from simulator_logic.work_with_text import WorkWithText


class Simulator:
    def __init__(self, user_interface):
        self.window = user_interface

        worker = WorkWithText()
        self.text = worker.read_file('text1.txt')
        self.symbols = worker.split(self.text)

        self.current_symbols = self.symbols.pop()
        self.current_line = ''

        self.progress = 0
        self.number_of_entered_characters = 0
        self.number_of_invalid_characters = 0
        self.accuracy = 100

        self.index = 0
        self.update_text()
        self.preparation()

    def preparation(self):
        self.window.point_to_the_button(self.current_symbols.upper())

    def activity(self, key, number_key):
        # Tab, Shift, Caps Lock, Ctrl, Alt, Win, Enter, Backspace
        numbers_unaccountable_characters = [
            16777217, 16777248, 16777252, 16777249,
            16777251, 16777250, 16777220, 16777219]
        if key == self.current_symbols:
            self.current_line += self.current_symbols
            self.update_line(self.current_line)
            if len(self.symbols) != 0:
                self.current_symbols = self.symbols.pop()
                self.window.point_to_the_button(self.current_symbols.upper())
                self.index += 1
            else:
                self.window.point_to_the_button('')
            self.number_of_entered_characters += 1
            self.update_statistic_data()
            self.update_text()

        elif number_key not in numbers_unaccountable_characters:
            self.number_of_invalid_characters += 1
            self.update_statistic_data()
        if len(self.current_line) == 126:
            self.current_line = ''
            self.update_line(self.current_line)

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
