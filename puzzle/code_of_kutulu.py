import sys
import math

# Survive the wrath of Kutulu
# Coded fearlessly by JohnnyYuge & nmahoude (ok we might have been a bit scared by the old god...but don't say anything)

width = int(input())
height = int(input())

set_all_available_space = set()
set_all_spawns = set()
set_all_walls = set()

delay = 0

is_first = True

for y in range(height):
    line = input()
    print(line, file=sys.stderr, flush=True)

    for x, value in enumerate(line):

        if value == '#':
            set_all_walls.add((x, y))
        elif value == '.':
            set_all_available_space.add((x,y))
        elif value == 'w':
            set_all_available_space.add((x,y))

# sanity_loss_lonely: how much sanity you lose every turn when alone, always 3 until wood 1
# sanity_loss_group: how much sanity you lose every turn when near another player, always 1 until wood 1
# wanderer_spawn_time: how many turns the wanderer take to spawn, always 3 until wood 1
# wanderer_life_time: how many turns the wanderer is on map after spawning, always 40 until wood 1
sanity_loss_lonely, sanity_loss_group, wanderer_spawn_time, wanderer_life_time = [int(i) for i in input().split()]

print("*-*-", file=sys.stderr, flush=True)

def verify_mov(x : int, y : int, all_available_space : set):
    if (x, y) in all_available_space:
        print(f"Valid: {x}, {y}", file=sys.stderr, flush=True)
        return True
    else:
        print(f"Invalid: {x}, {y}", file=sys.stderr, flush=True)
        return False

def fix_mov(x : int, y : int, cant_go : str, all_available_space : set):

    if cant_go != 'right' and verify_mov(x+1, y, all_available_space): # right
        print("Fixed: right", file=sys.stderr, flush=True)
        return (x+1, y, True)

    elif cant_go != 'left' and verify_mov(x-1, y, all_available_space): # left
        print("Fixed: left", file=sys.stderr, flush=True)
        return (x-1, y, True)
    
    elif cant_go != 'down' and verify_mov(x, y+1, all_available_space): # down
        print("Fixed: down", file=sys.stderr, flush=True)
        return (x, y+1, True)
    
    elif cant_go != 'up' and verify_mov(x, y-1, all_available_space): # up
        print("Fixed: up", file=sys.stderr, flush=True)
        return (x, y-1, True)
    
    else:
        print("Fixed: No valid option", file=sys.stderr, flush=True)
        return (x, y, True)

def verify_fix_isolated(list_explorers, my_pos):
    near_explorer = 0, 0
    is_isolated = True
    is_first = True
    for explorer in list_explorers:
        diff_x, diff_y = my_pos[0] - explorer['pos'][0], my_pos[1] - explorer['pos'][1]
        diff_x_near, diff_y_near = my_pos[0] - near_explorer[0], my_pos[1] - near_explorer[1]
        if abs(diff_x) < 1 and abs(diff_y) < 1:
            is_isolated = False
            near_explorer = 0, 0
            break
        elif is_first or abs(diff_x) + abs(diff_y) < abs(diff_x_near) + abs(diff_y_near):
            is_first = False
            near_explorer = explorer['pos'][0], explorer['pos'][1]
    
    return is_isolated, near_explorer

# game loop
while True:

    entity_count = int(input())  # the first given entity corresponds to your explorer
    param_mov = (0, 0, False) # x, y, Move or no
    valid_light = False
    list_explorers = []

    for i in range(entity_count):

        inputs = input().split()
        print(f"entity: {inputs}", file=sys.stderr, flush=True)
        entity_type = inputs[0]
        _id = int(inputs[1])
        x = int(inputs[2])
        y = int(inputs[3])
        param_0 = int(inputs[4])
        param_1 = int(inputs[5])
        param_2 = int(inputs[6])
        

        if i == 0:
            my_pos = (x, y)
            health = param_0
            plains = param_1
            lights = param_2
        
        elif entity_type == 'EXPLORER':
            list_explorers.append(
                {
                    'id': _id,
                    'pos': (x, y),
                    
                }
            )

        if entity_type == 'WANDERER':
            #if param_2 in ids_worry:
            diff_x, diff_y = my_pos[0]-x, my_pos[1]-y

            if abs(diff_x) <= 2 and abs(diff_y) <= 2:
                valid_light = True

            if abs(diff_x) <= 1 and abs(diff_y) <= 1 and (diff_x == 0 or diff_y == 0):
                print("Danger", file=sys.stderr, flush=True)
                if diff_x > 0:
                    
                    if verify_mov(my_pos[0]+1, my_pos[1], set_all_available_space):
                        param_mov = (my_pos[0]+1, my_pos[1], True)
                    else:
                        param_mov = fix_mov(my_pos[0], my_pos[1], 'left', set_all_available_space)
                
                elif diff_x < 0:
                    
                    if verify_mov(my_pos[0]-1, my_pos[1], set_all_available_space):
                        param_mov = (my_pos[0]-1, my_pos[1], True)
                    else:
                        param_mov = fix_mov(my_pos[0], my_pos[1], 'right', set_all_available_space)
                
                elif diff_y > 0:
                    
                    if verify_mov(my_pos[0], my_pos[1]+1, set_all_available_space):
                        param_mov = (my_pos[0], my_pos[1]+1, True)
                    else:
                        param_mov = fix_mov(my_pos[0], my_pos[1], 'down', set_all_available_space)
                
                elif diff_y < 0:
                    
                    if verify_mov(my_pos[0], my_pos[1]-1, set_all_available_space):
                        param_mov = (my_pos[0], my_pos[1]-1, True)
                    else:
                        param_mov = fix_mov(my_pos[0], my_pos[1], 'up', set_all_available_space)


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    is_isolated, near_explorer = verify_fix_isolated(list_explorers=list_explorers, my_pos=my_pos)

    print(f'is_isolated: {is_isolated}', file=sys.stderr, flush=True)
    print(f'near_explorer: {near_explorer}', file=sys.stderr, flush=True)

    if is_isolated:
        print(f'MOVE {near_explorer[0]} {near_explorer[1]}')
    elif param_mov[2]:
        print(f'MOVE {param_mov[0]} {param_mov[1]}')
    elif delay:
        delay -= 1
        print("WAIT")
    else:
        if lights > 0 or plains > 0:
            if plains > 0 and health < 100:
                print('PLAN')
                delay += 4
            elif lights > 0 and valid_light:
                print('LIGHT')
                delay += 2
            else:
                print("WAIT")    
        else:
            print("WAIT")
