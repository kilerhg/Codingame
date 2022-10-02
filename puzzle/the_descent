import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.
# https://www.codingame.com/training/easy/the-descent

# game loop
while True:
    mountains = []
    for i in range(8):
        mountains.append((i,int(input()))) # represents the height of one mountain.)
    #print(mountains, file=sys.stderr, flush=True)
    mountains.sort(key=lambda x: x[1])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    #print(mountains, file=sys.stderr, flush=True)
    # The index of the mountain to fire on.
    print(mountains[-1][0])
