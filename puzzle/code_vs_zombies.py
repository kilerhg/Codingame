import sys
import math


# todo: calc to verify if possible save by dist

# Save humans, destroy zombies!

def zombies_to_human(list_humans, list_zombies):
    dict_zombie_to_human = {}
    
    for zombie in list_zombies:
        x_z, y_z = zombie[1], zombie[2]
        min_value = 100_000_000
        id_zombie = zombie[0]
        for human in list_humans:
            x_h, y_h = human[1], human[2]
            diff_x, diff_y = x_h - x_z, y_h - y_z
            total_units = abs(diff_x) + abs(diff_y)
            if total_units < min_value:
                id_human = human[0]
                min_value = total_units
        if id_human in dict_zombie_to_human:
            dict_zombie_to_human[id_human].append(id_zombie)
        else:
            dict_zombie_to_human[id_human] = [id_zombie]
    return dict_zombie_to_human


def most_in_danger_human(list_humans, list_zombies, my_pos, cord_human):
    
    lower_units = 100_000_000
    is_first = True

    dict_zombie_to_human = zombies_to_human(list_humans, list_zombies)
    print(f"dict_zombie_to_human:{dict_zombie_to_human}", file=sys.stderr, flush=True)
    
    for human in list_humans:
        print('', file=sys.stderr, flush=True)
        id_human = human[0]
        x_h, y_h = human[1], human[2]
        diff_ash_x, diff_ash_y = x_h - my_pos[0], y_h - my_pos[1]
        dead = False
        for zombie in list_zombies:
            id_zombie = zombie[0]
            if id_human in dict_zombie_to_human and id_zombie in dict_zombie_to_human[id_human]:
                x_z, y_z = zombie[3], zombie[4]
                diff_x, diff_y = x_h - x_z, y_h - y_z
                total_units_zombie = abs(diff_x) + abs(diff_y)
                total_units_ash = abs(diff_ash_x) + abs(diff_ash_y)
                is_save_possible = (total_units_zombie >= 400 or total_units_ash <= 3700) and total_units_ash/3000-total_units_zombie/400 <= 0.65
                print(f"is_save_possible:{is_save_possible}", file=sys.stderr, flush=True)
                print(f"test:{total_units_ash//3000-total_units_zombie//400}", file=sys.stderr, flush=True)
                print(f"test1:{total_units_ash-total_units_zombie}", file=sys.stderr, flush=True)
                print(f'human: {human[0]} - zombie {zombie[0]}', file=sys.stderr, flush=True)
                print(f"total_units_zombie:{total_units_zombie}", file=sys.stderr, flush=True)
                print(f"current min:{lower_units}", file=sys.stderr, flush=True)
                print(f"lower_units <= total_units_zombie:{lower_units <= total_units_zombie}", file=sys.stderr, flush=True)
                if is_save_possible and not dead:
                    if is_first:
                        is_first = False
                        lower_units = total_units_zombie
                        cord_human = (x_h, y_h)
                        print(f"x_h:{x_h} - x_h:{y_h}", file=sys.stderr, flush=True)
                        print(f"cord_human: {cord_human}", file=sys.stderr, flush=True)
                        print(f"new_lower: first - cord_human:{cord_human}", file=sys.stderr, flush=True)
                    elif total_units_zombie < lower_units:
                        lower_units = total_units_zombie
                        cord_human = (x_h, y_h)
                        print(f"new_lower: normal - cord_human:{cord_human}", file=sys.stderr, flush=True)
                else:
                    print(f'human: {human[0]} - zombie {zombie[0]}', file=sys.stderr, flush=True)
                    dead = True
    return cord_human


# game loop
cord_human = (0, 0)
while True:
    my_pos = [int(i) for i in input().split()]
    human_count = int(input())
    list_humans = []
    list_zombies = []
    list_priority = []
    
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        print("human", human_id, human_x, human_y, file=sys.stderr, flush=True)
        list_humans.append((human_id, human_x, human_y))
    
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        print("zombie", zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext, file=sys.stderr, flush=True)

        list_zombies.append((zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext))
    
    print("*-"*10, file=sys.stderr, flush=True)

    cord_human = most_in_danger_human(list_humans=list_humans, list_zombies=list_zombies, my_pos=my_pos, cord_human=cord_human)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Your destination coordinates
    print(f'{cord_human[0]} {cord_human[1]}')
