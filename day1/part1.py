import typing
from rich import print


def process_depth_measurement_increase():
    depth_list = [int(line) for line in open("input.txt", "r")]
    increase_incr = lambda t: 1 if t[1] > t[0] else 0
    result = sum(map(increase_incr, zip(depth_list, depth_list[1:])))
    print(result)

if __name__ == '__main__':
    process_depth_measurement_increase()


