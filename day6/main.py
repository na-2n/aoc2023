if __name__ == '__main__':
    ans = 1

    with open('./input.txt', 'r') as f:
        lines = f.readlines()
        time = [int(x.strip()) for x in filter(lambda y: y != '', lines[0].split(':')[1].split(' '))]
        dist = [int(x.strip()) for x in filter(lambda y: y != '', lines[1].split(':')[1].split(' '))]

        for t, d in zip(time, dist):
            c = len(list(filter(lambda x: x > d, [i*(t-i) for i in range(t)])))

            ans *= c

    print(ans)

