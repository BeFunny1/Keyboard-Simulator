class WorkWithText:
    @staticmethod
    def read_file(file: str) -> str:
        with open('./texts/' + file, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    @staticmethod
    def split(line: str) -> list:
        symbols = list(line)
        symbols.reverse()
        return symbols


if __name__ == '__main__':
    pass
