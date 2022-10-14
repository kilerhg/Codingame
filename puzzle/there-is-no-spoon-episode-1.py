# https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1

import sys

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
print(f"width: {width}", file=sys.stderr, flush=True)
print(f"height: {height}", file=sys.stderr, flush=True)
list_lines = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    list_lines.append(line)

for y, line in enumerate(list_lines):
    for x, v in enumerate(line):
            if v == '0':
                print((x,y), file=sys.stderr, flush=True)
                value = f'{x} {y}'
                right = left = ' -1 -1'
                for i in range(1, width):
                    if x+i <= width-1 and line[x+i] == '0':
                        print("found right", file=sys.stderr, flush=True)
                        right = f' {x+i} {y}'
                        break
                for i in range(1, height):
                    if y+i <= height-1 and list_lines[y+i][x] == '0':
                        print("found down", file=sys.stderr, flush=True)
                        left = f' {x} {y+i}'
                        break
                print(value + right + left)
