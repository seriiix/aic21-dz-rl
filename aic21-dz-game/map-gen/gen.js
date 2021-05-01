
const BAS1 = 0
const BAS2 = 1
const EMPT = 2
const WALL = 3


map = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
]

console.log(map.length, map[0].length)

res = {
    MAP_HEIGHT: map.length,
    MAP_WIDTH: map[0].length,
    SHIFT_X: 0,
    SHIFT_Y: 0,
    cells_type: []
}

for (let i = 0; i < map.length; i++) {
    for (let j = 0; j < map[i].length; j++) {
        res.cells_type.push({
            row: i,
            col: j,
            cell_type: map[i][j],
            rec1: 0,
            rec2: 0
        })
    }
}

const { writeFileSync } = require('fs')
writeFileSync('map.json', JSON.stringify(res))