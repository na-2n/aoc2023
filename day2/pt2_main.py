if __name__ == '__main__':
    ans = 0

    with open('./input.txt', 'r') as f:
        for line in f:
            name, data = line.strip().split(':')
            id = int(name.split(' ')[1])
            games = [game.strip().split(',') for game in data.strip().split(';')]

            max_r = 0
            max_g = 0
            max_b = 0

            for cubes in games:
                for cube in cubes:
                    val, name = cube.strip().split(' ')

                    if name == 'red':
                        max_r = max(max_r, int(val))
                    elif name == 'green':
                        max_g = max(max_g, int(val))
                    elif name == 'blue':
                        max_b = max(max_b, int(val))
                    else:
                        print('invalid name')

            pow = max_r * max_g * max_b
            print(f'id={id} r={max_r} g={max_g} b={max_b} pow={pow} \t{line.strip()}')
            ans += pow

    print(ans)

