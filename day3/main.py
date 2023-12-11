import math
import os
import sys

from typing import Tuple, List


def get_xy_f(max_x: int):
    def inner(i: int) -> Tuple[int, int]:
        return (i % max_x, math.floor(i / max_x))

    return inner

def get_i_f(max_x: int):
    def inner(coord: Tuple[int, int]) -> int:
        x, y = coord
        return y * max_x + x

    return inner

def check_bounds_f(max_x: int, max_y=sys.maxsize):
    def inner(coords: Tuple[int, int]) -> Tuple[int, int]:
        x, y = coords

        if x < 0:
            x = 0
        if x > max_x:
            x = max_x
        if y < 0:
            y = 0
        if y > max_y:
            y = max_y

        return (x, y)

    return inner


if __name__ == '__main__':
    ans = 0

    with open('./input.txt') as f:
        max_x = len(f.readline()) - 1
        f.seek(0, os.SEEK_SET)

        get_i = get_i_f(max_x)
        get_xy = get_xy_f(max_x)
        check_bounds = check_bounds_f(max_x)

        d = f.read()
        print(d)
        print('-' * max_x)
        d = d.replace('\n', '')

        dlen = len(d)
        cur = ''

        syms = []
        for c in d:
            b = ord(c)
            if not (b >= ord('0') and b <= ord('9')) and c != '.' and c not in syms:
                syms.append(c)
        print(f'symbols = {syms}')

        for i, c in enumerate(d):
            b = ord(c)
            edge = False

            if i % max_x == 0:
                cur = ''

            if b >= ord('0') and b <= ord('9'):
                cur += c
                edge = (i+1) % max_x == 0

            if cur != '' and (c == '.' or c in syms or edge):
                x, y = get_xy(i)
                x_start = x - len(cur)
                x_end = x - 1

                if edge:
                    x_start += 1

                corner1 = check_bounds((x_start-1, y-1))
                corner2 = check_bounds((x_end+1, y+1))

                #print(f'\t1={corner1} 2={corner2}')

                for iy in range(corner1[1], corner2[1]+1):
                    for ix in range(corner1[0], corner2[0]+1):
                        i = get_i((ix, iy))

                        if i >= dlen:
                            break

                        if d[i] in syms:
                            print(f'-> IN: {cur} - {d[i]} @ {get_xy(i)}')

                            for sy in range(corner1[1], corner2[1]+1):
                                l = corner2[0] - corner1[0] + 1
                                si = get_i((corner1[0], sy))
                                line = d[si:si+l]
                                print(line)

                            ans += int(cur)
                            break

                #print(f'{cur} x={x_start}->{x_end} y={y}')
                print('--------------------------------------------------')
                cur = ''

    print(ans)

