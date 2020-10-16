import copy
import unittest
import time

from simulator_logic.basic_logic import Simulator


class SimulatorTest(unittest.TestCase):
    def setUp(self):
        self.simulator = Simulator(None, for_test=True)

    def test_calculate_number_of_symbols_in_last_second_usual_situation(self):
        current_time = time.perf_counter_ns()
        nanoseconds_per_second = 1000000000
        key_press_time = [
            current_time - 4 * nanoseconds_per_second,
            current_time - 3.5 * nanoseconds_per_second,
            current_time - 3 * nanoseconds_per_second,
            current_time - 2.5 * nanoseconds_per_second,
            current_time - 2 * nanoseconds_per_second,
            current_time - 1 * nanoseconds_per_second,
            current_time + 1 * nanoseconds_per_second,
            current_time + 2 * nanoseconds_per_second,
        ]
        self.simulator.key_press_time = copy.copy(key_press_time)
        self.assertEqual(2, self.simulator.calculate_number_of_symbols_in_last_second())
        self.assertEqual(key_press_time[6:], self.simulator.key_press_time)

    def test_calculate_number_of_symbols_in_last_second_unusual_situation(self):
        current_time = time.perf_counter_ns()
        nanoseconds_per_second = 1000000000
        key_press_time = [
            current_time - 4 * nanoseconds_per_second,
            current_time - 3.5 * nanoseconds_per_second
        ]
        self.simulator.key_press_time = copy.copy(key_press_time)
        self.assertEqual(0, self.simulator.calculate_number_of_symbols_in_last_second())
        self.assertEqual([], self.simulator.key_press_time)


if __name__ == '__main__':
    unittest.main()
