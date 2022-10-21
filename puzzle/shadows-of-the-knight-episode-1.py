# https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1

import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]

def calculate_guess(possible_range):
    x = (possible_range[0][0] + possible_range[1][0]) // 2
    y = (possible_range[0][1] + possible_range[1][1]) // 2
    return x, y

possible_range = [[], []] # [(x_start, y_start), (x_end, y_end)]
# game loop
min_x = min_y = 0
max_x, max_y = w-1, h-1
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print(f'bomb_dir: {bomb_dir}', file=sys.stderr, flush=True)
    if bomb_dir == 'U':
        possible_range = [[x, y-1], [x, min_y]]
        max_x = min_x = x
        max_y = y-1
    elif bomb_dir == 'UR':
        possible_range = [[x+1, y-1], [max_x, min_y]]
        min_x = x+1
        max_y = y-1
    elif bomb_dir == 'R':
        possible_range = [[x+1, y], [max_x, y]]
        min_x = x+1
        min_y = max_y = y
    elif bomb_dir == 'DR':
        possible_range = [[x+1, y+1], [max_x, max_y]]
        min_x = x+1
        min_y = y+1
    elif bomb_dir == 'D':
        possible_range = [[x, y+1], [x, max_y]]
        max_x = min_x = x
        min_y = y+1
    elif bomb_dir == 'DL':
        possible_range = [[x-1, y+1], [min_x, max_y]]
        max_x = x-1
        min_y = y+1
    elif bomb_dir == 'L':
        possible_range = [[x-1, y], [min_x, y]]
        max_x = x-1
        min_y = max_y = y
    elif bomb_dir == 'UL':
        possible_range = [[x-1, y-1], [min_x, min_y]]
        max_x = x-1
        max_y = y-1

    x, y = calculate_guess(possible_range=possible_range)   

    print(f'possible_range: {possible_range}', file=sys.stderr, flush=True)
    print(f'possible_range: {possible_range}', file=sys.stderr, flush=True)
    print(f'x: {x} y: {y}', file=sys.stderr, flush=True)
    print(f'min_x: {min_x} min_y: {min_y}', file=sys.stderr, flush=True)
    print(f'max_x: {max_x} max_y: {max_y}', file=sys.stderr, flush=True)
    


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    print(f"{x} {y}")
