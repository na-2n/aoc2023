if __name__ == '__main__':
    ans = 0

    with open('./input.txt', 'r') as f:
        lines = f.readlines()
        t = int(lines[0].split(':')[1].replace(' ', ''))
        d = int(lines[1].split(':')[1].replace(' ', ''))

        # very slow but whatever
        c = len(list(filter(lambda x: x > d, [i*(t-i) for i in range(t)])))

        ans = c


    print(ans)

