from typing import List
import itertools


def get_merged_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()

    for interval in intervals:
        for sub_index, sub_interval in enumerate(intervals):
            if interval[0] in sub_interval or interval[1] in sub_interval or \
                    interval[0] <= sub_interval[0] <= interval[1]:

                merged_interval = [min(interval[0], sub_interval[0]), max(interval[1], sub_interval[1])]
                intervals.pop(sub_index)
                intervals.insert(sub_index, merged_interval)

    return [interval for interval, _ in itertools.groupby(intervals)]
