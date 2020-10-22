from collections import Counter
import math


class StatisticCalculating:
    @staticmethod
    def get_count_the_number_of_repetitions(data: list) -> dict:
        rounded_data = [round(number) for number in data]
        number_of_characters_per_second = Counter(rounded_data)
        sorted_data_for_statistic \
            = dict(sorted(number_of_characters_per_second.items()))
        return sorted_data_for_statistic

    @staticmethod
    def calculate_data_based_on_the_interval(
            number_of_characters_per_second: dict, interval: int) -> dict:
        if interval == 0:
            return number_of_characters_per_second
        number_of_characters_per_interval = {}
        is_first = True
        multiple_interval = interval
        for time in number_of_characters_per_second.keys():
            if is_first:
                number_of_characters_per_interval[multiple_interval] \
                    = number_of_characters_per_second[time]
                is_first = False
                continue
            if time <= multiple_interval:
                number_of_characters_per_interval[multiple_interval] \
                    += number_of_characters_per_second[time]
            else:
                nearest_multiplicity = math.ceil(time / interval)
                multiple_interval = nearest_multiplicity * interval
                number_of_characters_per_interval[multiple_interval] \
                    = number_of_characters_per_second[time]
        return number_of_characters_per_interval

    @staticmethod
    def get_fast_typing_string(
            text: str, number_of_characters_per_interval: dict):
        data = {}
        start_index = 0
        end_index = 0
        prev_time = 0
        for key in number_of_characters_per_interval.keys():
            data[(prev_time, key)] = {}
            end_index += number_of_characters_per_interval[key]
            data[(prev_time, key)]['line'] = text[start_index:end_index]
            start_index = end_index
            data[(prev_time, key)]['score'] = number_of_characters_per_interval[key]
            prev_time = key
        return data
