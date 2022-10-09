import sys
import math

# Save humans, destroy zombies!

def most_in_danger_human(list_humans, list_zombies, my_pos):
    cord_human = (0, 0)
    lower_units = 0
    is_first = True

    for human in list_humans:
        print('', file=sys.stderr, flush=True)
        x_h, y_h = human[1], human[2]
        diff_ash_x, diff_ash_y = x_h - my_pos[0], y_h - my_pos[1]
        dead = False
        for zombie in list_zombies:
            x_z, y_z = zombie[1], zombie[2]
            diff_x, diff_y = x_h - x_z, y_h - y_z
            total_units_zombie = abs(diff_x) + abs(diff_y)
            total_units_ash = abs(diff_ash_x) + abs(diff_ash_y)
            is_save_possible = total_units_zombie >= 400 or total_units_ash <= 4000
            print(f"is_save_possible:{is_save_possible}", file=sys.stderr, flush=True)
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
                '''elif total_units_zombie <= lower_units:
                    lower_units = total_units_zombie
                    cord_human = (x_h, y_h)
                    print(f"new_lower: normal - cord_human:{cord_human}", file=sys.stderr, flush=True)'''
            else:
                dead = True
    return cord_human


# game loop
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

    cord_human = most_in_danger_human(list_humans=list_humans, list_zombies=list_zombies, my_pos=my_pos)
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Your destination coordinates
    print(f'{cord_human[0]} {cord_human[1]}')
