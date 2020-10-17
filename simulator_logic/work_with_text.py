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

    @staticmethod
    def split_string_into_substrings(string: str, max_line_length: int) -> list:
        substrings = []
        separators = [',', '.', ' ', ';', '?', '!']
        while True:
            if len(string) > max_line_length:
                indexes = []
                for separator in separators:
                    indexes.append(string[:max_line_length].rfind(separator))
                max_index_separator = max(indexes)
                if max_index_separator != -1:
                    substrings.append(string[:max_index_separator + 1])
                    string = string[max_index_separator + 1:]
                else:
                    substrings.append(string[:max_line_length])
                    string = string[max_line_length:]
            else:
                break
        substrings.append(string)
        return substrings


if __name__ == '__main__':
    pass
