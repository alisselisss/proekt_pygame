level_1_dict = {'level_map': 'map_1.map',
                'surface': 'ground.jpg',
                'beautiful_surface': 'grass.png',
                'back': 'back123.jpg'}
level_2_dict = {'level_map': 'map_2.map',
                'surface': 'ground.jpg',
                'beautiful_surface': 'grass.png',
                'back': 'back123.png'}
level_3_dict = {'level_map': 'map_3.map',
                'surface': 'ground.jpg',
                'beautiful_surface': 'grass.png',
                'back': 'back123.png'}
level_4_dict = {'level_map': 'map_4.map',
                'surface': 'ground.jpg',
                'beautiful_surface': 'grass.png',
                'back': 'back123.jpg'}
level_5_dict = {'level_map': 'map_5.map',
                'surface': 'ground.jpg',
                'beautiful_surface': 'grass.png',
                'back': 'back123.jpg'}
level_6_dict = {'level_map': 'map_6.map',
                'surface': 'ground.jpg',
                'beautiful_surface': 'grass.png',
                'back': 'back123.jpg'}
level_7_dict = {'level_map': 'map_7.map',
                'surface': 'ground.jpg',
                'beautiful_surface': 'grass.png',
                'back': 'back123.jpg'}
level_8_dict = {'level_map': 'map_8.map',
                'surface': 'ground.jpg',
                'beautiful_surface': 'grass.png',
                'back': 'back123.jpg'}
level_9_dict = {'level_map': 'map_9.map',
                'surface': 'ground.jpg',
                'beautiful_surface': 'grass.png',
                'back': 'back123.jpg'}
level_10_dict = {'level_map': 'map_10.map',
                 'surface': 'ground.jpg',
                 'beautiful_surface': 'grass.png',
                 'back': 'back123.jpg'}

progress_dict = {'player_coins': 0,
                 'hero_1': 1, 'hero_2': 0, 'hero_3': 0, 'hero_4': 0,
                 'level_1': 1, 'level_2': 2, 'level_3': 3, 'level_4': 0, 'level_5': 0,
                 'level_6': 0, 'level_7': 0, 'level_8': 0, 'level_9': 0, 'level_10': 0}


def load_progress():
    global progress_dict

    file = open('progress.txt')
    text = file.read().splitlines()
    for i in text:
        key = i[:i.find('=') - 1]
        progress_dict[key] = int(i[i.find('=') + 2:])
    file.close()


def write_progress():
    global progress_dict

    file = open('progress.txt', 'w')
    for key, val in progress_dict.items():
        file.write(f'{key} = {val}\n')
    file.close()