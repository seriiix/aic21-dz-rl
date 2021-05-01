# -----------|-----
# POS-11 | KIND-5
from Model import Game, ChatBox, CellType, ResourceType, AntTeam, AntType
from x_consts import MESSAGES, MESSAGE_TYPE

hash_index = 0
hash_index_to_pos = []
hash_pos_to_index = {}

IGNORE_CHAR = 60000
MAX_MESSAGE_LENGTH = 30

# handling hashes
for i in range(35):
    for j in range(35):
        hash_index_to_pos.append([i, j])
        hash_pos_to_index[(i, j)] = hash_index
        hash_index += 1


# encode message function
def encode(data):
    message = ""
    for i in range(len(data)):
        x = data[i][0]
        y = data[i][1]
        kind = data[i][2]

        pos = hash_pos_to_index[(x, y)]
        pos_str = f"{pos:b}"
        while len(pos_str) < 11:
            pos_str = "0" + pos_str

        kind_str = f"{kind:b}"
        while len(kind_str) < 5:
            kind_str = "0" + kind_str

        final_str = pos_str + kind_str
        message += chr(int(final_str, 2))

    while len(message) < MAX_MESSAGE_LENGTH:
        message += chr(IGNORE_CHAR)
    return message


# decode message function
def decode(text):
    res = []
    for i in range(len(text)):
        if ord(text[i]) == IGNORE_CHAR or i >= MAX_MESSAGE_LENGTH:
            break

        bin = f"{ord(text[i]):b}"
        while len(bin) < 16:
            bin = "0" + bin

        pos_str = bin[:11]
        kind_str = bin[11:]

        index = int(pos_str, 2)
        pos = hash_index_to_pos[index]
        x = pos[0]
        y = pos[1]

        kind = int(kind_str, 2)

        res.append((x, y, kind))

    # action is on last index
    action = int(text[31])
    return res, action


def search_message(curr_messages, m):
    for i in range(len(curr_messages)):
        if curr_messages[i][0] == m[0] and curr_messages[i][1] == m[1]:
            return i
    return -1


def handle_messages_priority(curr_messages, m):
    m_pos = search_message(curr_messages, m)
    if m_pos == -1:
        curr_messages.append(m)
    else:
        curr_mt: MESSAGE_TYPE = curr_messages[m_pos][2]
        new_mt: MESSAGE_TYPE = m[2]
        if new_mt.priority > curr_mt.priority:
            curr_messages[m_pos] = m
    return curr_messages


def seen_static_cells(chat_box: ChatBox):
    seen_walls = []
    seen_enemy_base = None

    for chat in chat_box.allChats:
        msgs, action = decode(chat.text)
        for msg in msgs:
            if msg[2] == MESSAGES['WALL'].code:
                seen_walls.append([msg[0], msg[1]])
            if msg[2] == MESSAGES['ENEMY_BASE'].code:
                seen_enemy_base = [msg[0], msg[1]]

        # print('TURN:', chat.turn, '-> ', decode(chat.text))

    return seen_walls, seen_enemy_base


def generate_message(game: Game):
    vision = game.ant.visibleMap
    our_base_x = game.baseX
    our_base_y = game.baseY

    seen_walls, seen_enemy_base = seen_static_cells(game.chatBox)
    curr_messages = []

    for cell_row in vision.cells:
        for cell in cell_row:
            if cell:
                # print(cell.__dict__)
                # WALL
                if cell.type == CellType.WALL.value:
                    m = [cell.x, cell.y, MESSAGES['WALL']]
                    # handle wall recreation
                    flag = True
                    for wall in seen_walls:
                        if m[0] == wall[0] and m[1] == wall[1]:
                            flag = False
                            break
                    if flag:
                        curr_messages = handle_messages_priority(
                            curr_messages, m)

                # RESOURCES
                if cell.resource_type == ResourceType.BREAD.value:
                    if cell.resource_value > 0 and cell.resource_value < 10:
                        m = [cell.x, cell.y, MESSAGES['BREAD_LOW']]
                        curr_messages = handle_messages_priority(
                            curr_messages, m)
                    elif cell.resource_value > 10:
                        m = [cell.x, cell.y, MESSAGES['BREAD_HIGH']]
                        curr_messages = handle_messages_priority(
                            curr_messages, m)

                if cell.resource_type == ResourceType.GRASS.value:
                    if cell.resource_value > 0 and cell.resource_value < 10:
                        m = [cell.x, cell.y, MESSAGES['GRASS_LOW']]
                        curr_messages = handle_messages_priority(
                            curr_messages, m)
                    elif cell.resource_value > 10:
                        m = [cell.x, cell.y, MESSAGES['GRASS_HIGH']]
                        curr_messages = handle_messages_priority(
                            curr_messages, m)

                # ANTS
                for ant in cell.ants:
                    # print(ant.__dict__)

                    if ant.antTeam == AntTeam.ALLIED.value:  # our ant
                        if ant.antType == AntType.KARGAR.value:  # worker
                            m = [ant.currentX, ant.currentY,
                                 MESSAGES['OUR_WORKER']]
                            curr_messages = handle_messages_priority(
                                curr_messages, m)
                        elif ant.antType == AntType.SARBAAZ.value:  # soldier
                            m = [ant.currentX, ant.currentY,
                                 MESSAGES['OUR_SOLDIER']]
                            curr_messages = handle_messages_priority(
                                curr_messages, m)

                    elif ant.antTeam == AntTeam.ENEMY.value:  # enemy ant
                        if ant.antType == AntType.KARGAR.value:  # worker
                            m = [ant.currentX, ant.currentY,
                                 MESSAGES['ENEMY_WORKER']]
                            curr_messages = handle_messages_priority(
                                curr_messages, m)
                        elif ant.antType == AntType.SARBAAZ:  # soldier
                            m = [ant.currentX, ant.currentY,
                                 MESSAGES['ENEMY_SOLDIER']]
                            curr_messages = handle_messages_priority(
                                curr_messages, m)

                # ENEMY BASE
                if cell.type == CellType.BASE.value:
                    if cell.x != our_base_x or cell.y != our_base_y:
                        if seen_enemy_base == None:
                            m = [cell.x, cell.y, MESSAGES['ENEMY_BASE']]
                            curr_messages = handle_messages_priority(
                                curr_messages, m)

    # ME
    if game.antType == AntType.SARBAAZ.value:
        m = [game.ant.currentX, game.ant.currentY, MESSAGES['ME_SOLDIER']]
        curr_messages = handle_messages_priority(curr_messages, m)
    elif game.antType == AntType.KARGAR.value:
        m = [game.ant.currentX, game.ant.currentY, MESSAGES['ME_WORKER']]
        curr_messages = handle_messages_priority(curr_messages, m)

    # TODO: if message length exceeded MAX_MESSAGE_LENGTH only send first MAX_MESSAGE_LENGTH important observations
    if len(curr_messages) > MAX_MESSAGE_LENGTH:
        curr_messages = curr_messages[:MAX_MESSAGE_LENGTH]

    # Generate message text and value

    m_value = 0
    m_fixed = []
    for m in curr_messages:
        m_fixed.append([m[0], m[1], m[2].code])
        m_value += m[2].value

    m_text = encode(m_fixed)
    return m_text, m_value
