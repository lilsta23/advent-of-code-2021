from dataclasses import dataclass
from rich import print


@dataclass
class Position:
    x: int
    y: int


def parse_movement() -> Position:
    """Reads an input file and calculates the final x and y position depending on the 'movements' encapsulated in
    the file."""
    movement_ops = open("input.txt", "r")
    pos: Position = Position(0, 0)
    # iterate through lines and change x or y depending on movement type.
    for op in movement_ops:
        movement, value = op.split()
        if movement == "forward":
            pos.x += int(value)
            continue
        if movement == "up":
            pos.y -= int(value)
            continue
        if movement == "down":
            pos.y += int(value)
            continue
        raise Exception(f"movement: {movement} is not recognised.")
    return pos


def parse_and_calculate_final_pos() -> None:
    pos: Position = parse_movement()
    depth_x_horizontal = pos.x * pos.y
    print(f"depth x horizontal: {depth_x_horizontal}")


if __name__ == "__main__":
    parse_and_calculate_final_pos()
