from enum import Enum
from Model import Direction
# Constants of AIC21
MAX_COM_PER_TURN = 5


# NEURAL NETWORK
MAP_SIZE = 35
CHANNELS = 11

# MESSAGES


class MESSAGE_TYPE:
    __slots__ = ('name', 'code', 'priority', 'value')

    def __init__(self, name: str, code: int, priority: int, value: int):
        self.name = name  # name of the observation
        self.code = code  # code of the observation
        self.priority = priority  # priority inside the state
        self.value = value  # value of this observation


# STATES CELLS DATA TYPES
STATE_INVALID = 0
STATE_UNKNOWN = 1
STATE_WALL = 2
STATE_GRASS_LOW = 3
STATE_GRASS_HIGH = 4
STATE_BREAD_LOW = 5
STATE_BREAD_HIGH = 6
STATE_ME_WORKER = 7
STATE_ME_SOLDIER = 8
STATE_OUR_WORKER = 9
STATE_OUR_SOLDIER = 10
STATE_OUR_BASE = 11
STATE_ENEMY_WORKER = 12
STATE_ENEMY_SOLDIER = 13
STATE_ENEMY_BASE_ESTIMATE = 14
STATE_ENEMY_BASE = 15
STATE_ME = 16

# FOR VIRTUALIZE
VIRTUALIZE_DICT = {
    STATE_INVALID : "❕",
    STATE_UNKNOWN : "✖️",
    STATE_WALL : "⬜️",
    STATE_GRASS_LOW : "🟢",
    STATE_GRASS_HIGH : "🟩",
    STATE_BREAD_LOW : "🟡",
    STATE_BREAD_HIGH : "🟨",
    STATE_ME_WORKER : "👤w",
    STATE_ME_SOLDIER : "👤s",
    STATE_OUR_WORKER : "🐜",
    STATE_OUR_SOLDIER : "🦀",
    STATE_OUR_BASE : "🟦",
    STATE_ENEMY_WORKER : "🤖",
    STATE_ENEMY_SOLDIER : "💀",
    STATE_ENEMY_BASE_ESTIMATE : "EnBS",
    STATE_ENEMY_BASE : "🟥",
    STATE_ME : "💂🏻‍♂️"
}


MESSAGES = {
    'ME_WORKER': MESSAGE_TYPE(name='ME', code=STATE_ME_WORKER, priority=100, value=1),
    'ME_SOLDIER': MESSAGE_TYPE(name='ME', code=STATE_ME_SOLDIER, priority=100, value=1),
    'WALL': MESSAGE_TYPE(name='WALL', code=STATE_WALL, priority=1, value=1),
    'BREAD_LOW': MESSAGE_TYPE(name='BREAD_LOW', code=STATE_BREAD_LOW, priority=2, value=2),
    'BREAD_HIGH': MESSAGE_TYPE(name='BREAD_HIGH', code=STATE_BREAD_HIGH, priority=2, value=3),
    'GRASS_LOW': MESSAGE_TYPE(name='GRASS_LOW', code=STATE_GRASS_LOW, priority=2, value=2),
    'GRASS_HIGH': MESSAGE_TYPE(name='GRASS_HIGH', code=STATE_GRASS_HIGH, priority=2, value=3),
    'OUR_WORKER': MESSAGE_TYPE(name='OUR_WORKER', code=STATE_OUR_WORKER, priority=3, value=5),
    'OUR_SOLDIER': MESSAGE_TYPE(name='OUR_SOLDIER', code=STATE_OUR_SOLDIER, priority=4, value=6),
    'ENEMY_WORKER': MESSAGE_TYPE(name='ENEMY_WORKER', code=STATE_ENEMY_WORKER, priority=5, value=8),
    'ENEMY_SOLDIER': MESSAGE_TYPE(name='ENEMY_SOLDIER', code=STATE_ENEMY_SOLDIER, priority=6, value=9),
    'ENEMY_BASE': MESSAGE_TYPE(name='ENEMY_BASE', code=STATE_ENEMY_BASE, priority=7, value=20),
}

# THRESHOLDS
HIGH_RESOURCE_THRESHOLD = 10

# REWARDS
REWARD_BREAD_TO_BASE = 1
REWARD_GRASS_TO_BASE = 1
REWARD_ATTACK_TO_ENEMY_WORKER = 3
REWARD_ATTACK_TO_ENEMY_SOLDIER = 3
REWARD_ATTACK_TO_ENEMY_BASE = 20
REWARD_GOT_DAMAGED_SOLDIER = -1
REWARD_GOT_DAMAGED_WORKER = -1
REWARD_GOT_DAMAGED_BASE = 0

# PRIORITY FOR ADDING DATA TO STATES
PRIORITY = {
    STATE_INVALID: 0,
    STATE_UNKNOWN: 1,
    STATE_WALL: 2,
    STATE_GRASS_LOW: 3,
    STATE_GRASS_HIGH: 4,
    STATE_BREAD_LOW: 5,
    STATE_BREAD_HIGH: 6,
    STATE_ME_WORKER: 7,
    STATE_ME_SOLDIER: 8,
    STATE_OUR_WORKER: 9,
    STATE_OUR_SOLDIER: 10,
    STATE_OUR_BASE: 11,
    STATE_ENEMY_WORKER: 12,
    STATE_ENEMY_SOLDIER: 13,
    STATE_ENEMY_BASE_ESTIMATE: 14,
    STATE_ENEMY_BASE: 15,
    STATE_ME: 16
}

DIRECTION_OFFSETS = {
    Direction.CENTER.value: (0, 0),
    Direction.DOWN.value: (0, 1),
    Direction.UP.value: (0, -1),
    Direction.RIGHT.value: (1, 0),
    Direction.LEFT.value: (-1, 0)
}
