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


if __name__ == '__main__':
    unittest.main()
