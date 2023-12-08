if __name__ == '__main__':
    ans = 0

    max_r = 12
    max_g = 13
    max_b = 14

    with open('./input.txt', 'r') as f:
        for line in f:
            name, data = line.strip().split(':')
            id = int(name.split(' ')[1])
            games = [game.strip().split(',') for game in data.strip().split(';')]

            p = True
            for cubes in games:
                r = 0
                g = 0
                b = 0

                for cube in cubes:
                    val, name = cube.strip().split(' ')

                    if name == 'red':
                        r = int(val)
                    elif name == 'green':
                        g = int(val)
                    elif name == 'blue':
                        b = int(val)
                    else:
                        print('invalid name')

                p = p and r <= max_r and g <= max_g and b <= max_b
                print(f'id={id}:{games.index(cubes)} r={r} g={g} b={b} \t{line.strip()}')
                if p:
                    print('OK')

            if p:
                ans += id

    print(ans)

