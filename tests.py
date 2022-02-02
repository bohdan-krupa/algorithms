from circular_printer import getTime
from merge_intervals import get_merged_intervals


class TestClass:
    def test_get_time(self):
        mocks = (
            ('ZYAFVBNFGMWIFGSB', 99), ('ZYAFVBNF', 45), ('B', 1), ('HJDTZ', 31),
            ('PNQZJ', 35), ('PPERBBQLDYEN', 89), ('ETFAZ', 33), ('BAZYGEJ', 19)
        )

        for mock in mocks:
            assert getTime(mock[0]) == mock[1]


    def test_get_merged_intervals(self):
        mocks = (
            (
                [[1, 2], [17, 22], [7, 7], [25, 28], [15, 20], [2, 3], [27, 30], [6, 11]],
                [[1, 3], [6, 11], [15, 22], [25, 30]]
            ),
            (
                [[7, 7], [2, 3], [6, 11], [1, 2]],
                [[1, 3], [6, 11]]
            ),
            (
                [[20, 30], [22, 22], [14, 20], [14, 32], [1, 10]],
                [[1, 10], [14, 32]]
            )
        )

        for mock in mocks:
            assert get_merged_intervals(mock[0]) == mock[1]
