import { open } from 'fs/promises';

const file = await open("./input.txt");
let ans = 0;

for await (const line of file.readLines()) {
    if (line.trim() === '') continue;

    const [name, data] = line.split(':');
    const id = parseInt(name.split(' ')[1]);
    const [winNum, holdNum] = data.trim().split('|')
        .map(x => x.trim().split(' ')
            .map(y => parseInt(y))
            .filter((v, i, a) => a.indexOf(v) == i)
        );

    let seen = []
    let score = 0;
    holdNum.forEach(num => {
        if (winNum.includes(num)) score += score === 0 ? 1 : score
    });

    ans += score;
}

await file.close();
console.log(ans);

