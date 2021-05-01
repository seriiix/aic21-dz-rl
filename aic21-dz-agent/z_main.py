# Main Runner for DZ-Coffee-Co Team AIC21

import numpy as np
import os
from z_agent import DuelingDDQNAgent
# from z_game_runner import GameRunner


class Main():

    def __init__(self):

        NUMBER_OF_ACTIONS = 5
        OBSERVATION_SPACE_SHAPE = [11, 35, 35]
        MEMORY_SIZE = 20000
        REPLACE_TARGET_NETWORK = 5000
        BATCH_SIZE = 32
        EPS_MIN = 0.1
        EPS_DEC = 1e-5
        GAMMA = 0.99
        EPSILON = 1.0
        LR = 0.0001

        self.train_counter = 0

        print('[+] DZ Coffee Co Trainer for AIC21')

        print('[i] Loading 3DQN Agent...')
        self.agent = DuelingDDQNAgent(gamma=GAMMA, epsilon=EPSILON, lr=LR,
                                      input_dims=OBSERVATION_SPACE_SHAPE, n_actions=NUMBER_OF_ACTIONS,
                                      mem_size=MEMORY_SIZE, eps_min=EPS_MIN,
                                      batch_size=BATCH_SIZE, replace=REPLACE_TARGET_NETWORK, eps_dec=EPS_DEC,
                                      chkpt_dir='models/')

        if self.find_model_number() == 1:
            print(
                f'[i] Generating initial model #{self.find_model_number()}...')
            self.agent.save_models(self.find_model_number())
        else:
            print(
                f'[i] Loading latest model #{self.find_model_number() - 1}...')
            self.agent.load_models(self.find_model_number() - 1)

    def recieved_data(self, data):
        state = np.array(data['state'])
        action = np.int(data['action'])
        reward = np.float(data['reward'])
        state_ = np.array(data['state_'])
        done = np.bool(data['done'])

        if reward > 0:
            print('yeaaaa')

        if state.shape != (11, 35, 35) or state_.shape != (11, 35, 35):
            print('[X]: STATE SHAPE IS WRONG:', state.shape)
            return

        self.agent.store_transition(state, action, reward, state_, done)
        self.train_counter += 1

        if (self.train_counter % 10 == 0):
            learning_result = self.agent.learn()
            if learning_result == True:
                self.agent.save_models(self.find_model_number())

    def get_epsilon(self):
        return self.agent.epsilon

    def find_model_number(self):
        models_dir = os.path.join('models/')
        if not os.path.exists(models_dir):
            os.mkdir(models_dir)

        files = os.listdir('models/')
        return int(((len(files)) / 3) + 1)
