import os
import torch as T
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np


class DeepQNetwork(nn.Module):
    def __init__(self, lr, n_actions, name, input_dims, chkpt_dir, TRAIN):
        super(DeepQNetwork, self).__init__()

        self.name = name
        self.checkpoint_dir = chkpt_dir
        self.TRAIN = TRAIN

        self.conv1 = nn.Conv2d(input_dims[0], 20, 5)
        self.conv2 = nn.Conv2d(20, 30, 3)
        self.conv3 = nn.Conv2d(30, 30, 3)

        fc_input_dims = self.calculate_conv_output_dims(input_dims)

        self.fc1 = nn.Linear(fc_input_dims, 120)
        self.fc2 = nn.Linear(120, 120)
        self.V = nn.Linear(120, 1)
        self.A = nn.Linear(120, n_actions)

        self.optimizer = optim.Adam(self.parameters(), lr=lr)
        self.loss = nn.MSELoss()
        # self.device = T.device('cuda:0' if T.cuda.is_available() else 'cpu')
        self.device = 'cpu'
        self.to(self.device)

    def calculate_conv_output_dims(self, input_dims):
        state = T.zeros(1, *input_dims)
        dims = self.conv1(state)
        dims = self.conv2(dims)
        dims = self.conv3(dims)
        return int(np.prod(dims.size()))

    def forward(self, state):
        conv1 = F.relu(self.conv1(state))
        conv2 = F.relu(self.conv2(conv1))
        conv3 = F.relu(self.conv3(conv2))
        conv_state = conv3.view(conv3.size()[0], -1)
        flat1 = F.relu(self.fc1(conv_state))
        flat2 = F.relu(self.fc2(flat1))

        V = self.V(flat2)
        A = self.A(flat2)

        return V, A

    def load_checkpoint(self):
        if self.TRAIN:
            models_dir = os.path.join('../aic21-dz-agent/models')
            model_num = self.find_model_number(models_dir)
            self.load_state_dict(
                T.load(os.path.join(models_dir, f'{model_num-1}_eval')))
            print(f"[+] Loaded checkpoint #{model_num-1}")
        else:
            self.load_checkpoint_release()

    def load_checkpoint_release(self):
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        T.load(os.path.join(curr_dir, 'model'))
        print(f'[+] Loaded release model')

    def find_model_number(self, models_dir):
        tmp = os.listdir(models_dir)
        return int(((len(tmp)) / 3) + 1)


""" test = DeepQNetwork(0.0001, 5, 'asd', [11, 35, 35], 'models/')
f = test.forward(T.zeros(1, *[11, 35, 35]))
T.save(test.state_dict(), '1_eval')
print(f)
 """
