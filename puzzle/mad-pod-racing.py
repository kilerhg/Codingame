import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop

has_boost = True

while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    max_x, max_y = 16000, 9000
    total_units = max_x + max_y
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    
    #power = 100

    # if abs(next_checkpoint_angle) >= 0:
    power = int((1 - (abs(next_checkpoint_angle)/179)) * 100)

    if has_boost and abs(next_checkpoint_angle) <= 5 and next_checkpoint_dist >= total_units / 5:
        power = 'BOOST'
        has_boost = False


    
   
    print(total_units / 4, file=sys.stderr, flush=True)
    print(next_checkpoint_dist, file=sys.stderr, flush=True)
    print(next_checkpoint_angle, file=sys.stderr, flush=True)

    print(power, file=sys.stderr, flush=True)
    print(has_boost, file=sys.stderr, flush=True)

    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + f" {power}")
