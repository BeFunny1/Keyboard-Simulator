class WorkWithText:
    def __init__(self):
        pass

    @staticmethod
    def read_file(file: str):
        with open('./texts/' + file, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    @staticmethod
    def split(line: str):
        symbols = [char for char in line]
        symbols.reverse()
        return symbols


if __name__ == '__main__':
    pass
