# AIC21 - DZ Coffee Co

import numpy as np
import torch as T
import os
from Model import *

from x_consts import *
from x_messages import decode
from x_http import Http


# This is an virtual env in openai gym format
# Due to some difficulty with the server our step function for training is always one step behind
# Procedure:
# | server -(game)-> cli
# | cli -(game)-> ENV -(state)-> cli
# | cli -(state)-> local agent -(action)-> cli
# | cli saves current game as prev_game
# | cli -(action)-> server -(new_game)-> cli
# | cli -(action, prev_game, new_game)-> ENV (step function)
# | ENV -> calculates rewards and send new_state, reward, done, info to core agent

class Env():

    def __init__(self):
        self.states = None
        self.map_template = None
        self.game = None
        self.http = Http()

    def get_state(self, game: Game, brain):
        self.game = game

        if self.states is None:  # first time
            self.states = np.zeros((1, CHANNELS, MAP_SIZE, MAP_SIZE))
            self.initialize_map_template()
            for i in range(0, CHANNELS-1):
                self.states[0, i, :, :] = self.map_template[:, :]

        vision = game.ant.visibleMap
        our_base_x, our_base_y = game.baseX, game.baseY
        last_turn_messages = self.get_last_turn_messages()

        self.states[0, 1:-1, :, :] = self.states[0, 0:-2, :, :]
        self.initialize_current_state()
        self.fetch_old_messages_data_if_just_generated(brain)
        self.add_last_turn_messages_data_to_map(last_turn_messages)
        self.add_teammate_new_positions_to_map(last_turn_messages)
        self.add_vision_data_to_map()
        self.add_self_to_map()
        self.generate_meta_data()
        # TODO: مردن مورچه ها رو هندل نکنیم؟!

        return T.tensor(self.states).float()

    def initialize_current_state(self):
        self.states[0, 0, :, :] = self.map_template[:, :]
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                if self.states[0, 1, i, j] in (STATE_WALL, STATE_UNKNOWN, STATE_ENEMY_BASE, STATE_OUR_BASE):
                    self.states[0, 0, i, j] = self.states[0, 1, i, j]

    def generate_meta_data(self):
        if self.game.antType == AntType.KARGAR:
            self.states[0, CHANNELS-1, :, :] = AntType.KARGAR.value
        elif self.game.antType == AntType.SARBAAZ:
            self.states[0, CHANNELS-1, :, :] = AntType.SARBAAZ.value

    def initialize_map_template(self):
        height, width = self.game.mapHeight, self.game.mapWidth
        border = np.zeros((MAP_SIZE, MAP_SIZE))
        border[0:height, 0: width] = STATE_UNKNOWN
        self.map_template = border

    def add_self_to_map(self):
        self.add_data_to_cell(0, self.game.ant.currentX,
                              self.game.ant.currentY, STATE_ME)

    def add_vision_data_to_map(self):
        "the ant adds its vision information to the states"
        our_base_x, our_base_y = self.game.baseX, self.game.baseY
        self.add_data_to_cell(0, our_base_x, our_base_y, STATE_OUR_BASE)

        vision = self.game.ant.visibleMap
        for cell_row in vision.cells:
            for cell in cell_row:
                if cell:
                    x, y = cell.x, cell.y
                    if cell.type == CellType.WALL.value:
                        self.add_item_to_all_states((x, y, STATE_WALL))
                    if cell.resource_type == ResourceType.BREAD.value:
                        if cell.resource_value > 0 and cell.resource_value < HIGH_RESOURCE_THRESHOLD:
                            self.add_data_to_cell(
                                0, cell.x, cell.y, STATE_BREAD_LOW)
                        elif cell.resource_value > HIGH_RESOURCE_THRESHOLD:
                            self.add_data_to_cell(
                                0, cell.x, cell.y, STATE_BREAD_HIGH)
                    if cell.resource_type == ResourceType.GRASS.value:
                        if cell.resource_value > 0 and cell.resource_value < HIGH_RESOURCE_THRESHOLD:
                            self.add_data_to_cell(
                                0, cell.x, cell.y, STATE_GRASS_LOW)
                        elif cell.resource_value > HIGH_RESOURCE_THRESHOLD:
                            self.add_data_to_cell(
                                0, cell.x, cell.y, STATE_GRASS_HIGH)

                    # ANTS
                    for ant in cell.ants:
                        if ant.antTeam == AntTeam.ALLIED.value:
                            if ant.antType == AntType.KARGAR.value:
                                self.add_data_to_cell(
                                    0, cell.x, cell.y, STATE_OUR_WORKER)
                            elif ant.antType == AntType.SARBAAZ.value:
                                self.add_data_to_cell(
                                    0, cell.x, cell.y, STATE_OUR_SOLDIER)

                        elif ant.antTeam == AntTeam.ENEMY.value:
                            if ant.antType == AntType.KARGAR.value:
                                self.add_data_to_cell(
                                    0, cell.x, cell.y, STATE_ENEMY_WORKER)
                            elif ant.antType == AntType.SARBAAZ.value:
                                self.add_data_to_cell(
                                    0, cell.x, cell.y, STATE_ENEMY_SOLDIER)

                    # ENEMY BASE
                    if cell.type == CellType.BASE.value:
                        if cell.x != our_base_x or cell.y != our_base_y:
                            self.add_item_to_all_states(
                                (x, y, STATE_ENEMY_BASE))

    def get_last_turn_number(self):
        all_chats = self.game.chatBox.allChats
        return all_chats[-1].turn if len(all_chats) else -1

    def get_last_turn_messages(self):
        last_turn_number = self.get_last_turn_number()
        chats = []
        if last_turn_number != -1:
            for chat in reversed(self.game.chatBox.allChats):
                if chat.turn == last_turn_number:
                    chats.append(chat)
                else:
                    break
        return chats

    def add_teammate_new_positions_to_map(self, last_turn_messages):
        for chat in last_turn_messages:
            locations_info, action = decode(chat.text)
            for info in locations_info:
                x, y, kind = info
                if kind == STATE_ME_WORKER or kind == STATE_ME_SOLDIER:
                    new_x, new_y = self.get_new_position(
                        x, y, DIRECTION_OFFSETS[action])
                    if kind == STATE_ME_WORKER:
                        self.add_data_to_cell(
                            0, new_x, new_y, STATE_OUR_WORKER)
                    elif kind == STATE_ME_SOLDIER:
                        self.add_data_to_cell(
                            0, new_x, new_y, STATE_OUR_SOLDIER)
                    break

    def get_new_position(self, old_x, old_y, offset):
        new_x, new_y = old_x+offset[0], old_y+offset[1]
        if new_x < 0:
            new_x = self.game.mapWidth - 1
        elif new_y < 0:
            new_y = self.game.mapHeight - 1
        elif new_x > self.game.mapWidth - 1:
            new_x = 0
        elif new_y > self.game.mapHeight - 1:
            new_y = 0
        if self.states[0, 0, new_y, new_x] == STATE_WALL:
            new_x, new_y = old_x, old_y
        return new_x, new_y

    def add_last_turn_messages_data_to_map(self, messages):
        for chat in messages:
            locations_info, action = decode(chat.text)
            for info in locations_info:
                # نباید پوزیشن خودشو اضافه کنه! چون فک میکنه دوستشه
                self.add_data_to_cell(1, *info)

    def add_data_to_cell(self, channel, x, y, kind):
        "with handling priority"
        if PRIORITY[kind] > PRIORITY[self.states[0, channel, y, x]]:
            self.states[0, channel, y, x] = kind

    def fetch_old_messages_data_if_just_generated(self, brain):
        "reads all messages and adds the walls and enemy base data to the states."
        our_base_x, our_base_y = self.game.baseX, self.game.baseY
        self.add_item_to_all_states((our_base_x, our_base_y, STATE_OUR_BASE))

        if brain.ant_turn_number == 0:
            for chat in self.game.chatBox.allChats:
                locations_info, action = decode(chat.text)
                for info in locations_info:
                    kind = info[2]
                    if kind == STATE_ENEMY_BASE or kind == STATE_WALL:
                        self.add_item_to_all_states(info)

    def add_item_to_all_states(self, item):
        x, y, kind = item
        for i in range(0, CHANNELS-1):
            self.add_data_to_cell(i, x, y, kind)

    def calc_reward(self, prev_game: Game, curr_game: Game):
        if prev_game == None:
            return 0

        reward = 0
        ant = curr_game.ant
        attacks = ant.attacks

        # Moving resources to our base
        if ant.antType == AntType.KARGAR.value:
            if ant.currentResource.value == 0 and prev_game.ant.currentResource.value != 0:
                if prev_game.ant.currentResource.type == ResourceType.BREAD.value:
                    reward += prev_game.ant.currentResource.value * REWARD_BREAD_TO_BASE
                elif prev_game.ant.currentResource.type == ResourceType.GRASS.value:
                    reward += prev_game.ant.currentResource.value * REWARD_GRASS_TO_BASE

        for attack in attacks:
            # Getting damaged
            if attack.is_attacker_enemy:
                if attack.defender_row == curr_game.baseX and attack.defender_col == curr_game.baseY:
                    # TODO: to be checked --> does it need to calculate based on base's health??
                    reward += REWARD_GOT_DAMAGED_BASE
                elif attack.defender_row == ant.currentX and attack.defender_col == ant.currentY and prev_game.ant.health != ant.health:
                    damage = prev_game.ant.health-ant.health  # damage > 0
                    # damage = 1 # TODO: is this needed or not?
                    if ant.antType == AntType.SARBAAZ.value:
                        reward += damage * REWARD_GOT_DAMAGED_SOLDIER
                    elif ant.antType == AntType.KARGAR.value:
                        reward += damage * REWARD_GOT_DAMAGED_WORKER

            else:
                # Attacking from us
                if attack.attacker_row == ant.currentX and attack.attacker_col == ant.currentY and ant.antType == AntType.SARBAAZ.value:
                    if self.states(0, 0, attack.defender_row, attack.defender_col) == STATE_ENEMY_BASE:
                        reward += REWARD_ATTACK_TO_ENEMY_BASE
                    elif self.states(0, 0, attack.defender_row, attack.defender_col) == STATE_ENEMY_SOLDIER:
                        reward += REWARD_ATTACK_TO_ENEMY_SOLDIER
                    elif self.states(0, 0, attack.defender_row, attack.defender_col) == STATE_ENEMY_WORKER:
                        reward += REWARD_ATTACK_TO_ENEMY_WORKER

        return reward

    def virtualize_state(self, folder, turn_number):
        output = ''
        for i in range(CHANNELS):
            for j in range(self.game.mapHeight):
                for k in range(self.game.mapWidth):
                    output += f" {VIRTUALIZE_DICT[int(self.states[0, i, j, k])]}"
                output += '\n'
            output += '\n'
        if not os.path.exists(f"logs\{str(folder)}"):
            os.mkdir(f"logs\{str(folder)}")
        with open(f"logs\{str(folder)}\{turn_number}.txt", 'w', encoding="utf8") as f:
            f.write(output)

    def step(self, state, action, reward, state_, done, turn_number: int):
        if turn_number == 0:
            print('[!] Skipping env.step for first turn.')

        # TODO: Send state, action, reward, state_, done to agent (network call)

        self.http.send(state, action, reward, state_, done, turn_number)

    def get_epsilon(self):
        return self.http.get_epsilon()
