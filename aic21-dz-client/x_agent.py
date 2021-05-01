import numpy as np
import torch as T
from x_dq_network import DeepQNetwork


class Agent():

    def __init__(self, n_actions, input_dims, TRAIN):

        # lr is not needed
        self.dq_network = DeepQNetwork(n_actions=n_actions,  input_dims=input_dims,
                                       name='1', chkpt_dir='models/',
                                       lr=0.99, TRAIN=TRAIN)

        self.dq_network.load_checkpoint()

    def choose_action(self, state):
        random_state = state.to(self.dq_network.device)
        V, actions = self.dq_network.forward(random_state)
        action = T.argmax(actions).item()
        return action

    def get_random_action(self):
        return np.random.choice(5)
