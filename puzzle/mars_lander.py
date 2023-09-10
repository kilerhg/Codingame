import sys
import math

# Save the Planet.
# Use less Fossil Fuel.

TOTAL_X = 7000
TOTAL_Y = 3000

MIN_SAFE_X = 20
MIN_SAFE_Y = 40


ACCEPTABLE_H_SPEED_LAND = 5

MAX_POWER = 4
MAX_ANGLE = 90

DEFAULT_ANGLE_NO_H_SPEED = 0
DEFAULT_ANGLE_WRONG_SIDE = 60
DEFAULT_ANGLE_FAR_AWAY = 55
DEFAULT_ANGLE_STOP_LANDING = 45

def find_landing_point(list_all_points : list) -> tuple:
    last_x = -1
    last_y = -1
    for item in list_all_points:
        if item[1] == last_y:
            start_landing_x = last_x
            end_landing_x = item[0]
            return (start_landing_x, end_landing_x, land_y, last_y)
        last_x, last_y = item


def get_diffs(x, y, mean_landing, land_y_plane, land_place_y) -> tuple:
    diff_x = x - mean_landing
    diff_y = y - land_y_plane
    diff_y_real = y - land_place_y
    return (diff_x, diff_y, diff_y_real)


def is_safe_to_land(vs, hs) -> tuple:
    is_safe_to_land_y = abs(vs) <= MIN_SAFE_Y
    is_safe_to_land_x = abs(hs) <= MIN_SAFE_X
    return (is_safe_to_land_y, is_safe_to_land_x)


def landing_mode(x, start_landing_x, end_landing_x, recommended_speed):
    on_landing_zone = (x >= start_landing_x and x <= end_landing_x)
    if on_landing_zone:
        recommended_speed = 18
    else:
        recommended_speed = recommended_speed
    return (on_landing_zone, recommended_speed)


def calculate_generic_angle(diff_x, max_angle):
    generic_angle = ((abs(diff_x) / TOTAL_X)*max_angle)
    generic_angle_neg = generic_angle*-1
    return (generic_angle, generic_angle_neg)


def calculate_max_angle(land_place_y, max_angle):
    if land_place_y/TOTAL_Y >= 0.6:
        print("Far away case", file=sys.stderr, flush=True)
        max_angle = DEFAULT_ANGLE_FAR_AWAY
    return max_angle

def calculate_all_angles(land_place_y, hs, diff_x, recommended_speed, max_angle):
    
    angle = DEFAULT_ANGLE_NO_H_SPEED
    
    max_angle = calculate_max_angle(land_place_y, max_angle)
    
    generic_angle, generic_angle_neg = calculate_generic_angle(diff_x, max_angle)

    if hs >= 0 and diff_x < 0:
        print("Correct Side, Turning right", file=sys.stderr, flush=True)
        if hs > recommended_speed:
            angle = generic_angle
        else:
            angle = generic_angle_neg

    elif hs <= 0 and diff_x > 0:
        print("Correct Side, Turning left", file=sys.stderr, flush=True)
        if hs < recommended_speed*-1:
            angle = generic_angle_neg
        else:
            angle = generic_angle
    
    elif hs >= 0 and diff_x > 0:
        print("Wrong Side, Turning left", file=sys.stderr, flush=True)
        angle = DEFAULT_ANGLE_WRONG_SIDE
    else:
        print("Wrong Side, Turning Right", file=sys.stderr, flush=True)
        angle = -DEFAULT_ANGLE_WRONG_SIDE
    
    return angle


def calculate_descent_vertical(diff_y, vs, power):
    if diff_y > 1100 or vs >= -(MIN_SAFE_Y-1):
        power = int(abs(diff_y/TOTAL_Y)*3)+1
    else:
        if vs < -MIN_SAFE_Y:
            power = MAX_POWER
        elif vs >= 0:
            power = 1
    return power


def calculate_stop_horizontal(hs, power):
    if hs >= ACCEPTABLE_H_SPEED_LAND:
        angle = DEFAULT_ANGLE_STOP_LANDING
        power = MAX_POWER
    elif hs <= -ACCEPTABLE_H_SPEED_LAND:
        angle = -DEFAULT_ANGLE_STOP_LANDING
        power = MAX_POWER
    else:
        angle = DEFAULT_ANGLE_NO_H_SPEED
    return (angle, power)


n = int(input())  # the number of points used to draw the surface of Mars.

list_all_points = []

for i in range(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    list_all_points.append((land_x, land_y))

start_landing_x, end_landing_x, land_y_plane, land_place_y = find_landing_point(list_all_points)

mean_landing = (start_landing_x + end_landing_x)/2

on_landing_zone = False

recommended_speed = 40

last_hs = 0

# game loop
while True:
    max_angle = MAX_ANGLE
    on_landing_zone = False
    # hs: the horizontal speed (in m/s), can be negative.
    # vs: the vertical speed (in m/s), can be negative.
    # f: the quantity of remaining fuel in liters.
    # r: the rotation angle in degrees (-90 to 90).
    # p: the thrust power (0 to 4).
    x, y, hs, vs, f, r, p = [int(i) for i in input().split()]

    diff_x, diff_y, diff_y_real = get_diffs(x, y, mean_landing, land_y_plane, land_place_y)

    is_safe_to_land_y, is_safe_to_land_x = is_safe_to_land(vs, hs)

    on_landing_zone, recommended_speed = landing_mode(x, start_landing_x, end_landing_x, recommended_speed)

    power = MAX_POWER
        
    if not on_landing_zone:

        angle = calculate_all_angles(land_place_y, hs, diff_x, recommended_speed, max_angle)
    
    else:
    
        power = calculate_descent_vertical(diff_y, vs, power)

        angle, power = calculate_stop_horizontal(hs, power)

    print(f"""
    diff_x: {diff_x}
    diff_y: {diff_y}
    diff_y_real: {diff_y_real}
    x: {x}
    y: {y}
    hs: {hs}
    hy: {vs}
    start_landing_x: {start_landing_x}
    end_landing_x: {end_landing_x}
    land_y_plane: {land_y_plane}
    angle: {angle}
    power: {power}
    on_landing_zone: {on_landing_zone}
    is_safe_to_land_y: {is_safe_to_land_y}
    is_safe_to_land_x: {is_safe_to_land_x}
    recommended_speed: {recommended_speed}
    land_place_y: {land_place_y}
    """, file=sys.stderr, flush=True)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # R P. R is the desired rotation angle. P is the desired thrust power.
    print(f"{int(angle)} {power}")