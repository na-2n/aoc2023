def format_map(x):
    return [[int(z.strip()) for z in y.strip().split(' ')]
            for y in x.split(':')[1].strip().split('\n')]

if __name__ == '__main__':
    ans = 0

    with open('./input.txt', 'r') as f:
        d = f.read()
        s = d.split('\n\n')
        seeds = [int(x.strip()) for x in s[0].split(':')[1].strip().split(' ')]
        maps = [format_map(x) for x in s[1:]]

        nums = seeds
        next_buf = seeds

        print(seeds)
        print('----------------')

        for x in maps:
            for i, num in enumerate(nums):
                for dest, src, r in x:
                    if num >= src and num <= src + r:
                        tmp = num + (dest - src)
                        print(f'{num} -> {tmp}')
                        next_buf[i] = tmp
                        break
            print(next_buf)
            nums = next_buf

        print('----------------')
        print(nums)
        print('----------------')
        ans = sorted(nums)[0]

    print(ans)

