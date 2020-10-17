import unittest

from simulator_logic.work_with_text import WorkWithText


class WorkWithTextTest(unittest.TestCase):
    def setUp(self):
        self.worker = WorkWithText()

    def test_split_empty_line(self):
        line = ''
        self.assertEqual(self.worker.split(line), [])

    def test_split_correct_line(self):
        line = 'correct line'
        self.assertEqual(
            ['e', 'n', 'i', 'l', ' ', 't', 'c', 'e', 'r', 'r', 'o', 'c'],
            self.worker.split(line)
        )

    def test_split_string_into_substrings_small_str(self):
        string = 'abc'
        max_line_length = 10
        answer = self.worker.split_string_into_substrings(string, max_line_length)
        self.assertEqual(['abc'], answer)

    def test_split_string_into_substrings_str_more_max(self):
        string = 'abcdefg'
        max_line_length = 4
        answer = self.worker.split_string_into_substrings(string, max_line_length)
        self.assertEqual(['abcd', 'efg'], answer)

    def test_split_string_into_substrings_str_with_separator(self):
        string = 'abc defg'
        max_line_length = 4
        answer = self.worker.split_string_into_substrings(string, max_line_length)
        self.assertEqual(['abc ', 'defg'], answer)

    def test_split_string_into_substrings_str_normal_str(self):
        string = 'Он подошел к Анне Павловне, ' \
                 'поцеловал ее руку, подставив ' \
                 'ей свою надушенную и сияющую ' \
                 'лысину, и покойно уселся на диване.'
        max_line_length = 30
        answer = self.worker.split_string_into_substrings(string, max_line_length)
        self.assertEqual(
            ['Он подошел к Анне Павловне, ',
             'поцеловал ее руку, подставив ',
             'ей свою надушенную и сияющую ',
             'лысину, и покойно уселся на ',
             'диване.'], answer)


if __name__ == '__main__':
    unittest.main()
