import os
import torch as T
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np


class DeepQNetwork(nn.Module):
    def __init__(self, lr, n_actions, name, input_dims, chkpt_dir):
        super(DeepQNetwork, self).__init__()

        self.name = name
        self.checkpoint_dir = chkpt_dir

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

    def save_checkpoint(self, episode):
        checkpoint_file = os.path.join(
            self.checkpoint_dir, f"{episode}_{self.name}")
        print(f"[!] saving checkpoint for {self.name} #{episode}")
        T.save(self.state_dict(), checkpoint_file)

    def load_checkpoint(self, episode):
        checkpoint_file = os.path.join(
            self.checkpoint_dir, f"{episode}_{self.name}")
        print(f"[!] loading checkpoint for {self.name} #{episode}")
        self.load_state_dict(T.load(checkpoint_file))


""" test = DeepQNetwork(0.0001, 5, 'asd', [11, 35, 35], 'models/')
f = test.forward(T.zeros(1, *[11, 35, 35]))
print(f)
test.save_checkpoint(4)
 """
