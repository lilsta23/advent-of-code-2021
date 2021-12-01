import typing
from rich import print


def process_depth_measurement_increase_sliding_window():
    depth_list = [int(line) for line in open("input.txt", "r")]

    sliding_window_list = list(zip(depth_list, depth_list[1:], depth_list[2:]))

    result = sum(
        map(
            lambda window_a, window_b: 1 if sum(window_b) > sum(window_a) else 0,
            sliding_window_list,
            sliding_window_list[1:],
        )
    )
    print(result)


if __name__ == "__main__":
    process_depth_measurement_increase_sliding_window()
