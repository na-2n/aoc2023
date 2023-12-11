import { open } from 'fs/promises';

const file = await open("./input.txt");
const cards = [];
let wonCards = [];
let ans = 0;

for await (let line of file.readLines()) {
    line = line.trim()

    if (line === '') continue;

    const [name, data] = line.split(':');
    const id = parseInt(name.split(/\s+/g)[1].trim());
    const card = data.trim().split('|')
        .map(x => x.trim().split(/\s+/g)
            .map(y => parseInt(y))
        );
    const score = card[1].filter(x => card[0].includes(x)).length;

    for (let i = 0; i < score; i++) {
        wonCards.push(id + 1 + i);
    }
    cards.push({ id, card, score });
}

const MAX_ID = cards[cards.length-1].id;

const iterCards = inCards => {
    const cardz = [];

    for (const id of inCards) {
        const { score } = cards.find(x => x.id == id);

        for (let i = 0; i < score; i++) {
            const won = id + 1 + i;

            if (won <= MAX_ID) {
                cardz.push(won)
            }
        }
    }

    if (cardz.length > 0) {
        wonCards = [...wonCards, ...cardz];
        iterCards(cardz)
    }
};

iterCards(wonCards);

ans = wonCards.length + cards.length;

await file.close();
console.log(ans);

