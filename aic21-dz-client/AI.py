from Model import *
from datetime import datetime
from typing import *
from copy import deepcopy
from x_env import Env
from x_agent import Agent
from x_messages import generate_message
import numpy as np

DEBUG = False
TRAIN = False


class Brain:
    def __init__(self):
        self.env = Env()
        self.agent = Agent(5, [11, 35, 35], TRAIN)

        self.prev_game: Game = None
        self.prev_action = None
        self.prev_state = None
        self.prev_reward = None

        self.ant_turn_number = 0


brain = Brain()
my_id = f"{datetime.now().minute}.{datetime.now().second}"


class AI:
    def __init__(self):
        # Current Game State
        self.game: Game = None

        # Answer
        self.message: str = None
        self.direction: int = None
        self.value: int = None

    def turn(self):
        if brain.ant_turn_number == 0:
            print(
                f'[+] Client started in {"TRAIN" if TRAIN else "RELEASE"} mode')
            print(
                f'[+] Started agent (X={self.game.ant.currentX} Y={self.game.ant.currentY}), type={self.game.antType}')
        print(f'[i] Ant turn number:', brain.ant_turn_number)

        state = brain.env.get_state(self.game, brain)
        reward = brain.env.calc_reward(brain.prev_game, self.game)
        state /= 16  # normalize state

        # TRAIN MODE
        if TRAIN:
            action = None
            epsilon = brain.env.get_epsilon()
            if np.random.random() > epsilon:
                action = brain.agent.choose_action(state)
                print(f'[+] Agent action: {action}')
            else:
                action = brain.agent.get_random_action()
                print(f'[+] Random action: {action}')

            # Load trained network from core agent every 5 games
            brain.env.step(brain.prev_state, brain.prev_action,
                           brain.prev_reward, state, False, brain.ant_turn_number)

            if brain.ant_turn_number % 5 == 0 and brain.ant_turn_number > 0:
                brain.agent.dq_network.load_checkpoint()

        # RELEASE MODE
        if not TRAIN:
            action = brain.agent.choose_action(state)

        if DEBUG:
            brain.env.virtualize_state(my_id, brain.ant_turn_number)

        # action = Direction.UP.value

        brain.prev_game = deepcopy(self.game)
        brain.prev_state = deepcopy(state)
        brain.prev_action = deepcopy(action)
        brain.prev_reward = deepcopy(reward)

        # Increment turn number
        brain.ant_turn_number += 1

        print(f'[+] Action: {action}')

        m_text, m_value = generate_message(self.game)
        m_text += f'A{action}'

        return (m_text, m_value, action)
