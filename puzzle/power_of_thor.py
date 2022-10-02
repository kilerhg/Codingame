import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
current_tx, current_ty = initial_tx, initial_ty
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    diff_x, diff_y = light_x-current_tx, light_y-current_ty
    
    print(f"light_x: {light_x} - light_y: {light_y} ", file=sys.stderr, flush=True)
    print(f"diff_x: {diff_x} - diff_y: {diff_y} ", file=sys.stderr, flush=True)
    print(f"current_tx: {current_tx} - current_ty: {current_ty} ", file=sys.stderr, flush=True)
    
    # A single line providing the move to be made: N NE E SE S SW W or NW

    v = 0

    if diff_x > v:
        if diff_y > v:
            print('SE')
            current_tx += 1
            current_ty += 1
        elif diff_y < v:
            print("NE")
            current_tx += 1
            current_ty -= 1
        else:
            current_tx += 1
            print("E")
    elif diff_x < v:
        if diff_y > v:
            print('SW')
            current_tx -= 1
            current_ty += 1
        elif diff_y < v:
            print("NW")
            current_tx -= 1
            current_ty -= 1
        else:
            print("W")
            current_tx -= 1
    else:
        if diff_y > v:
            print('S')
            current_ty += 1
        elif diff_y < v:
            print("N")
            current_ty -= 1
