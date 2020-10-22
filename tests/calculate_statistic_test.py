import unittest
from simulator_logic.calculate_statistic import StatisticCalculating


class StatisticCalculatingTest(unittest.TestCase):
    def setUp(self):
        self.calculator = StatisticCalculating()

    def test_count_the_number_of_repetitions_usual_situation(self):
        data = [0.8192694187164307, 1.0271663665771484,
                1.6676995754241943, 1.7946839332580566, 1.9507570266723633,
                5.641010999679565, 5.805948495864868, 6.0302817821502686,
                7.727970123291016, 7.805712461471558, 7.956776857376099, 8.084296226501465, 8.309312105178833,
                10.6707435131073, 10.600067710876465, 10.656843423843384]
        answer = {1: 2, 2: 3, 6: 3, 8: 5, 11: 3}
        count_the_number_of_repetitions = self.calculator.get_count_the_number_of_repetitions(data)
        self.assertEqual(answer, count_the_number_of_repetitions)

    def test_count_the_number_of_repetitions_one_element_on_list(self):
        data = [0.8192694187164307]
        answer = {1: 1}
        count_the_number_of_repetitions = self.calculator.get_count_the_number_of_repetitions(data)
        self.assertEqual(answer, count_the_number_of_repetitions)

    def test_calculate_data_based_on_the_interval_without_interval(self):
        data = {1: 2, 2: 3, 6: 3, 8: 5, 11: 3}
        interval = 0
        answer = {1: 2, 2: 3, 6: 3, 8: 5, 11: 3}
        number_of_characters_per_interval = self.calculator.calculate_data_based_on_the_interval(data, interval)
        self.assertEqual(answer, number_of_characters_per_interval)

    def test_calculate_data_based_on_the_interval_usual_situation(self):
        data = {1: 2, 2: 3, 6: 3, 8: 5, 11: 3}
        interval = 3
        answer = {3: 5, 6: 3, 9: 5, 12: 3}
        number_of_characters_per_interval = self.calculator.calculate_data_based_on_the_interval(data, interval)
        self.assertEqual(answer, number_of_characters_per_interval)

    def test_calculate_data_based_on_the_interval_small_interval(self):
        data = {1: 2, 2: 3, 6: 3, 8: 5, 11: 3}
        interval = 1
        answer = {1: 2, 2: 3, 6: 3, 8: 5, 11: 3}
        number_of_characters_per_interval = self.calculator.calculate_data_based_on_the_interval(data, interval)
        self.assertEqual(answer, number_of_characters_per_interval)

    def test_calculate_data_based_on_the_interval_big_interval(self):
        data = {1: 2, 2: 3, 6: 3, 8: 5, 11: 3}
        interval = 12
        answer = {12: 16}
        number_of_characters_per_interval = self.calculator.calculate_data_based_on_the_interval(data, interval)
        self.assertEqual(answer, number_of_characters_per_interval)

    def test_get_fast_typing_string_usual_situation(self):
        line = 'VOTETO15SYMBOLS'
        number_of_characters_per_interval = {1: 2, 2: 3, 6: 3, 8: 5, 11: 2}
        answer = {
            (0, 1): {
                'line': 'VO',
                'score': 2
            },
            (1, 2): {
                'line': 'TET',
                'score': 3
            },
            (2, 6): {
                'line': 'O15',
                'score': 3
            },
            (6, 8): {
                'line': 'SYMBO',
                'score': 5
            },
            (8, 11): {
                'line': 'LS',
                'score': 2
            }
        }
        data = self.calculator.get_fast_typing_string(
            line, number_of_characters_per_interval)
        self.assertEqual(answer, data)


if __name__ == '__main__':
    unittest.main()
